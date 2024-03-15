from qt_core import *
# IMPORT WIDGETS
from view.widgets.dialogs.py_add_user_dialog import AddUserWindow
from view.widgets.dialogs.py_edit_user_dialog import EditUserWindow
from view.widgets.dialogs.py_edit_password import EditPasswordWindow
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.users_repository import UsersRepository
# IMPORTS VALIDATOR
from email_validator import validate_email, EmailNotValidError
import bcrypt
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
        self.table_page.button_edit_user.clicked.connect(self.edit_user_gui)
        
        # VARIABLES
        self.num_columns = 5
        self.user_registre = {}
        self.password = ""
        self.password_edit = False
        
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
        btn_show.clicked.connect(lambda: self.toggle_password_visibility(btn_show, edit_pass, pass_confirm))
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
            
    def toggle_password_visibility(self, btn_show, edit_pass, edit_pass_confirm):
        if btn_show.isChecked():
            edit_pass.setEchoMode(QLineEdit.Normal)
            edit_pass_confirm.setEchoMode(QLineEdit.Normal)
            btn_show.setIcon(QIcon("resources/images/icons/eyes_close.svg"))
        else:
            edit_pass.setEchoMode(QLineEdit.Password)
            edit_pass_confirm.setEchoMode(QLineEdit.Password)
            btn_show.setIcon(QIcon("resources/images/icons/eyes_open.svg"))
            
    def password_equal(self, password, pass_confirm):
        if password.text() != pass_confirm.text():
            dlg = WarningMessageBox(title="Attention!", txt="Password confirmation failed!")
            password.clear()
            pass_confirm.clear()
            dlg.exec() 
            return False
        else:
            return True
    
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
            
# ---------------------------- Edit User ------------------------------------        
    def edit_user_gui(self):
        selected_items = self.table.selectedItems()
        if selected_items:
            self.user_registre.clear() # Init User Registre
            password = ""
            
            row = selected_items[0].row()
            column_email = self.table.item(row, 1)
            email = column_email.text()
            
            # --------------------- DataBase
            self.user_registre = self.__users_repository.select_one_user(email) # - Registre DataBase
            form_user = EditUserWindow() # ---------------------------------------- Window Dialog User
            # ------------------- Form Edit
            form_user.edit_fisrt_name.setText(self.user_registre['first_name'])
            form_user.edit_fisrt_name.textChanged.connect(lambda text: self.edit_registre(text, 'first_name'))
            
            form_user.edit_last_name.setText(self.user_registre['last_name'])
            form_user.edit_last_name.textChanged.connect(lambda text: self.edit_registre(text, 'last_name'))
            
            form_user.edit_email.setText(self.user_registre['email'])
            form_user.edit_email.textChanged.connect(lambda text: self.edit_registre(text, 'email'))
            # ComboBox
            form_user.combo_role.setCurrentIndex(self.user_registre['role'])
            form_user.combo_role.currentIndexChanged.connect(lambda option: self.edit_registre(int(option), 'role'))
            # PASSWORD EDIT
            form_user.btn_edit_password.clicked.connect(self.edit_password)
            
            #---------------------------- Buttons
            form_user.btn_register.clicked.connect(lambda: self.registre_edit(form_user))
            form_user.btn_delete_user.clicked.connect(lambda: self.delete_user(form_user))
            form_user.btn_cancel.clicked.connect(form_user.close)
            
            form_user.exec() 
            
        else:
            dlg = WarningMessageBox(title="Information!", txt="Please! Select a user before editing")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec() 
            
    def edit_registre(self, text, label):
        self.user_registre[label] = text
        
    def edit_password(self):
        dialog_pass = EditPasswordWindow()
        btn_show = dialog_pass.btn_show_password
        edit_pass = dialog_pass.edit_pass
        edit_pass_confirm = dialog_pass.edit_pass_confirm
        btn_show.clicked.connect(lambda: self.toggle_password_visibility(btn_show, edit_pass, edit_pass_confirm))
        dialog_pass.btn_register.clicked.connect(lambda: self.registre_new_password(dialog_pass))
        dialog_pass.btn_cancel.clicked.connect(dialog_pass.close)
        dialog_pass.exec()

    def registre_new_password(self, dialog_pass):
        password = dialog_pass.edit_pass
        pass_confirm = dialog_pass.edit_pass_confirm
        if self.password_equal(password, pass_confirm):
            dlg = WarningMessageBoxOption(title="Information!", txt="This action cannot be undone. Click \"Yes\" to proceed with changing your password:")
            dlg.setIcon(QMessageBox.Information)
            if dlg.exec_() == QMessageBox.Yes:
                password_txt = dialog_pass.edit_pass_confirm.text()
                self.__users_repository.edit_registry_password(self.user_registre['email'], password_txt)
                dialog_pass.close()
        else:
            return
            
    def registre_edit(self, edit_form):
        dlg = WarningMessageBoxOption(title="Information!", txt="This action cannot be undone. Please confirm your choice:")
        dlg.setIcon(QMessageBox.Information)
        if dlg.exec_() == QMessageBox.Yes:
            first_name = self.user_registre['first_name']
            last_name = self.user_registre['last_name']
            email = self.user_registre['email']
            role = self.user_registre['role']
            
            self.__users_repository.edit_registry_user(email, first_name, last_name, role)
            
            edit_form.close()
            self.table.clearContents()
            self.table_init()
             
    def delete_user(self, edit_form):
        dlg = WarningMessageBoxOption(title="Information!", txt="Deleting this user will have permanent consequences. Are you sure you want to proceed?")
        dlg.setIcon(QMessageBox.Information)
        if dlg.exec_() == QMessageBox.Yes:
            self.__users_repository.delete_registry_user(self.user_registre['email'])
            edit_form.close()
            self.table.clearContents()
            self.table_init()