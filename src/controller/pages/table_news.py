from qt_core import *
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository

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
        self.toggle_order = Qt.DescendingOrder
        self.num_columns = 6
        
        self.table_init()
        
        self.table_page.button_unselect.clicked.connect(self.table.clearSelection)
        self.table.horizontalHeader().sectionClicked.connect(self.on_column_header_clicked) # Colunm Header Clicked
        self.table_page.button_note.clicked.connect(self.on_selection_table)
    
            
    def table_init(self):
        list_news = self.__news_repository.select_many_news(optionsReturn={"_id": 0, "publication_date": 1, "newspaper": 1, "title": 1, "manual_relevance_class": 1, "automatic_relevance_class": 1, "certainty_level": 1})
        itens = len(list_news)
        self.table.setRowCount(itens)
        for row, text in enumerate(list_news):
            for column, label in enumerate(text):
                self.table.setItem(row, column, QTableWidgetItem(str(text[label])))
    
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(2, 860)
        
    def on_selection_table(self):
        selected_items = self.table.selectedItems() # O selectedItems seleciona cada celula
        num_selected = int(len(selected_items) / self.num_columns) # São 5 celulas por ser 5 colunas
        
        if num_selected == 0:
            dlg = WarningMessageBoxOption(title="Question", txt="Would you like the system to select the news for you?")
            dlg.setIcon(QMessageBox.Question)
            dlg.exec()
        elif num_selected >= 5:
            for i in range(0, num_selected):               
                row = selected_items[i * self.num_columns].row() # Necessário multiplicar para acessar nova linha
                column_title = self.table.item(row, 2)
                self.title_list.append(column_title.text())
            
            self.table.clearSelection()
            self.set_title_list(self.title_list)
            self.set_text_class()
            self.show_page_class()
        else:
            dlg = WarningMessageBox(title="Information", txt="At least 5 news articles must be selected for the analysis.")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()

    def on_column_header_clicked(self, logical_index): # Ordenação da Table
        
        if self.toggle_order == Qt.AscendingOrder:
            self.table.sortItems(logical_index, self.toggle_order)
            self.toggle_order = Qt.DescendingOrder
            
        else:
            self.table.sortItems(logical_index, self.toggle_order)
            self.toggle_order = Qt.AscendingOrder