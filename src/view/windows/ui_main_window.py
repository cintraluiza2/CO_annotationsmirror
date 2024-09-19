from qt_core import *
# IMPORT WIDGETS
from view.widgets.py_push_button import *
#IMPORT PAGES
from view.pages.ui_pages import Ui_Pages

# Main Window
class UiMainWindow(object):
    def setup_ui(self, parent):
        # Configurações iniciais da janela principal
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # Define o título da janela, ícone e tamanho mínimo
        parent.setWindowTitle('OCNewsAnnotator')
        parent.setWindowIcon(QIcon('resources/images/icons/icon_logo.svg'))
        parent.setMinimumSize(1000, 700)

        # Cria o widget central, define o estilo (cor de fundo e fonte)
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("font-family: 'Roboto'; color: black; background-color: #E5E5E5")
        
# ---------------------------------------------------------------------- ITENS/FRAMES
        # ------------------------ LEFT MENU ------------------------
        # Criação do menu lateral esquerdo com fundo azul escuro
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #1B4269;")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        
        # Frame superior do menu esquerdo
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        
        # Botão para alternar o menu (toggle)
        self.toggle_button_menu = PyPushButtonIcon("Menu", icon_path="burger.svg")
        
        # Espaçamento entre os botões
        self.button_space = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Frame central do menu esquerdo
        self.left_menu_central_frame = QFrame()
        self.left_menu_central_frame.setMinimumHeight(50)
        
        # Botões principais do menu: Home, Classificação, Extração e Dados
        self.button_home = PyPushButtonIcon("Home", is_active=True, icon_path="home.svg")
        self.button_class = PyPushButtonIcon("Classificação", icon_path="class.svg")
        self.button_extra = PyPushButtonIcon("Extração", icon_path="extraction.svg")
        self.button_data = PyPushButtonIcon("Dados", icon_path="data.svg")
        
        # Espaçamento para manter os botões organizados no menu
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Frame inferior do menu esquerdo
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        
        # Botão para sair do sistema
        self.button_exit = PyPushButtonIcon("Sair", icon_path="exit.svg")
        
        # Label para exibir a versão do sistema no menu lateral inferior
        self.left_menu_label_version = QLabel("v2.2.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #E5E5E5")
        
        # ------------------------ CONTENT ------------------------
        # Área principal de conteúdo à direita do menu
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #E5E5E5")
        
        # ------------------------ TOP BAR ------------------------
        # Barra superior da janela
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(50)
        self.top_bar.setMaximumHeight(50)
        self.top_bar.setStyleSheet("background-color: #FFFFFF; color: #AAB2C8")
        
        # Label do logo na barra superior
        self.top_label_left = QLabel()
        self.logo = QPixmap("resources/images/logo.svg")
        self.top_label_left.setPixmap(self.logo)
        
        # Espaçamento na barra superior (entre logo e usuário)
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # Label do ícone de usuário na barra superior
        self.top_label_right = QLabel()
        self.icon_user = QPixmap("resources/images/user_small.svg")
        self.top_label_right.setPixmap(self.icon_user)
        
        # ------------------------ PAGES ------------------------
        # Páginas principais (área de conteúdo que troca conforme seleção no menu)
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("background-color: #FFFFFF")
        self.ui_pages = Ui_Pages() 
        self.ui_pages.setupUi(self.pages)
        
        # CLASSIFICATION PAGE
        # Página de classificação (Comentado por enquanto)
        # self.classification_page = UiClassification()
        # self.classification_page.setup_ui(self.pages)
        
# -------------------------------------------------------------------- LAYOUTS
        # Layout principal da janela
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Layout do menu lateral esquerdo
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)

        # Layout do frame superior do menu esquerdo
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)
        
        # Layout do frame central do menu esquerdo
        self.left_menu_central_layout = QVBoxLayout(self.left_menu_central_frame)
        self.left_menu_central_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_central_layout.setSpacing(20)
        
        # Layout do frame inferior do menu esquerdo
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)
        
        # Layout do conteúdo principal à direita
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        
        # Layout da barra superior
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(20, 0, 53, 0)
    
# -------------------------------------------------------------------- Widgets
        # Adiciona os widgets à janela principal
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # Adiciona widgets ao menu lateral esquerdo
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.button_space)
        self.left_menu_layout.addWidget(self.left_menu_central_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        
        # Adiciona botões ao menu
        self.left_menu_top_layout.addWidget(self.toggle_button_menu)
        self.left_menu_central_layout.addWidget(self.button_home)
        self.left_menu_central_layout.addWidget(self.button_class)
        self.left_menu_central_layout.addWidget(self.button_extra)
        self.left_menu_central_layout.addWidget(self.button_data)
        self.left_menu_bottom_layout.addWidget(self.button_exit)
        
        # Adiciona widgets ao conteúdo principal (excluindo temporariamente a barra superior)
        # self.content_layout.addWidget(self.top_bar) Desativar o TopBar
        self.content_layout.addWidget(self.pages)
        
        # Adiciona elementos à barra superior (logo e ícone de usuário)
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # --------- Define o widget central ------------ 
        parent.setCentralWidget(self.central_frame)
