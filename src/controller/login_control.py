# Import QT Core
from qt_core import *
import sys
# IMPORTS WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption, WarningMessageBoxOptionOk
# IMPORTS VIEWS
from view.windows.ui_login_window import Ui_Login
# Imports CONTROLLER
from controller.main_control import MainWindow
# IMPORTS VALIDATORS
from email_validator import validate_email, EmailNotValidError
import requests
import bcrypt
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
from models.repository.users_repository import UsersRepository

# ----------------------------Login Window--------------------------

class LoginWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()
        
        # Setup Login Window
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        
        # Check Username and Password
        self.ui.butons_access.clicked.connect(self.access_permission)
        
        self.show()
        
        # DB Variables
        self.__db_handle = DBConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__users_repository = UsersRepository(self.__db_connection)
        
    def access_permission(self):
        # DATABASE CHECK
        user_email = self.ui.txt_user.text()
        txt_pass = self.ui.txt_password.text()
        
        try:
            validate_email(user_email)
            response = self.__users_repository.select_user_pass(user_email)
            if not response:
                dlg = WarningMessageBox(title="Erro", txt="Senha ou Email Incorreto")
                dlg.exec()
            else:
                result = bcrypt.checkpw(txt_pass.encode("utf-8"), response["password"])
                if not result:
                    dlg = WarningMessageBox(title="Erro", txt="Senha ou Email Incorreto")
                    dlg.exec()
                else:
                    role = response["role"]
                    if role == 0:
                        self.win = MainWindow()
                    self.win.show()
                    self.close() 
                
        except EmailNotValidError:
            dlg = WarningMessageBox(title="Erro", txt="Email Inválido")
            dlg.exec()