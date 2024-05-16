# ----------------------------Imports--------------------------
# Import QT Core
from qt_core import *
import sys
import requests
# Import Windows
from view.windows.ui_main_window import UiMainWindow
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
from view.widgets.dialogs.py_progress_data_base import UiProgressDataBase
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
        self.table_news_manager.populate_table_news()
        # if self.progress == 100:
        # else:
        #     sys.exit(self.close())

# ---------------------------------------------------------------------------------------- Methods        
    def erro_connect(self):
            try:
                # Tente fazer uma solicitação GET para um site conhecido para verificar rede
                requests.get("http://www.google.com", timeout=5)
                dlg = WarningMessageBox("Atenção", "Sem acesso ao banco de dados. Tente novamente mais tarde!\nSe o erro persistir, entre em contato com o suporte!")
            except requests.ConnectionError:
                dlg = WarningMessageBox("Atenção", "Sem acesso à rede!\nVerifique sua conexão com a internet.")
            dlg.exec()
            sys.exit(self.close())    
            
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
        dlg = WarningMessageBoxOption(title="Atenção!", txt="Gostaria de fechar o aplicativo?")
        
        if dlg.exec_() == QMessageBox.Yes:
            self.close() 
        
# ---------------------------------------------------------------------------------- TABLE CONTROL
                
# ------------------------------------------------------------------------------------------- CLASSIFICATION CONTROL              