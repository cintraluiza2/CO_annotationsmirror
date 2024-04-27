from qt_core import *

class WarningMessageBoxOption(QMessageBox):
    def __init__(self, title, txt):
        super().__init__()
        
        self.setWindowIcon(QIcon('resources/images/icons/attention.svg'))
        self.resize(200, 140)
        self.setStyleSheet("font-size: 20; color: black; background-color: #F1F1F1")
        self.setWindowTitle(txt)
        self.setText(txt)
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        self.setButtonText(QMessageBox.Yes, "Sim")
        self.setButtonText(QMessageBox.Cancel, "Cancelar")
        
class WarningMessageBoxOptionOk(QMessageBox):
    def __init__(self, title, txt):
        super().__init__()
        
        self.setWindowIcon(QIcon('resources/images/icons/attention.svg'))
        self.resize(200, 140)
        self.setStyleSheet("font-size: 20; color: black; background-color: #F1F1F1")
        self.setWindowTitle(txt)
        self.setText(txt)
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.setButtonText(QMessageBox.Yes, "Sim")
        self.setButtonText(QMessageBox.Cancel, "Cancelar")
        
class WarningMessageBox(QMessageBox):
    def __init__(self, title, txt):
        super().__init__()
        
        self.setWindowIcon(QIcon('resources/images/icons/attention.svg'))
        self.resize(300, 140)
        self.setStyleSheet("font-size: 20; color: black; background-color: #F1F1F1")
        self.setWindowTitle(title)
        self.setText(txt)
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Ok)
        