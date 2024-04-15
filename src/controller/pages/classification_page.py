from qt_core import *
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
# IMPORTS DATA GEO
from models.utils.geo_reference import GeoReference

class ClassificationManager:
    def __init__(self, classification, show_page_table_class) -> None:
        self.classification = classification
        self.show_page_table_class = show_page_table_class
        
        # DB_VARIABLES
        self.__db_handle = DBConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__news_repository = NewsClassRepository(self.__db_connection)
        
        # VARIABLES GLOBAL
        self.title_list = []
        self.title_news = ""
        self.title_select = ""
        self.actor1 = ""
        self.actor2 = ""
        self.bool_save = False
        
        # INIT COMBOBOX
        self.geo = GeoReference()
        self.dict_geo = self.geo.geo_country()
        self.classification.init_combo_box(self.classification.combo_country, self.dict_geo)
        
        self.classification.combo_country.currentIndexChanged.connect(self.check_selected_country)
        self.classification.combo_region.currentIndexChanged.connect(self.check_selected_region)
        self.disable_widgets()
        
        # BUTTONS EXTRACTION        
        self.classification.combo_actor.currentIndexChanged.connect(self.name_actor)
        self.classification.name_actor.editingFinished.connect(self.edit_actor)
        self.classification.button_accept_news.clicked.connect(self.enabled_widgets)
        self.classification.button_reject_news.clicked.connect(self.disable_widgets)
        
        
        self.classification.button_back.clicked.connect(self.back_news)
        self.classification.button_next.clicked.connect(self.next_news)
        self.classification.button_finish.clicked.connect(self.finish_class)
        self.classification.button_cancel.clicked.connect(self.back_table_page)
        
    def set_title_list(self, title_list, title_select):
        self.title_list = title_list
        self.title_select = title_select
        
    def set_text_class(self):
        if self.title_list:
            title_news = self.title_list[self.title_select]
            news = self.__news_repository.select_one_news(title={"$regex": title_news}, optionsReturn={"title": 1, "article": 1, "manual_relevance_class": 1, "publication_date": 1, "last_update": 1, "automatic_relevance_class": 1, "confidence_relevance_class": 1})
            
            mapping = {0: 'rejeite', 1: 'aceite', None: None}
            self.title_news = news["title"]
            publication_news = news["publication_date"]
            update_news = news['last_update']
            automatic_news = mapping.get(news['automatic_relevance_class'])
            manual_news = news['manual_relevance_class']
            confidence_news = news['confidence_relevance_class']
            text_news = news["article"]
            
            if manual_news: self.classification.button_accept_news.setChecked(True) 
            else: self.classification.button_reject_news.setChecked(True)
            
            self.classification.title_article.setText(title_news)
            self.classification.data_publication.setText(publication_news)
            data = QDate.fromString(publication_news, "dd-MM-yyyy")
            self.classification.input_date_event.setDate(data)
            self.classification.data_update.setText(update_news)
            self.classification.machine_class.setText(automatic_news)
            self.classification.confidence_machine.setText(confidence_news)
            self.classification.text_box_article.setText(text_news)
            
        else:
            dlg = WarningMessageBox(title="Information", txt="The news classification process has been completed.")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            self.show_page_table_class()
            
    def next_news(self):
        self.save_infos()
        self.title_select = self.title_select + 1
        self.set_text_class()
        
    def back_news(self):
        self.save_infos()
        self.title_select = self.title_select - 1
        self.set_text_class()
        
    def save_infos(self):
        """
            Salvar as informações extraidas do texto.
        """
        accept_res = int(self.classification.button_accept_news.isChecked())
        if accept_res:
            country = self.classification.combo_country.currentData()
            region = self.classification.combo_region.currentData()
            city = self.classification.combo_city.currentData()
            data_event = self.classification.input_date_event.text()
            deaths = int(self.classification.input_deaths.text())
            conflict = self.classification.combo_conflict.currentIndex()
            type_narcotic = self.classification.combo_type_narcotic.currentIndex()
            actor_1 = self.actor1
            actor_2 = self.actor2
            edit = {"manual_relevance_class": accept_res, "data_evento": data_event, "quant_mortes": deaths, "tipo_conflito_armado": conflict, "pais": country, "regiao": region, "municipio": city, "ator1_nome": actor_1, "ator2_nome": actor_2, "tipo_droga": type_narcotic}
        
        edit = {"manual_relevance_class": accept_res}
        self.__news_repository.edit_registry_news(self.title_news, edit)
            
    def finish_class(self):
        dlg = WarningMessageBoxOption(title="Question", txt="Would you like to finish?")
        dlg.setIcon(QMessageBox.Question)
        if dlg.exec_() == QMessageBox.Yes:
            self.save_infos()
            self.title_list.clear()
            self.show_page_table_class()

    def back_table_page(self):
        dlg = WarningMessageBoxOption(title="Question", txt="Just to confirm, you would like to return?")
        dlg.setIcon(QMessageBox.Question)
        if dlg.exec_() == QMessageBox.Yes:
            self.title_list.clear()
            self.show_page_table_class()
            
    def name_actor(self):
        """
            Atualizar o QLabel do nome do Ator.
        """
        selected_text = self.classification.combo_actor.currentText()
        # Atualizando o QLineEdit
        if selected_text == "Primeiro Ator":
            self.classification.label_name_actor.setText("Nome do Primeiro Ator:")
            self.classification.name_actor.clear()
        elif selected_text == "Segundo Ator":
            self.classification.label_name_actor.setText("Nome do Segundo Ator:")
            self.classification.name_actor.clear()
            
    def edit_actor(self):
        """
            Recuperar o nome do Ator digitado.
        """
        selected_id = self.classification.combo_actor.currentIndex()
        text_name = self.classification.name_actor.text()
        if not selected_id:
            self.actor1 = text_name
        else:
            self.actor2 = text_name
            
    def disable_widgets(self):
        for widget in self.classification.frame_extraction.findChildren(QFrame):
            widget.setEnabled(False)
    
    def enabled_widgets(self):
        for widget in self.classification.frame_extraction.findChildren(QFrame):
            widget.setEnabled(True)
            
    def check_selected_country(self, index):
        selected_country = self.classification.combo_country.currentText()
        if selected_country == "Brasil":
            self.classification.combo_region.setEnabled(True)
            self.dict_geo = self.geo.geo_region_br()
            self.classification.init_combo_box(self.classification.combo_region, self.dict_geo)
        else:
            self.classification.combo_city.clear()
            self.classification.combo_region.clear()
            self.classification.combo_region.setEnabled(False)
            self.classification.combo_city.setEnabled(False)
            
    def check_selected_region(self, index):
        self.classification.combo_city.clear()
        self.classification.combo_city.setEnabled(True)
        self.dict_geo = self.geo.geo_city_br((index + 1))
        self.classification.init_combo_box(self.classification.combo_city, self.dict_geo)
        