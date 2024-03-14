from qt_core import *
# IMPORT WIDGETS
from view.widgets.dialogs.py_add_user_dialog import AddUserWindow
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.users_repository import UsersRepository
# IMPORTS VALIDATOR
from email_validator import validate_email, EmailNotValidError
from pymongo.errors import DuplicateKeyError

class TableUsersManager:
    def __init__(self, table, table_page) -> None:
        self.table = table
        self.table_page = table_page
        
        # DB_VARIABLES
        self.__db_handle = DBConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__users_repository = UsersRepository(self.__db_connection)
        
        # Buttons
        self.table_page.button_add_user.clicked.connect(self.add_user)
        
        self.table_init()
        
    def table_init(self):
        list_news = self.__users_repository.select_many_users()
        itens = len(list_news)
        self.table.setRowCount(itens)
        for row, text in enumerate(list_news):
            for column, label in enumerate(text):
                if label == "role":
                    if text[label] == 0:
                        item = QTableWidgetItem(str("Standard"))
                    else:
                        item = QTableWidgetItem(str("Admin"))
                else:
                    item = QTableWidgetItem(str(text[label]))
                    
                item.setTextAlignment(Qt.AlignCenter)
                item = self.table.setItem(row, column, item)

        self.table.resizeColumnsToContents()
        
# ---------------------------- Add Users ------------------------------------        
    def add_user(self):
        add_user = AddUserWindow()
        # Variables
        email = add_user.edit_email
        edit_pass = add_user.edit_pass
        pass_confirm = add_user.edit_pass_confirm
        btn_show = add_user.btn_show_password
        # Veficação
        btn_show.clicked.connect(lambda: self.toggle_password_visibility(btn_show, edit_pass))
        email.editingFinished.connect(lambda: self.mensage_email(email))
        pass_confirm.editingFinished.connect(lambda: self.password_equal(edit_pass, pass_confirm))
        # Conexão
        add_user.btn_cancel.clicked.connect(add_user.close)
        add_user.btn_register.clicked.connect(lambda: self.register_user(add_user))
        add_user.exec()
        
    def mensage_email(self, email):
        email_txt = str(email.text())
        try:
            validate_email(email_txt)
            pass
        except EmailNotValidError as e:
            dlg = WarningMessageBox(title="Invalid", txt="Invalid email format!")
            dlg.exec()
            
    def toggle_password_visibility(self, btn_show, edit_pass):
        if btn_show.isChecked():
            edit_pass.setEchoMode(QLineEdit.Normal)
            btn_show.setIcon(QIcon("resources/images/icons/eyes_close.svg"))
        else:
            edit_pass.setEchoMode(QLineEdit.Password)
            btn_show.setIcon(QIcon("resources/images/icons/eyes_open.svg"))
            
    def password_equal(self, password, pass_confirm):
        if password.text() != pass_confirm.text():
            dlg = WarningMessageBox(title="Attention!", txt="Password confirmation failed!")
            dlg.exec() 
        else:
            pass
    
    def register_user(self, user_form):
        first_name = user_form.edit_fisrt_name.text()
        last_name = user_form.edit_last_name.text()
        email = user_form.edit_email.text()
        password = user_form.edit_pass.text()
        role = user_form.combo_role.currentIndex()
        if self.__users_repository.insert_user(first_name=first_name, last_name=last_name, email=email, password=password, role=role):
            dlg = WarningMessageBox(title="Congratulations!", txt="Account created!")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            user_form.close()
            self.table.clearContents()
            self.table_init() 
        else:
            dlg = WarningMessageBox(title="Attention!", txt="Email already in use!")
            dlg.exec() 