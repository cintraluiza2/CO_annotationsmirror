# Imports QT CORE
from qt_core import *

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
        self.table.setMaximumWidth(900)
        self.table.setMaximumHeight(600)
        # Size Table
        self.table.setRowCount(50)
        self.table.setColumnCount(5)
        self.table.setColumnWidth(0, 410)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 100)
        self.table.setColumnWidth(4, 150)
        
        # Define o modo de redimensionamento de todas as colunas para Qt.Fixed
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)  # Seleção de linha inteira
        self.table.setSelectionMode(QTableWidget.MultiSelection)  # Seleção de várias linhas
        # Definição do Header
        self.table.setHorizontalHeaderLabels(["Title", "Publication", "Class", "Newspaper", "Level"])
        # Impede a edição de todas as células da tabela
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Oculta as linhas de divisão de coluna e linha
        self.table.setShowGrid(False)
        
        # --------------------- BUTTONS --------------------------
        # Frame Button
        self.frame_buttons = QFrame()
        self.frame_buttons.setMinimumHeight(50)
        self.frame_buttons.setMaximumHeight(50)
        # Buttons
        self.button_note = QPushButton("Note")
        self.button_unselect = QPushButton("Unselect")
        self.button_train = QPushButton("Train")
        
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
        self.buttons_layout.addWidget(self.button_unselect)
        self.buttons_layout.addWidget(self.button_train)
        
        # --------- SET CENTRAL WIDGET ------------
        parent.addWidget(self.central_frame)
