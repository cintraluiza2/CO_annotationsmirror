# Imports QT CORE
from qt_core import *
# IMPORTS WIDGETS
from view.widgets.py_push_button import PyPushButtonGUI, PyPushButtonIcon
# IMPORT STYLE
from view.widgets.style_css import table_style

class UiTableUsers(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("parent")
            
        # SET INITIAL PARAMETERS
        parent.resize(800, 600)
        
        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("font-family: 'Roboto'; color: black; background-color: #FFFFFF")
        
# -------------------------------------------------------------------- ITENS/FRAMES
        self.header_frame = QFrame()
        # LABEL
        self.title_page_news = QLabel("Users")
        self.title_page_news.setStyleSheet("font: 25px")
        self.button_prev = PyPushButtonIcon(icon_path="arrow_left.svg", btn_color="transparent", btn_hover="#E5E5E5", btn_pressed="transparent", icon_color="#374957")
        self.button_prev.setMaximumWidth(50)
        self.button_next = PyPushButtonIcon(icon_path="arrow_right.svg", btn_color="transparent", btn_hover="#E5E5E5", btn_pressed="transparent", icon_color="#374957")
        self.button_next.setMaximumWidth(50)
        
        #--------------------------- TABLE -------------------
        self.frame_table = QFrame()
        self.table = QTableWidget()
        self.table.setMaximumWidth(600)
        self.table.setMaximumHeight(600)
        # Size Table
        self.table.setRowCount(10)
        self.table.setColumnCount(5)
        
        # Define o modo de redimensionamento de todas as colunas para Qt.Fixed
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)  # Seleção de linha inteira
        # Definição do Header
        self.table.setHorizontalHeaderLabels(["Name", "Email", "User Role", "News articles analyzed", "Notes"])
        # Impede a edição de todas as células da tabela
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Oculta as linhas de divisão de coluna e linha
        self.table.setShowGrid(False)
        self.table.verticalHeader().setVisible(False)
        
        # Redimensionamento das Colunas
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        
        # Style
        self.table.setStyleSheet(table_style)
        self.table.verticalHeader().setDefaultSectionSize(40)
        
        #--------------------------- PANEL INFORMATION -------------------
        self.panel_frame = QFrame()
        
        # --------------------- BUTTONS --------------------------
        # Frame Button
        self.frame_buttons = QFrame()
        self.frame_buttons.setMinimumHeight(50)
        self.frame_buttons.setMaximumHeight(50)
        # self.frame_buttons.spacing(130)
        # Buttons
        self.button_view_user = PyPushButtonGUI(text="View User", btn_color="#77966D", btn_hover="#6E9673", btn_pressed="#89966E", border_radius=20, width=187, font_size=13, font_family="Roboto")
        self.button_add_user = PyPushButtonGUI(text="Add User", btn_color="#D39854", btn_hover="#D4AA55", btn_pressed="#D48255", border_radius=20, width=187, font_size=13, font_family="Roboto")
        self.button_edit_user = PyPushButtonGUI(text="Edit User", btn_color="#1B5A69", btn_hover="#1B4269", btn_pressed="#1B695E", border_radius=20, width=187, font_size=13, font_family="Roboto")
        
# -------------------------------------------------------------------- LAYOUTS
        # MAIN LAYOUT
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(15, 10, 15, 15)
        self.main_layout.setSpacing(15)
        # HEADER LAYOUT
        self.header_layout = QHBoxLayout(self.header_frame)
        # Table Layout
        self.table_layout = QHBoxLayout(self.frame_table)
        # Panel Layout
        self.panel_layout = QVBoxLayout(self.panel_frame)
        # BUTTONS LAYOUT
        self.buttons_layout = QHBoxLayout(self.frame_buttons)
        
# -------------------------------------------------------------------- WIDGETS
        # IN MAIN LAYOUT
        self.main_layout.addWidget(self.header_frame)
        self.main_layout.addWidget(self.frame_table)
        self.main_layout.addWidget(self.frame_buttons)
        # IN HEADER LAYOUT
        self.header_layout.addWidget(self.title_page_news)
        # self.header_layout.addWidget(self.button_prev)
        # self.header_layout.addWidget(self.button_next)
        # self.header_layout.addSpacing(50)
        # IN FRAME TABLE
        self.table_layout.addWidget(self.table)
        self.table_layout.addWidget(self.panel_frame)
        # IN BUTTONS LAYOUT
        self.buttons_layout.addWidget(self.button_view_user)
        self.buttons_layout.addSpacing(120)
        self.buttons_layout.addWidget(self.button_add_user)
        self.buttons_layout.addSpacing(120)
        self.buttons_layout.addWidget(self.button_edit_user)
        
        # --------- SET CENTRAL WIDGET ------------
        parent.addWidget(self.central_frame)
