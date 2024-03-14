# ----------------------------Imports--------------------------
# Import QT Core
from qt_core import *
import random
# Import Windows
from view.windows.ui_host_window import UiHostWindow
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBoxOption, WarningMessageBox
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
from models.repository.users_repository import UsersRepository

from controller.pages.table_users import TableUsersManager
from controller.pages.table_news import TableNewsManager
from controller.pages.classification_page import ClassificationManager

# ----------------------------Main Window--------------------------

class HostWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Setup Main Window
        self.ui = UiHostWindow()
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
        
        # ---------------------------- TABLE USERS --------------------- 
        self.table_page = self.ui.table_users_page       
        self.table = self.table_page.table
        
        self.table_users_manager = TableUsersManager(self.table, self.table_page)
        
        self.table_page.button_edit_user.clicked.connect(self.edit_user)
        
        # --------------------------- CLASSIFICATION --------------------
        self.classification = self.ui.classification_page
        self.classification_maneger = ClassificationManager(self.classification, self.show_page_table_class)
        
        # --------------------------- TABLE PAGE -----------------------
        self.table_page = self.ui.table_news_page
        self.table = self.table_page.table
        self.table_news = TableNewsManager(self.table, self.table_page, self.show_page_class, self.classification_maneger.set_text_class, self.classification_maneger.set_title_list)
                
        # ---------------------------- MENU BAR BUTTONS ---------------------        
        # Toggle Button
        self.ui.toggle_button_menu.clicked.connect(self.toggle_button)
        
        # BUTTON HOME / TABLE
        self.ui.button_home.clicked.connect(self.show_page_table)
        
        # BUTTON CLASSIFICATION
        self.ui.button_class.clicked.connect(self.show_page_table_class)
        
        # BUTTON EXIT
        self.ui.button_exit.clicked.connect(self.show_dialog_exit)

        self.show()

# ---------------------------- Methods Menu ------------------------------------
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
    
        self.ui.pages.setCurrentIndex(0)
        
    def show_page_table_class(self):
        self.reset_selection()
        self.ui.button_class.set_active(True)
        
        self.ui.pages.setCurrentIndex(1)
    
    def show_page_class(self):
        self.reset_selection()
        self.ui.button_class.set_active(True)
        
        self.ui.pages.setCurrentIndex(2)
    
        
    def show_dialog_exit(self):        
        dlg = WarningMessageBoxOption(title="Attention!", txt="Do you want to close the app?")
        
        if dlg.exec_() == QMessageBox.Yes:
            self.close()
            
# ---------------------------- Methods Table Users ------------------------------------        
    def edit_user(self):
        print("ola")        
        
    