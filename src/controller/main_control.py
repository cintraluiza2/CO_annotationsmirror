# ----------------------------Imports--------------------------
# Import QT Core
from qt_core import *
import random
# Import Windows
from view.windows.ui_main_window import UiMainWindow
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
from models.repository.users_repository import UsersRepository


# ----------------------------Main Window--------------------------

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Setup Main Window
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        
        # DB_VARIABLES
        self.__db_handle = DBConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__news_repository = NewsClassRepository(self.__db_connection)
        self.__users_repository = UsersRepository(self.__db_connection)
        
        # VARIABLES GLOBAL
        self.title_list = []
        self.title_news = ""
        self.toggle_order = Qt.DescendingOrder
        
        # TABLE PAGE
        self.table = self.ui.table_news_page.table
        self.table_init()
        self.table_page = self.ui.table_news_page
        self.table_page.button_note.clicked.connect(self.on_selection_table)
        self.table_page.button_unselect.clicked.connect(self.table.clearSelection)
        self.table.horizontalHeader().sectionClicked.connect(self.on_column_header_clicked) # Colunm Header Clicked
        # CLASSIFICATION
        self.classification = self.ui.classification_page
        self.classification.button_accept.clicked.connect(self.accept_news)
        self.classification.button_rejected.clicked.connect(self.rejected_news)
        self.classification.button_back.clicked.connect(self.back_table_page)
                
        # Toggle Button
        self.ui.toggle_button_menu.clicked.connect(self.toggle_button)
        
        # BUTTON HOME / TABLE
        self.ui.button_home.clicked.connect(self.show_page_table)
        
        # BUTTON CLASSIFICATION
        # self.ui.button_class.clicked.connect(self.show_page_class)
        
        # BUTTON EXIT
        self.ui.button_exit.clicked.connect(self.show_dialog_exit)

        self.show()

# ---------------------------------------------------------------------------------------- Methods
    def reset_selection(self):
        for button in self.ui.left_menu.findChildren(QPushButton):
            try:
                button.set_active(False)
            except:
                pass
            
    # BUTTONS ACTIONS
    def toggle_button(self):
        # Get Menu Width
        menu_width = self.ui.left_menu.width()

        # Check Width
        width = 50
        if menu_width == 50:
            width = 160

        # Start Animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InQuint)
        self.animation.start()
        
    
    def show_page_table(self):
        self.reset_selection()
        self.ui.button_home.set_active(True)
        self.table_init()
        
        self.ui.pages.setCurrentIndex(0)
    
    def show_page_class(self):
        self.reset_selection()
        self.ui.button_class.set_active(True)
        
        self.ui.pages.setCurrentIndex(1)
        
    def show_dialog_exit(self):        
        dlg = WarningMessageBoxOption(title="Attention!", txt="Do you want to close the app?")
        
        if dlg.exec_() == QMessageBox.Yes:
            self.close()
        
# ---------------------------------------------------------------------------------- TABLE CONTROL
    def on_column_header_clicked(self, logical_index): # Ordenação da Table
        
        if self.toggle_order == Qt.AscendingOrder:
            self.table.sortItems(logical_index, self.toggle_order)
            self.toggle_order = Qt.DescendingOrder
            
        else:
            self.table.sortItems(logical_index, self.toggle_order)
            self.toggle_order = Qt.AscendingOrder
        
        
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
        num_selected = int(len(selected_items) / 5) # São 5 celulas por ser 5 colunas
        
        if num_selected == 0:
            dlg = WarningMessageBoxOption(title="Question", txt="Would you like the system to select the news for you?")
            dlg.setIcon(QMessageBox.Question)
            dlg.exec()
            
        elif num_selected >= 5:
            for i in range(0, num_selected):               
                row = selected_items[i * 5].row() # Necessário multiplicar por 5 para acessar nova linha
                column_title = self.table.item(row, 2)
                self.title_list.append(column_title.text())
            
            self.table.clearSelection()
            self.set_text_class()
            self.show_page_class()
        else:
            dlg = WarningMessageBox(title="Information", txt="At least 5 news articles must be selected for the analysis.")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
                
        
# ------------------------------------------------------------------------------------------- CLASSIFICATION CONTROL
        
    def set_text_class(self):
        title_news = self.title_list.pop()
        
        news = self.__news_repository.select_one_news(title={"$regex": title_news}, optionsReturn={"title": 1, "article": 1})
        text_news = news["article"]
        self.title_news = news["title"]
        self.classification.title_article.setText(title_news)
        self.classification.text_box_article.setText(text_news)
        
        if not self.title_list:
            dlg = WarningMessageBox(title="Information", txt="The news classification process has been completed.")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            self.show_page_table()
        
    
    def accept_news(self):
        edit = {"manual_relevance_class": 1}
        self.__news_repository.edit_registry_news(self.title_news, edit)
        self.db.edit_accept_news(self.id_news)
        self.set_text_class()
        
    def rejected_news(self):
        edit = {"manual_relevance_class": 0}
        self.__news_repository.edit_registry_news(self.title_news, edit)
        self.set_text_class()
        
    def back_table_page(self):
        dlg = WarningMessageBoxOption(title="Question", txt="Just to confirm, you would like to return?")
        dlg.setIcon(QMessageBox.Question)
        if dlg.exec_() == QMessageBox.Yes:
            self.title_list.clear()
            self.show_page_table()
        