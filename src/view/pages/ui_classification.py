from qt_core import *
# IMPORTS WIDGETS
from view.widgets.py_push_button import PyPushButtonGUI, PyPushButtonIcon, PyPushButtonGUIIcon
# IMPORTS STYLE
from view.widgets.style_css import text_box_class_style
# IMPORTS DATA
from models.utils.data import *
import random

class UiClassification(object):
        def setup_ui(self, parent):
                if not parent.objectName():
                        parent.setObjectName("parent")
                        parent.resize(800, 600)
                
                # SET INITIAL PARAMETERS
                self.central_frame = QFrame()
                self.central_frame.setStyleSheet("font-family: 'Roboto'; color: black; background-color: #FFFFFF")
        # ---------------------------------------------------------------------- ITENS/FRAMES
                # BOX
                self.box = QFrame()
                self.box.setMinimumWidth(500)
                self.box.setMaximumHeight(700)
                self.box.setStyleSheet(text_box_class_style)
                
                # TITLE ARTICLE
                self.title_article = QLabel("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ")
                self.title_article.setMargin(5)
                self.title_article.setMinimumHeight(25)
                self.title_article.setMaximumHeight(25)
                self.title_article.setMinimumWidth(600)
                self.title_article.setMaximumWidth(900)
                
                # Frame Infos
                self.frame_infos = QFrame()
                self.frame_infos.setMinimumHeight(25)
                self.frame_infos.setMaximumHeight(25)
                self.frame_infos.setMinimumWidth(600)
                self.frame_infos.setMaximumWidth(900)
                
                # ------------------------ Intens Infos
                self.label_publication = QLabel("Publicação:")
                self.label_publication.setStyleSheet("background-color: transparent; max-width: 4.6875em;")
                self.data_publication = QLabel("00-00-0000")
                
                self.label_update = QLabel("Atualização:")
                self.label_update.setStyleSheet("background-color: transparent; max-width: 5em;")
                self.data_update = QLabel("00-00-0000")
                
                self.label_machine_class = QLabel("Classe da Máquina:")
                self.label_machine_class.setStyleSheet("background-color: transparent")
                self.machine_class = QLabel("Relevante")
                self.machine_class.setStyleSheet("max-width: 4.6875em;")
                
                self.label_confidence= QLabel("Confiança:")
                self.label_confidence.setStyleSheet("background-color: transparent; max-width: 4.6875em;")
                self.confidence_machine = QLabel("00.00%")
                self.confidence_machine.setStyleSheet("max-width: 3.75em;")
                
                # TEXT ARTICLE
                self.text_box_article = QTextBrowser()
                
                # FRAME EXTRACTION
                self.frame_extraction = QFrame()
                self.frame_extraction.setMinimumHeight(310)
                self.frame_extraction.setMaximumHeight(310)
                
                # ---------------- Itens Frame Extraction
                # Radions Buttons
                self.groupBox = QGroupBox()
                self.groupBox.setStyleSheet("border: none")
                self.button_accept_news = QRadioButton("Relevante", self.groupBox)
                self.button_reject_news = QRadioButton("Irrelevante", self.groupBox)
                self.button_query = QRadioButton("Dúvida", self.groupBox)
                # Geographic Data
                self.frame_geo = QFrame()
                self.frame_geo.setStyleSheet("""QLabel {background-color: transparent; max-width: 8em}""")
                self.label_country = QLabel("País:") # Combo box País
                self.combo_country = QComboBox()
                self.combo_country.setStyleSheet("max-width: 4.72em")

                self.label_region = QLabel("Região:")
                self.combo_region = QComboBox()
                self.combo_region.setEnabled(False)

                self.label_state = QLabel("Estado")
                self.combo_state = QComboBox()
                self.combo_state.setEnabled(False)

                self.label_city = QLabel("Município:")
                self.combo_city = QComboBox()
                self.combo_city.setEnabled(False)

                self.label_date_event = QLabel("Data do Evento:")
                self.label_date_event.setStyleSheet("max-width: 6em")
                self.input_date_event = QDateEdit()
                self.input_date_event.setDisplayFormat("dd-MM-yyyy")
                # News data
                self.frame_news_data = QFrame()
                self.frame_news_data.setStyleSheet("""QLabel {background-color: transparent; max-width: 7em}""")
                self.label_deaths = QLabel("Quant. de Mortes:")
                self.input_deaths = QSpinBox()
                self.input_deaths.setMinimum(0)
                self.label_conflict = QLabel("Conflito Armado: ")
                self.combo_conflict = QComboBox()
                self.init_combo_box(self.combo_conflict, data_combo_conflict)
                self.label_type_narcotic = QLabel("Tipo de Droga:")
                self.combo_type_narcotic = QComboBox()
                self.init_combo_box(self.combo_type_narcotic, data_type_narcotic)
                self.label_qty_narcotic = QLabel("Quant. de Drogas:")
                self.input_qty_narcotic = QSpinBox()
                self.input_qty_narcotic.setMinimum(0)
                # Conflict Data
                self.frame_conflit_data = QFrame()
                self.frame_conflit_data.setStyleSheet("""QLabel {background-color: transparent; max-width: 9em}""")
                self.label_name_actor_1 = QLabel("Nome do Primeiro Ator:")
                self.name_actor_1 = QLineEdit()
                self.label_name_actor_2 = QLabel("Nome do Segundo Ator:")
                self.name_actor_2 = QLineEdit()
                self.label_latitude = QLabel("Latitude:")
                self.latitude = QLineEdit()
                # validator = QDoubleValidator(-90.0, 90.0, 2)
                # validator.top(90)
                # validator.bottom(-90) 
                # self.latitude.setValidator(validator)
                self.label_longitude = QLabel("Longitude:")
                self.longitude = QLineEdit()
                # Type Relation
                self.frame_type_relation = QFrame()
                self.frame_type_relation.setStyleSheet("""QLabel {background-color: transparent; max-width: 12em}""")
                self.label_type_relation = QLabel("Tipo de Relação Entre Atores:")
                self.combo_type_relation = QComboBox()
                self.init_combo_box(self.combo_type_relation, data_type_relation)
                
                # BUTTONS FRAME
                self.frame_buttons = QFrame()
                self.frame_buttons.setMinimumHeight(50)
                self.frame_buttons.setMaximumHeight(50)
                
                # BUTTONS TEXT
                self.button_back = PyPushButtonGUIIcon(width=200, border_radius=20, icon_path="arrow_return.svg", text="Anterior", btn_color="#1B4269", btn_hover="#1B5A69", btn_pressed="#3E5369", icon_color="white")
                self.button_finish = PyPushButtonGUI("Finalizar", width=200, border_radius=20, font_family="Roboto", font_size=13, btn_color="#77966D", btn_hover="#566C4F", btn_pressed="#3B4A36")
                self.button_cancel = PyPushButtonGUI("Cancelar", width=200, border_radius=20, font_family="Roboto", font_size=13, btn_color="#941C2F", btn_hover="#8B1A2B", btn_pressed="#470E16")
                self.button_next = PyPushButtonGUIIcon(width=200, minimum_width=320, border_radius=20, icon_path="arrow_next.svg", text="Próxima", btn_color="#1B4269", btn_hover="#1B5A69", btn_pressed="#3E5369", icon_color="white")
                        
        # -------------------------------------------------------------------- LAYOUTS
                # CREATE LAYOUT MAIN
                self.main_layout = QVBoxLayout(self.central_frame)
                self.main_layout.setContentsMargins(15, 10, 15, 15)
                self.main_layout.setSpacing(15)
                
                # BOX LAYOUT
                self.box_layout = QVBoxLayout(self.box)
                self.box_layout.setContentsMargins(10, 10, 10, 10)
                self.box_layout.setSpacing(15)
                
                # Infos Layout
                self.infos_layout = QHBoxLayout(self.frame_infos)
                self.infos_layout.setContentsMargins(0, 0, 0, 0)
                self.infos_layout.setSpacing(10)
                
                # Extraction Layout
                self.extraction_layout = QVBoxLayout(self.frame_extraction)
                self.extraction_layout.setContentsMargins(10, 15, 10, 10)
                
                # Layouts Extraction
                self.geographic_layout = QHBoxLayout(self.frame_geo)    
                self.geographic_layout.setSpacing(15)
                self.news_data_layout = QHBoxLayout(self.frame_news_data)
                self.conflit_data_layout = QHBoxLayout(self.frame_conflit_data)
                self.type_relation_layout = QHBoxLayout(self.frame_type_relation)
                
                # RadioBoxLayout
                self.radio_layout = QHBoxLayout(self.groupBox)
                self.radio_layout.setSpacing(0)
                
                # BUTTONS LAYOUT
                self.buttons_layout = QHBoxLayout(self.frame_buttons)

        # -------------------------------------------------------------------- WIDGETS
                # IN MAIN LAYOUT
                self.main_layout.addWidget(self.box)
                self.main_layout.addWidget(self.frame_buttons)
                
                # IN INFOS LAYOUT
                self.infos_layout.addWidget(self.label_publication)
                self.infos_layout.addWidget(self.data_publication)
                self.infos_layout.addWidget(self.label_update)
                self.infos_layout.addWidget(self.data_update)
                self.infos_layout.addWidget(self.label_machine_class)
                self.infos_layout.addWidget(self.machine_class)
                self.infos_layout.addWidget(self.label_confidence)
                self.infos_layout.addWidget(self.confidence_machine)
                
                # IN BOX LAYOUT
                self.box_layout.addWidget(self.title_article)
                self.box_layout.addWidget(self.frame_infos)
                self.box_layout.addWidget(self.text_box_article)
                self.box_layout.addWidget(self.frame_extraction)
                
                # IN EXTRATION LAYOUT
                self.radio_layout.addWidget(self.button_accept_news)
                self.radio_layout.addWidget(self.button_reject_news)
                self.radio_layout.addWidget(self.button_query)
                self.extraction_layout.addWidget(self.groupBox)
                self.extraction_layout.addWidget(self.frame_geo)
                self.extraction_layout.addWidget(self.frame_news_data)
                self.extraction_layout.addWidget(self.frame_conflit_data)
                self.extraction_layout.addWidget(self.frame_type_relation)
                
                # IN GEOGRAPHIC LAYOUT
                self.geographic_layout.addWidget(self.label_country)
                self.geographic_layout.addWidget(self.combo_country)
                self.geographic_layout.addWidget(self.label_region)
                self.geographic_layout.addWidget(self.combo_region)
                self.geographic_layout.addWidget(self.label_city)
                self.geographic_layout.addWidget(self.combo_city)
                self.geographic_layout.addWidget(self.label_date_event)
                self.geographic_layout.addWidget(self.input_date_event)
                
                # IN NEWS DATA
                self.news_data_layout.addWidget(self.label_deaths)
                self.news_data_layout.addWidget(self.input_deaths)
                self.news_data_layout.addWidget(self.label_conflict)
                self.news_data_layout.addWidget(self.combo_conflict)
                self.news_data_layout.addWidget(self.label_type_narcotic)
                self.news_data_layout.addWidget(self.combo_type_narcotic)
                self.news_data_layout.addWidget(self.label_qty_narcotic)
                self.news_data_layout.addWidget(self.input_qty_narcotic)
                
                # IN CONFLIT DATA
                self.conflit_data_layout.addWidget(self.label_name_actor_1)
                self.conflit_data_layout.addWidget(self.name_actor_1)
                self.conflit_data_layout.addWidget(self.label_name_actor_2)
                self.conflit_data_layout.addWidget(self.name_actor_2)
                self.conflit_data_layout.addWidget(self.label_latitude)
                self.conflit_data_layout.addWidget(self.latitude)
                self.conflit_data_layout.addWidget(self.label_longitude)
                self.conflit_data_layout.addWidget(self.longitude)
                self.type_relation_layout.addWidget(self.label_type_relation)
                self.type_relation_layout.addWidget(self.combo_type_relation)
                
                # IN BUTTONS LAYOUT
                self.buttons_layout.addWidget(self.button_back)
                self.buttons_layout.addWidget(self.button_finish)
                self.buttons_layout.addWidget(self.button_cancel)
                self.buttons_layout.addWidget(self.button_next)
                
                # --------- SET CENTRAL WIDGET ------------
                parent.addWidget(self.central_frame)
        
        def init_combo_box(self, combo_box, data):
                for key, value in data.items():
                        combo_box.addItem(key, value)