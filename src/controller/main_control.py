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

from controller.pages.table_news import TableNewsManager
from controller.pages.classification_page import ClassificationManager


# ----------------------------Main Window--------------------------

class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        # Setup Main Window
        self.setup_ui(self)
        
        # VARIABLES GLOBAL
        self.title_list = []
        self.title_news = ""
        self.toggle_order = Qt.DescendingOrder
        
        # CLASSIFICATION
        self.classification_maneger = ClassificationManager(self.ui_pages, self.show_page_home)
        
        # TABLE PAGE
        self.table_page = self.ui_pages
        self.table_news_manager = TableNewsManager(self.table_page.table_news, self.table_page, self.show_page_class, self.classification_maneger.set_text_class, self.classification_maneger.set_title_list)
                
        # Toggle Button
        self.toggle_button_menu.clicked.connect(self.toggle_button)
        
        # BUTTON HOME / TABLE
        self.button_home.clicked.connect(self.show_page_home)
        
        # BUTTON CLASSIFICATION
        # self.ui.button_class.clicked.connect(self.show_page_table_class)
        
        # BUTTON EXIT
        self.button_exit.clicked.connect(self.show_dialog_exit)

        self.show()

# ---------------------------------------------------------------------------------------- Methods
    def reset_selection(self):
        for button in self.left_menu.findChildren(QPushButton):
            try:
                button.set_active(False)
            except:
                pass
            
    # BUTTONS ACTIONS
    def toggle_button(self):
        # Get Menu Width
        menu_width = self.left_menu.width()

        # Check Width
        width = 50
        if menu_width == 50:
            width = 160

        # Start Animation
        self.animation = QPropertyAnimation(self.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InQuint)
        self.animation.start()
        
    
    def show_page_home(self):
        self.reset_selection()
        self.button_home.set_active(True)
        
        self.pages.setCurrentIndex(0)
        
    def show_page_table_class(self):
        self.reset_selection()
        self.button_class.set_active(True)
        self.table_news_manager.populate_table_news()
        
        self.pages.setCurrentIndex(0)
    
    def show_page_class(self):
        self.reset_selection()
        self.button_class.set_active(True)
        
        self.pages.setCurrentIndex(1)
        
    def show_dialog_exit(self):        
        dlg = WarningMessageBoxOption(title="Attention!", txt="Do you want to close the app?")
        
        if dlg.exec_() == QMessageBox.Yes:
            self.close()
        
# ---------------------------------------------------------------------------------- TABLE CONTROL
                
# ------------------------------------------------------------------------------------------- CLASSIFICATION CONTROL              