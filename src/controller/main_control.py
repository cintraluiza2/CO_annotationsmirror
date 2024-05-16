# ----------------------------Imports--------------------------
# Import QT Core
from qt_core import *
import sys
import random
# Import Windows
from view.windows.ui_main_window import UiMainWindow
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
from view.widgets.dialogs.py_progress_data_base import UiProgressDataBase
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
from models.repository.users_repository import UsersRepository
from config import server_configs
from sshtunnel import open_tunnel, BaseSSHTunnelForwarderError

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

        dlg = UiProgressDataBase(self.table_news_manager.populate_table_news, self.__connect_server)
        self.progress = dlg.ui.progress_data_base.value()
        if self.progress == 100:
            self.show()
        else:
            sys.exit(self.close())

# ---------------------------------------------------------------------------------------- Methods
    def __connect_server(self):
            try:
                SSH_TIMEOUT = 15
                with open_tunnel(
                (server_configs['ip_server'], server_configs['port']),
                ssh_username=server_configs['username'],
                ssh_password=server_configs['password'],
                local_bind_address=(server_configs['local_address'], server_configs['local_port_ssh']),
                remote_bind_address=(server_configs['remote_address'], server_configs['remote_port_ssh'])
                ) as server:
                    self.server = server
            except:
                return False 
            
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