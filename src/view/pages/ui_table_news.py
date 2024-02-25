# Imports QT CORE
from qt_core import *
# IMPORTS WIDGETS
from view.widgets.py_push_button import PyPushButtonGUI
# IMPORT STYLE
from view.widgets.style_css import table_style

class UiTableNews(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("parent")
            
        # SET INITIAL PARAMETERS
        parent.resize(800, 600)
        
        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("font-family: 'Roboto'; color: black; background-color: #FFFFFF")
        
# -------------------------------------------------------------------- ITENS/FRAMES
        # LABEL
        self.title_page_news = QLabel("News")
        self.title_page_news.setStyleSheet("font: 25px")
        
        #--------------------------- TABLE -------------------
        self.table = QTableWidget()
        self.table.setMinimumWidth(600)
        self.table.setMaximumWidth(1230)
        self.table.setMaximumHeight(600)
        # Size Table
        self.table.setRowCount(50)
        self.table.setColumnCount(6)
        
        # Define o modo de redimensionamento de todas as colunas para Qt.Fixed
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)  # Seleção de linha inteira
        self.table.setSelectionMode(QTableWidget.MultiSelection)  # Seleção de várias linhas
        # Definição do Header
        self.table.setHorizontalHeaderLabels(["Publication", "News", "Title", "Human", "Machine", "Level"])
        # Impede a edição de todas as células da tabela
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Oculta as linhas de divisão de coluna e linha
        self.table.setShowGrid(False)
        self.table.verticalHeader().setVisible(False)
        
        # Style
        self.table.setStyleSheet(table_style)
        self.table.verticalHeader().setDefaultSectionSize(35)
        
        # --------------------- BUTTONS --------------------------
        # Frame Button
        self.frame_buttons = QFrame()
        self.frame_buttons.setMinimumHeight(50)
        self.frame_buttons.setMaximumHeight(50)
        # self.frame_buttons.spacing(130)
        # Buttons
        self.button_note = PyPushButtonGUI(text="Note", btn_color="#77966D", btn_hover="#6E9673", btn_pressed="#89966E", border_radius=20, width=187, font_size=13, font_family="Roboto")
        self.button_unselect = PyPushButtonGUI(text="Unselect", btn_color="#D39854", btn_hover="#D4AA55", btn_pressed="#D48255", border_radius=20, width=187, font_size=13, font_family="Roboto")
        self.button_train = PyPushButtonGUI(text="Train", btn_color="#1B5A69", btn_hover="#1B4269", btn_pressed="#1B695E", border_radius=20, width=187, font_size=13, font_family="Roboto")
        
# -------------------------------------------------------------------- LAYOUTS
        # MAIN LAYOUT
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(15, 10, 15, 15)
        self.main_layout.setSpacing(15)
        # BUTTONS LAYOUT
        self.buttons_layout = QHBoxLayout(self.frame_buttons)
        
# -------------------------------------------------------------------- WIDGETS
        # IN MAIN LAYOUT
        self.main_layout.addWidget(self.title_page_news)
        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.frame_buttons)
        # IN BUTTONS LAYOUT
        self.buttons_layout.addWidget(self.button_note)
        self.buttons_layout.addSpacing(120)
        self.buttons_layout.addWidget(self.button_unselect)
        self.buttons_layout.addSpacing(120)
        self.buttons_layout.addWidget(self.button_train)
        
        # --------- SET CENTRAL WIDGET ------------
        parent.addWidget(self.central_frame)
