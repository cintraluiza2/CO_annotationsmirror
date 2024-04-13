from qt_core import *
import os
# IMPORTS WIDGETS
from view.widgets.py_push_button import PyPushButtonGUI

class UiLoginWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("parent")
        
        # SET INITIAL PARAMETERS
        parent.setWindowTitle("Login - OrgaExtractor")
        parent.setWindowIcon(QIcon('resources/images/icons/icon_logo.svg'))
        parent.resize(700, 600)
        parent.setMaximumSize(700, 600)
        parent.setMinimumSize(700, 600)
        
        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("font-family: 'Roboto'; background-color: #FFFFFF")
        
        # ------------------ IMAGE LOGO --------------------
        self.image_logo = QLabel()
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "resources/images/logo_small.svg"
        path = os.path.join(app_path, folder)
        # Make PixMap
        pixmap = QPixmap(path)
        self.image_logo.setPixmap(pixmap)
        self.image_logo.resize(pixmap.width(), pixmap.height())
# ---------------------------------------------------------------------- ITENS/FRAMES
        # ------------------ FRAME LOGIN --------------------
        self.login_frame = QFrame()
        self.login_frame.setMaximumWidth(448)
        self.login_frame.setMaximumHeight(448)
        
        # ------------------ FRAME ICON --------------------
        self.frame_icon = QFrame()
        self.frame_icon.setMaximumWidth(448)
        self.frame_icon.setMaximumHeight(138)
        
        # ------------------ IMAGE ICON --------------------
        self.image_login = QLabel()
        # Format Path
        app_path = os.path.abspath(os.getcwd())
        folder = "resources/images/user_login.svg"
        path = os.path.join(app_path, folder)
        # Make PixMap
        pixmap = QPixmap(path)
        self.image_login.setPixmap(pixmap)
        self.image_login.resize(pixmap.width(), pixmap.height())
        
        # ------------------ FRAME INPUT --------------------
        self.frame_input = QFrame()
        self.frame_input.setStyleSheet("font-size: 14pt; color: black;")
        self.frame_input.setMaximumWidth(448)
        self.frame_input.setMaximumHeight(300)
        
        style_line_edit = """
            border-style: solid;  
            border-color: black; 
            border-radius: 20px;
            background-color: #CED2D6; 
            padding: 10px 10px 10px 15px;
            color: #524F4F
        """   
        
        # Create Frame User
        self.user_frame = QFrame()
        self.user_frame.setMaximumWidth(341)
        self.user_frame.setMaximumHeight(90)
        
        # Label User
        self.label_user = QLabel("Email")
        self.label_user.setAlignment(Qt.AlignLeft)
        
        # Create LineEdit User
        self.txt_user = QLineEdit()
        self.txt_user.setPlaceholderText("email@address.com")
        self.txt_user.setStyleSheet(style_line_edit)
        
        # Create Frame Pass
        self.pass_frame = QFrame()
        self.pass_frame.setMaximumWidth(341)
        self.pass_frame.setMaximumHeight(90)
        
        # Label Pass
        self.label_pass = QLabel("Password")
        self.label_pass.setAlignment(Qt.AlignLeft)
        
        # Create LineEdit PassWord
        self.txt_pass_word = QLineEdit()
        self.txt_pass_word.setEchoMode(QLineEdit.Password)
        self.txt_pass_word.show()
        self.txt_pass_word.setPlaceholderText("8-character passcode")
        self.txt_pass_word
        self.txt_pass_word.setStyleSheet(style_line_edit)
        
        # BUTTONS
        self.butons_access = PyPushButtonGUI(text="Access", font_family="Roboto", font_size=13, width=310, border_radius=20)
        
# ---------------------------------------------------------------------- Layouts
        # CREATE WINDOW LAYOUT
        self.window_layout = QVBoxLayout()
        # CREATE MAIN LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        # CREATE LOGIN LAYOUT
        self.login_layout = QVBoxLayout(self.login_frame)
        self.login_layout.setContentsMargins(0, 0, 0, 0)
        self.login_layout.setSpacing(44)
        
        # CREATE LAYOUT ICON
        self.icon_layout = QVBoxLayout(self.frame_icon)
        self.icon_layout.setContentsMargins(0, 0, 0, 0)
        self.icon_layout.setSpacing(0)
        
        # CREATE LAYOUT INPUT
        self.input_layout = QVBoxLayout(self.frame_input)
        self.input_layout.setContentsMargins(65, 0, 65, 0)
        
        # LAYOUT USER
        self.user_layout = QVBoxLayout(self.user_frame)
        
        # LAYOUT PASS
        self.pass_layout = QVBoxLayout(self.pass_frame)
        
# ---------------------------------------------------------------------- Widgets
        # IN LAYOUT WINDOW
        self.window_layout.addWidget(self.central_frame)
        # IN MAIN LAYOUT
        self.main_layout.addWidget(self.login_frame)
        
        # IN LOGIN LAYOUT
        self.login_layout.addWidget(self.frame_icon)
        self.login_layout.addWidget(self.frame_input)
        
        # IN ICON LAYOUT
        self.icon_layout.addWidget(self.image_login)
        
        # IN INPUT LAYOUT
        self.input_layout.addWidget(self.user_frame)
        self.input_layout.addWidget(self.pass_frame)
        self.input_layout.addSpacing(10)
        self.input_layout.addWidget(self.butons_access)
        
        # IN USER LAYOUT
        self.user_layout.addWidget(self.label_user)
        self.user_layout.addWidget(self.txt_user)
        # IN PASS LAYOUT
        self.pass_layout.addWidget(self.label_pass)
        self.pass_layout.addWidget(self.txt_pass_word)
        
        # --------- SET CENTRAL WIDGET ------------
        parent.setLayout(self.window_layout)
        