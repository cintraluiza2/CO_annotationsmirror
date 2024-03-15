from qt_core import *
from view.widgets.py_push_button import PyPushButtonGUI
from view.widgets.style_css import form_register_style

class EditPasswordWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Edit Registration')
        self.setWindowIcon(QIcon('resources/images/user_small.svg'))
        self.resize(400, 300)
        
        form_layout = QFormLayout()
        
        self.top_label_image = QLabel()
        self.icon_people = QPixmap("resources/images/password_forget.svg")
        self.top_label_image.setPixmap(self.icon_people)
        form_layout.addWidget(self.top_label_image)
        
        self.label_pass = QLabel('Enter New Password:')
        self.edit_pass = QLineEdit()
        self.edit_pass.setPlaceholderText("To change your password, enter a new one here")
        self.edit_pass.setEchoMode(QLineEdit.Password)
        self.btn_show_password = QPushButton()
        self.btn_show_password.setIcon(QIcon("resources/images/icons/eyes_open.svg"))
        self.btn_show_password.setCheckable(True)
        
        # FRAME PASS BUTTON
        self.frame_pass_button = QFrame()
        self.layout_pass_button = QHBoxLayout(self.frame_pass_button)
        self.layout_pass_button.setContentsMargins(0, 0, 0, 0)
        self.layout_pass_button.setSpacing(0)
        self.layout_pass_button.addWidget(self.edit_pass)
        self.layout_pass_button.addWidget(self.btn_show_password)
        form_layout.addRow(self.label_pass, self.frame_pass_button)
        
        self.label_pass_confirm = QLabel('Confirm password:')
        self.edit_pass_confirm = QLineEdit()
        self.edit_pass_confirm.setEchoMode(QLineEdit.Password)
        form_layout.addRow(self.label_pass_confirm, self.edit_pass_confirm)

        # Buttons Layout
        self.btn_frame = QFrame()
        self.btn_layout = QHBoxLayout(self.btn_frame)
        
        self.btn_register = PyPushButtonGUI(text='Edit', border_radius=20)
        self.btn_cancel = PyPushButtonGUI('Cancel', border_radius=20, btn_color="#D39854", btn_hover="#D4B955", btn_pressed="#D48255")
        
        self.btn_layout.addWidget(self.btn_register)
        self.btn_layout.addWidget(self.btn_cancel)
        form_layout.addWidget(self.btn_frame)
        
        self.setStyleSheet(form_register_style)
        
        self.setLayout(form_layout)
        