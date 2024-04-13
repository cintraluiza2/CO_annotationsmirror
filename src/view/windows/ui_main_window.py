from qt_core import *
# IMPORT WIDGETS
from view.widgets.py_push_button import PyPushButtonIcon
#IMPORT PAGES
from view.pages.ui_classification import UiClassification
from view.pages.ui_table_news import UiTableNews

# Main Window
class UiMainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INITIAL PARAMETERS
        parent.setWindowTitle('OrgaExtractor')
        parent.setWindowIcon(QIcon('resources/images/icons/icon_logo.svg'))
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("font-family: 'Roboto'; color: black; background-color: #E5E5E5")
        
# ---------------------------------------------------------------------- ITENS/FRAMES
        # ------------------------ LEFT MENU ------------------------
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #1B4269;")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        
        # Top Frame Menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        # Top Buttons
        self.toggle_button_menu = PyPushButtonIcon("Menu", icon_path="burger.svg")
        
        # Button Spacer
        self.button_space = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Central Frame Menu
        self.left_menu_central_frame = QFrame()
        self.left_menu_central_frame.setMinimumHeight(50)
        # Central Buttons
        self.button_home = PyPushButtonIcon("Home", is_active=True, icon_path="home.svg")
        self.button_class = PyPushButtonIcon("Classification", icon_path="class.svg")
        self.button_extra = PyPushButtonIcon("Extraction", icon_path="extraction.svg")
        self.button_data = PyPushButtonIcon("Data", icon_path="data.svg")
        
        # Menu Spacer
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Bottom Frame Menu
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        
        # Bottom Buttons
        self.button_exit = PyPushButtonIcon("Exit", icon_path="exit.svg")
        
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
        # TABLE NEWS PAGE
        
        # CLASSIFICATION PAGE
        self.classification_page = UiClassification()
        self.classification_page.setup_ui(self.pages)
        self.table_news_page = UiTableNews()
        self.table_news_page.setup_ui(self.pages)
        
# -------------------------------------------------------------------- LAYOUTS
        # Layoyt Main Window
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Layout Left Menu
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Top Frame Layout Menu
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)
        
        # Central Frame Layout Menu
        self.left_menu_central_layout = QVBoxLayout(self.left_menu_central_frame)
        self.left_menu_central_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_central_layout.setSpacing(20)
        
        # Bottom Frame Layout Menu
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)
        
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
        self.left_menu_layout.addItem(self.button_space)
        self.left_menu_layout.addWidget(self.left_menu_central_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        
        # Add Buttons Menu
        self.left_menu_top_layout.addWidget(self.toggle_button_menu)
        self.left_menu_central_layout.addWidget(self.button_home)
        self.left_menu_central_layout.addWidget(self.button_class)
        self.left_menu_central_layout.addWidget(self.button_extra)
        self.left_menu_central_layout.addWidget(self.button_data)
        self.left_menu_bottom_layout.addWidget(self.button_exit)
        
        # Add widgets content 
        # self.content_layout.addWidget(self.top_bar) Desativar o TopBar
        self.content_layout.addWidget(self.pages)
        
        # Add to top bar
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # --------- SET CENTRAL WIDGET ------------
        parent.setCentralWidget(self.central_frame)