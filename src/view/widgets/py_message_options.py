from qt_core import *

class WarningMessageBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        
        self.resize(200, 140)
        self.setStyleSheet("font-size: 20; color: black; background-color: #F1F1F1")
        self.setWindowTitle(title)
        self.setText(text)
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        