from qt_core import *
from collections import deque
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
# IMPORTS NEWS RATING
# from models.news_rating.dataframe_fuctions import DataFrame
# from models.news_rating.doc_to_vector import DocToVector
# from models.news_rating.model_prediction import ModelPrediction

class TableNewsManager:
    def __init__(self, table=None, table_page=None, show_page_class=None, set_text_class=None, set_title_list=None) -> None:
        self.table = table
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
        self.num_columns = 5
        
        self.table_init()
        
        self.table.horizontalHeader().sectionClicked.connect(self.on_column_header_clicked) # Colunm Header Clicked
        self.table.cellDoubleClicked.connect(self.on_selection_table)
        self.table_page.button_note.clicked.connect(self.on_selection_table)
        # self.table_page.button_train.clicked.connect(self.train_table_news)
    
            
    def table_init(self):
        self.toggle_order = Qt.AscendingOrder
        list_news = self.__news_repository.select_many_order_news(optionsReturn={"_id": 0, "publication_date": 1, "newspaper": 1, "title": 1, "manual_relevance_class": 1, "automatic_relevance_class": 1, "certainty_level": 1}, orderFilter='manual_relevance_class', optionsFilter=1)
        mapping = {0: "Irrelevante", 1: "Relevante", None: "SClasse"}
        itens = len(list_news)
        self.table.setRowCount(itens)
        for row, dict_news in enumerate(list_news):
            dict_news["manual_relevance_class"] = mapping.get(dict_news["manual_relevance_class"])
            dict_news["automatic_relevance_class"] = mapping.get(dict_news["automatic_relevance_class"])
            for column, label in enumerate(dict_news):
                self.table.setItem(row, column, QTableWidgetItem(str(dict_news[label])))
    
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(2, 790)
        self.table.setColumnWidth(3, 100)
        
    def on_selection_table(self):
        selected_items = self.table.selectedItems() # O selectedItems seleciona cada celula
        num_selected = int(len(selected_items) / self.num_columns) # São 5 celulas por ser 5 colunas
        
        if num_selected == 0:
            dlg = WarningMessageBox(title="Atenção!", txt="A anotação requer a seleção de um artigo de notícias.")
            dlg.setIcon(QMessageBox.Warning)
            dlg.exec()
        else:
            title_selected = selected_items[2].text()
            for row in range(self.table.rowCount()):
                column_title = self.table.item(row, 2)
                self.title_list.append(column_title.text())
            
            self.table.clearSelection()
            title_selected_id = self.title_list.index(title_selected)
            self.set_title_list(self.title_list, title_selected_id)
            self.set_text_class()
            self.show_page_class()

    def on_column_header_clicked(self, logical_index): # Ordenação da Table
        
        if self.toggle_order == Qt.AscendingOrder:
            self.table.sortItems(logical_index, self.toggle_order)
            self.toggle_order = Qt.DescendingOrder
            
        else:
            self.table.sortItems(logical_index, self.toggle_order)
            self.toggle_order = Qt.AscendingOrder
            
    # def train_table_news(self):
    #     df = DataFrame()
    #     mp = ModelPrediction()
    #     dtv = DocToVector()

    #     df_news = df.make_data_frame()
    #     x, y = dtv.create_XY_vector(df_news, 40, 50)
    #     data_best_model = mp.cross_model(x, y, 20)

    #     name_model, best_model, confidence, standard_deviation = data_best_model
    #     best_model.fit(x, y)
    #     new_df = mp.automatic_relevance_class(df_news, name_model, best_model, x)
    #     automatic_list = new_df['automatic_relevance_class'].astype(int)
    #     self.table_init()
    #     num_rows = self.table.rowCount()
    #     for row in range(0, num_rows):
    #         self.table.setItem(row, 4, QTableWidgetItem(str(automatic_list[row])))