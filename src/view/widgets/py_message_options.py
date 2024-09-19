from qt_core import *

class WarningMessageBoxOption(QMessageBox):
    """
        Classe para criar uma caixa de diálogo de aviso com botões 'Sim' e 'Cancelar'.

        Parâmetros:
        ----------
        title : str
            O título da janela da caixa de mensagem.
        txt : str
            O texto da mensagem que será exibido na caixa de diálogo.
    """
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
    """ 
        Classe para criar uma caixa de diálogo de aviso com botões 'Ok' e 'Cancelar'.

        Parâmetros:
        ----------
        title : str
            O título da janela da caixa de mensagem.
        txt : str
            O texto da mensagem que será exibido na caixa de diálogo.
    """
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
    """ 
        Classe para criar uma caixa de diálogo de aviso com um botão 'Ok'.

        Parâmetros:
        ----------
        title : str
            O título da janela da caixa de mensagem.
        txt : str
            O texto da mensagem que será exibido na caixa de diálogo.
    """
    def __init__(self, title, txt):
        super().__init__()
        
        self.setWindowIcon(QIcon('resources/images/icons/attention.svg'))
        self.resize(300, 140)
        self.setStyleSheet("font-size: 20; color: black; background-color: #F1F1F1")
        self.setWindowTitle(title)
        self.setText(txt)
        self.setIcon(QMessageBox.Warning)
        self.setStandardButtons(QMessageBox.Ok)
        