from qt_core import *
import json
import os
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
from view.widgets.py_color_delegate import PyColorDelegate
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
# IMPORTS NEWS RATING
# from models.news_rating.dataframe_fuctions import DataFrame
# from models.news_rating.doc_to_vector import DocToVector
# from models.news_rating.model_prediction import ModelPrediction
from models.utils.data import *

class TableNewsManager:
    def __init__(self, table_news=None, table_page=None, show_page_class=None, set_text_class=None, set_title_list=None) -> None:
        """
        Initializes the `TableNewsManager` class, sets up the table view, and configures various components.

        Sets up connections to the database, initializes global variables, and configures table model and buttons.
        
        Args:
            table_news (QTableView): The table view widget for displaying news.
            table_page (QWidget): The widget containing table-related UI elements.
            show_page_class (Callable): Callback function to show the classification page.
            set_text_class (Callable): Callback function to set the classification text.
            set_title_list (Callable): Callback function to set the list of titles.
        """
        self.table_news = table_news
        self.table_page = table_page
        self.show_page_class = show_page_class
        self.set_title_list = set_title_list
        self.set_text_class = set_text_class
        
        # DB_VARIABLES
        self.__db_handle = DBConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__news_repository = NewsClassRepository(self.__db_connection)
        
        
        # VARIABLES GLOBAL
        self.title_list = []
        self.title_news = ""
        self.toggle_order = Qt.AscendingOrder
        self.num_columns = 6
        self.filtro = ""
        self.dir = os.path.dirname(os.path.abspath(__file__)) 
        self.path_filtro = os.path.join(self.dir, "filtro.json") 
        
        # TABLE MODEL NEWS
        self.model_table = QStandardItemModel()
        self.model_table.setHorizontalHeaderLabels(["Data de Publicação", "Jornal", "Título", "Relevância Manual", "Relevância Automática", "Nível de Certeza", "ID"])
        self.table_news.setModel(self.model_table)
        self.table_news.setItemDelegate(PyColorDelegate(self.table_news))
        # Definir a ordem de classificação na QTableView
        
        # BUTTONS CONNECTS
        self.table_news.doubleClicked.connect(self.on_selection_table)
        self.table_page.button_note.clicked.connect(self.on_selection_table)
        self.table_page.button_filter.clicked.connect(self.set_filters)
        
        # INIT COMBO TABLE
        self.init_combo_box(self.table_page.combo_filter_year, data_years)
        self.init_combo_box(self.table_page.combo_filter_month, data_months)
        self.init_combo_box(self.table_page.combo_filter_day, data_day)
        self.init_combo_box(self.table_page.comboBox_relevance, data_relevance)
        self.init_combo_box(self.table_page.comboBox_news, data_newspaper)
        
        # INIT STATUS
        self.set_status()
    
            
    def populate_table_news(self):
        """
        Populates the table with news data from the database.

        Retrieves news data based on filters stored in `filtro.json`, maps relevance classes to readable strings,
        and updates the table model with the news data.
        """
        try:
            if os.path.exists(self.path_filtro):
                with open(self.path_filtro, 'r') as file_filtro:
                    self.filtro = json.load(file_filtro)
                
            list_news = self.__news_repository.select_many_order_news(filters=self.filtro, optionsReturn={"_id": 0,"publication_date": 1, "newspaper": 1, "title": 1, "manual_relevance_class": 1, "automatic_relevance_class": 1, "id_event": 1, "certainty_level": 1}, orderFilter='manual_relevance_class', optionsFilter=1, model_return=False)
            mapping = {0: "Irrelevante", 1: "Relevante", 2: "Dúvida", None: "SClasse"}
            
            self.model_table.clear()
            
            # TABLE MODEL NEWS
            self.model_table = QStandardItemModel()
            self.model_table.setHorizontalHeaderLabels(["Data de Publicação", "Jornal", "Título", "Relevância Manual", "Relevância Automática", "Nível de Certeza", "ID"])
            self.table_news.setModel(self.model_table)
            self.table_news.setItemDelegate(PyColorDelegate(self.table_news))                 
                    
            for row, dict_news in enumerate(list_news):
                try:
                    dict_news["manual_relevance_class"] = mapping.get(dict_news["manual_relevance_class"])
                except KeyError:
                    dict_news["manual_relevance_class"] = None
                    dict_news["manual_relevance_class"] = mapping.get(dict_news["manual_relevance_class"])
                try:
                    dict_news["automatic_relevance_class"] = mapping.get(dict_news["automatic_relevance_class"])
                except KeyError:
                    dict_news["automatic_relevance_class"] = None
                    dict_news["automatic_relevance_class"] = mapping.get(dict_news["automatic_relevance_class"])
                                        
                for column, label in enumerate(dict_news):
                    item = QStandardItem(str(dict_news[label]))
                    if label == 'publication_date': self.model_table.setItem(row, 0, item)
                    if label == 'newspaper': self.model_table.setItem(row, 1, item)
                    if label == 'title': self.model_table.setItem(row, 2, item)
                    if label == 'manual_relevance_class': self.model_table.setItem(row, 3, item)
                    if label == 'automatic_relevance_class': self.model_table.setItem(row, 4, item)
                    if label == 'certainty_level': self.model_table.setItem(row, 5, item)                 
                    if label == 'id_event': self.model_table.setItem(row, 6, item)                    
                                  
                    if not column == 2:
                        item.setTextAlignment(Qt.AlignCenter)       
                                    
            self.table_news.setColumnWidth(2, 570)
            self.get_filters()
                        
        except Exception as e:
            print("Erro ao popular tabela de notícias:", e)
            
    def set_status(self):
        """
        Updates the status labels on the table page with counts of total, relevant, irrelevant, evaluated, and non-evaluated news items.

        Retrieves counts from the database and updates the corresponding labels on the UI.
        """
        total = self.__news_repository.get_count()
        relevance = self.__news_repository.get_count({"manual_relevance_class": 1})
        irrelevant = self.__news_repository.get_count({"manual_relevance_class": 0})
        evaluated = 0 if (relevance + irrelevant) < 0 else (relevance + irrelevant)
        no_evaluated = 0 if (total - evaluated) < 0 else (total - evaluated)
                
        self.table_page.lab_count_total.setText(str(total))
        self.table_page.lab_irrelevant.setText(str(irrelevant))
        self.table_page.lab_relevance.setText(str(relevance))
        self.table_page.lab_evaluated.setText(str(evaluated))
        self.table_page.lab_not_evaluated.setText(str(no_evaluated))
            
    def set_filters(self):
        """
        Applies filters based on user input and updates the table with filtered news data.

        Retrieves filter criteria from UI elements, updates the `filtro` dictionary, and saves it to `filtro.json`.
        Then, populates the table with news data that matches the filters.
        """
        title = self.table_page.lineEdit.text()
        year = self.table_page.combo_filter_year.currentData()
        months = self.table_page.combo_filter_month.currentData()
        day = self.table_page.combo_filter_day.currentData()
        relevance = self.table_page.comboBox_relevance.currentData()
        newspaper = self.table_page.comboBox_news.currentData()
        
        search_date = f"{day}-{months}-{year}"
        search_date = {"$regex": search_date}
        
        self.filtro = {"publication_date": search_date}
        
        if title != "":
            title = f".*{title}.*"
            self.filtro["title"] = {"$regex": title}
        if relevance is not None:
            self.filtro["manual_relevance_class"] = relevance
        if newspaper is not None:
            self.filtro["newspaper"] = newspaper
        
        with open(self.path_filtro, 'w') as arquivo:
            json.dump(self.filtro, arquivo)
        
        self.populate_table_news()
            
    # Get Filters             
    def get_filters(self):
        """
        Updates UI elements with the current filter criteria.

        Retrieves filter criteria from the `filtro` dictionary and sets the corresponding values in the UI elements.
        """
        if "title" in self.filtro:
            title = self.filtro["title"]['$regex']
            self.table_page.lineEdit.setText(title)
        
        if "publication_date" in self.filtro:
            datas = self.filtro["publication_date"]['$regex'].split("-")
            
            if datas[0] == r"\d{2}": self.table_page.combo_filter_day.setCurrentIndex(0)
            else: self.table_page.combo_filter_day.setCurrentIndex(int(datas[0]))
            
            if datas[1] == r"\d{2}": self.table_page.combo_filter_month.setCurrentIndex(0)
            else: self.table_page.combo_filter_month.setCurrentIndex(int(datas[1]))
            
            if datas[2] == r"\d{4}": self.table_page.combo_filter_year.setCurrentIndex(0)
            else: self.table_page.combo_filter_year.setCurrentText(datas[2])
        
        if "manual_relevance_class" in self.filtro:
            relevance = self.filtro['manual_relevance_class']
            if relevance == None:
                self.table_page.comboBox_relevance.setCurrentIndex(0)
            elif relevance == 1:
                self.table_page.comboBox_relevance.setCurrentIndex(1)
            elif relevance == 0:
                self.table_page.comboBox_relevance.setCurrentIndex(2)
            elif relevance == 2:
                self.table_page.comboBox_relevance.setCurrentIndex(3)
                            
        if "newspaper" in self.filtro:
            newspaper = self.filtro["newspaper"]
            if newspaper == None:
                self.table_page.comboBox_relevance.setCurrentIndex(0)
            elif newspaper == "G1":
                self.table_page.comboBox_news.setCurrentIndex(1)
            elif newspaper == "DM":
                self.table_page.comboBox_news.setCurrentIndex(2)
                
            
    def on_selection_table(self):
        """
        Handles selection of a news item in the table.

        Retrieves the ID of the selected news item, updates the title list, and displays the classification page.
        """
        selected_items = self.table_news.selectedIndexes() # O selectedItems seleciona cada celula
        num_selected = len(selected_items) // self.num_columns  # Cada linha é representada por self.num_columns células
        if num_selected == 0:
            dlg = WarningMessageBox(title="Atenção!", txt="A anotação requer a seleção de um artigo de notícias.")
            dlg.setIcon(QMessageBox.Warning)
            dlg.exec()
        else:
            title_selected = int(selected_items[6].data())
            for row in range(self.model_table.rowCount()):
                column_title = self.model_table.item(row, 6)
                self.title_list.append(int(column_title.text()))
            
            self.table_news.clearSelection()
            title_selected_id = self.title_list.index(title_selected)
            self.set_title_list(self.title_list, title_selected_id, self.model_table)
            self.set_text_class()
            self.show_page_class()

    def on_column_header_clicked(self, logical_index): # Ordenação da Table
        """
        Handles sorting of the table by column header.

        Toggles between ascending and descending order when a column header is clicked.
        
        Args:
            logical_index (int): The index of the column header that was clicked.
        """
        
        if self.toggle_order == Qt.AscendingOrder:
            self.table.sortItems(logical_index, self.toggle_order)
            self.toggle_order = Qt.DescendingOrder
            
        else:
            self.table.sortItems(logical_index, self.toggle_order)
            self.toggle_order = Qt.AscendingOrder
            
    def init_combo_box(self, combo_box, data):
        """
        Initializes a combo box with data.

        Populates the combo box with items from the provided data dictionary.
        
        Args:
            combo_box (QComboBox): The combo box to be initialized.
            data (dict): A dictionary where keys are item labels and values are item data.
        """
        for key, value in data.items():
                combo_box.addItem(key, value)
