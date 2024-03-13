# Import QT Core
from qt_core import *
# IMPORTS WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS VIEWS
from view.windows.ui_login_window import UiLoginWindow
# Imports CONTROLLER
from controller.main_control import MainWindow
# IMPORTS VALIDATORS
from email_validator import validate_email, EmailNotValidError
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
from models.repository.users_repository import UsersRepository

# ----------------------------Login Window--------------------------

class LoginWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()
        
        # DB Variables
        self.__db_handle = DBConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__users_repository = UsersRepository(self.__db_connection)
        
        # Setup Login Window
        self.ui = UiLoginWindow()
        self.ui.setup_ui(self)
        
        # Check Username and Password
        self.ui.butons_access.clicked.connect(self.access_permission)
        
        self.show()
        
    def access_permission(self):
        # DATABASE CHECK
        user_email = self.ui.txt_user.text()
        txt_pass = self.ui.txt_pass_word.text()
        
        try:
            validate_email(user_email)
            result = self.__users_repository.select_one_user(user_email, txt_pass)
            print(result)
            if result is None:
                dlg = WarningMessageBox(title="Error", txt="Incorrect email or password")
                dlg.exec()
            else:
                self.win = MainWindow()
                self.win.show()
                self.close() 
                
        except EmailNotValidError:
            dlg = WarningMessageBox(title="Error", txt="Invalid Email")
            dlg.exec()