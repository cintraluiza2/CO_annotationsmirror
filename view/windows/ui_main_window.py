from qt_core import *

# Main Window
class UiMainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INITIAL PARAMETERS
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #E5E5E5")
        
        # -------------------------------------------------------------------- Itens
        
        # ------------------------ LEFT MENU ------------------------
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #1B4269;")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        
        # Top Frame Menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setStyleSheet("background-color: red")
        
        # Top Buttons
        self.togle_button_menu = QPushButton("Menu")
        
        # Menu Spacer
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Bottom Frame Menu
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setStyleSheet("background-color: red")
        
        # Label Version
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #E5E5E5")
        
        # ------------------------ CONTENT ------------------------
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #E5E5E5")
        
        # ------------------------ TOP BAR ------------------------
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(50)
        self.top_bar.setMaximumHeight(50)
        self.top_bar.setStyleSheet("background-color: #FFFFFF; color: #AAB2C8")
        
        # Left Label Logo
        self.top_label_left = QLabel()
        self.logo = QPixmap("resources/images/logo.svg")
        self.top_label_left.setPixmap(self.logo)
        
        # Top spacer
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # Right Label User
        self.top_label_right = QLabel()
        self.icon_user = QPixmap("resources/images/user_small.svg")
        self.top_label_right.setPixmap(self.icon_user)
        
        # ------------------------ PAGES ------------------------
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-family: Roboto; font-size: 12pt; background-color: #FFFFFF")
        
        # -------------------------------------------------------------------- LAYOUTS
        # Layoyt Main Window
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Layout Left Menu
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Top Frame Layout
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)
        
        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        
        # Layout Top Bar
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(20, 0, 53, 0)
    
        # -------------------------------------------------------------------- Widgets
        # Add widgets app
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # Add Widgest Left Menu
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        
        # Add widgets content 
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        
        # Add to top bar
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # --------- SET CENTRAL WIDGET ------------
        parent.setCentralWidget(self.central_frame)