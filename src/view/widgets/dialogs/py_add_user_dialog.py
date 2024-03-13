from qt_core import *
from view.widgets.py_push_button import PyPushButtonGUI
from view.widgets.style_css import form_register_style

class AddUserWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('User Registration')
        self.setWindowIcon(QIcon('resources/images/user_small.svg'))
        self.resize(600, 500)
        
        form_layout = QFormLayout()
        
        self.top_label_image = QLabel()
        self.icon_people = QPixmap("resources/images/people.svg")
        self.top_label_image.setPixmap(self.icon_people)
        form_layout.addWidget(self.top_label_image)


        self.label_fisrt_name = QLabel('First Name:')
        self.edit_fisrt_name = QLineEdit()
        form_layout.addRow(self.label_fisrt_name, self.edit_fisrt_name)
        
        self.label_last_name = QLabel('Last Name:')
        self.edit_last_name = QLineEdit()
        form_layout.addRow(self.label_last_name, self.edit_last_name)

        self.label_email = QLabel('Email:')
        self.edit_email = QLineEdit()
        form_layout.addRow(self.label_email, self.edit_email)

        self.label_pass = QLabel('Enter Password:')
        self.edit_pass = QLineEdit()
        self.edit_pass.setEchoMode(QLineEdit.Password)
        form_layout.addRow(self.label_pass, self.edit_pass)
        
        self.label_pass_confirm = QLabel('Confirm password:')
        self.edit_pass_confirm = QLineEdit()
        self.edit_pass_confirm.setEchoMode(QLineEdit.Password)
        form_layout.addRow(self.label_pass_confirm, self.edit_pass_confirm)
        
        self.label_role = QLabel('User Role:')
        self.combo_role = QComboBox()
        self.combo_role.addItem('Standard User')
        self.combo_role.addItem('Administrator')
        form_layout.addRow(self.label_role, self.combo_role)

        # Buttons Layout
        self.btn_frame = QFrame()
        self.btn_layout = QHBoxLayout(self.btn_frame)
        
        self.btn_register = PyPushButtonGUI(text='Register', border_radius=20)
        self.btn_cancel = PyPushButtonGUI('Cancel', border_radius=20, btn_color="#941C2F", btn_hover="#692630", btn_pressed="#3F2125")
        # self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)
        
        self.btn_layout.addWidget(self.btn_register)
        self.btn_layout.addWidget(self.btn_cancel)
        form_layout.addWidget(self.btn_frame)
        
        self.setStyleSheet(form_register_style)
        
        self.setLayout(form_layout)
        