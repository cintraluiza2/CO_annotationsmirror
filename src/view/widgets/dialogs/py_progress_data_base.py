from PySide6.QtCore import QObject
from qt_core import *
from view.widgets.dialogs.progress_data_base import Ui_py_progress_data
import time

class LoaderServer(QThread):
    update_progress = Signal(int)

    def run(self):
        self.update_progress.emit(100)
            
class UiProgressDataBase(QDialog):
    def __init__(self, populate_table_news) -> None:
        super().__init__()
        self.populate_table_news = populate_table_news
        
        self.ui = Ui_py_progress_data()
        self.ui.setupUi(self)
        
        self.__loader_server = LoaderServer(self.populate_table_news)
        self.__loader_server.update_progress.connect(self.ui.set_progress)
        self.ui.progress_data_base.valueChanged.connect(self.close_load)
        
        self.exec() 
        
    def close_load(self, value):
        if value == 100:
            self.close()
        
        