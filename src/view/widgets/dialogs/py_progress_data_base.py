from PySide6.QtCore import QObject
from qt_core import *
from view.widgets.dialogs.progress_data_base import Ui_py_progress_data
from config import server_configs
from sshtunnel import open_tunnel, SSH_TIMEOUT
import time

class LoaderServer(QThread):
    quit_signal = Signal()
    update_progress = Signal(int)
    
    def __init__(self, populate_table_news, connect_server) -> None:
        super().__init__()
        self.populate_table_news = populate_table_news
        self.connect_server = connect_server

    def run(self):
        if self.connect_server() == False:
            self.update_progress.emit(-1)
        else:
            self.update_progress.emit(50)
            time.sleep(1)
            if self.populate_table_news() == False:
                self.update_progress.emit(-2)
            else:
                self.update_progress.emit(100)
            
class UiProgressDataBase(QDialog):
    def __init__(self, populate_table_news, connect_server) -> None:
        super().__init__()
        self.populate_table_news = populate_table_news
        self.connect_server = connect_server
        
        self.ui = Ui_py_progress_data()
        self.ui.setupUi(self)
        
        self.__loader_server = LoaderServer(self.populate_table_news, self.connect_server)
        self.__loader_server.update_progress.connect(self.ui.set_progress)
        self.__loader_server.quit_signal.connect(self.__loader_server.quit)
        self.ui.progress_data_base.valueChanged.connect(self.close_load)
        
        self.__loader_server.start()
        self.exec() 
        
    def close_load(self, value):
        if value == 100:
            self.close()
            self.__loader_server.quit_signal.emit()
        
        