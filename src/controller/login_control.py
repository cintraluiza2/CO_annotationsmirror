# IMPORT BASIC
from validate_docbr import CPF
# Import QT Core
from qt_core import *
# IMPORTS WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS VIEWS
from view.windows.ui_login_window import UiLoginWindow
# Imports CONTROLLER
from controller.db_control_connection import DBControlConnections
from controller.main_control import MainWindow

# ----------------------------Login Window--------------------------

class LoginWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()
        
        # DB CONTROL
        self.__db_control = DBControlConnections()
        
        # Setup Login Window
        self.ui = UiLoginWindow()
        self.ui.setup_ui(self)
        self.setWindowTitle("Login - QTSorting Hat")
        
        # Check Username and Password
        self.ui.butons_access.clicked.connect(self.access_permission)
        
        self.show()
        
    def access_permission(self):
        # DATABASE CHECK
        txt_user = self.ui.txt_user.text()
        txt_pass = self.ui.txt_pass_word.text()
        cpf = CPF()
        
        if cpf.validate(txt_user) or txt_user == "123.123.123-12":
            result = self.__db_control.users_check_password(txt_user, txt_pass)
        
            if result[0]:
                self.win = MainWindow()
                self.win.show()
                self.close() 
            else:
                dlg = WarningMessageBox(title="Error", txt="Invalid username or password")
                dlg.exec()
        else:
            dlg = WarningMessageBox(title="Error", txt="Invalid CPF. Please check the number.")
            dlg.exec()
            