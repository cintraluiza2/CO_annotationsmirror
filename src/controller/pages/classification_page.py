from qt_core import *
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
# IMPORTS DATA GEO
from models.utils.geo_reference import GeoReference
# IMPORTS RANDOM
import hashlib
import random

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
        self.bool_save = False
        
        # INIT COMBOBOX
        self.geo = GeoReference()
        self.dict_geo = self.geo.geo_country()
        self.classification.init_combo_box(self.classification.combo_country, self.dict_geo)
        
        self.classification.combo_country.currentIndexChanged.connect(self.check_selected_country)
        self.classification.combo_region.currentIndexChanged.connect(self.check_selected_region)
        
        # BUTTONS EXTRACTION        
        self.classification.button_accept_news.clicked.connect(self.enabled_widgets)
        self.classification.button_reject_news.clicked.connect(self.disable_widgets)
        
        # Buttons Action
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
            news = self.__news_repository.select_one_news(title={"$regex": title_news}, optionsReturn={"title": 1, "article": 1, "manual_relevance_class": 1, "publication_date": 1, "last_update": 1, "automatic_relevance_class": 1, "confidence_relevance_class": 1, "tipo_conflito_armado": 1, "ator1_nome": 1, "ator2_nome": 1, "tipo_relacao_entre_atores": 1})
            
            mapping = {0: 'rejeite', 1: 'aceite', None: "SClasse"}
            self.title_news = news["title"]
            publication_news = news["publication_date"]
            update_news = news['last_update']
            automatic_news = mapping.get(news['automatic_relevance_class'])
            manual_news = news['manual_relevance_class']
            confidence_news = news['confidence_relevance_class']
            text_news = news["article"]
            armed_conflict = 0 if news["tipo_conflito_armado"] == None else news["tipo_conflito_armado"]
            actor1 = news["ator1_nome"]
            actor2 = news['ator2_nome']
            relationship_atores = 0 if news['tipo_relacao_entre_atores'] == None else news['tipo_relacao_entre_atores']
            
            if manual_news == 1: 
                self.classification.button_accept_news.setChecked(True)
                self.enabled_widgets()
            elif manual_news == 2:
                self.classification.button_query.setChecked(True)
                self.disable_widgets()
            else: 
                self.classification.button_reject_news.setChecked(True)
                self.disable_widgets()
            
            self.classification.title_article.setText(title_news)
            self.classification.data_publication.setText(publication_news)
            data = QDate.fromString(publication_news, "dd-MM-yyyy")
            self.classification.input_date_event.setDate(data)
            self.classification.data_update.setText(update_news)
            self.classification.machine_class.setText(automatic_news)
            self.classification.confidence_machine.setText(confidence_news)
            self.classification.text_box_article.setText(text_news)
            self.classification.combo_conflict.setCurrentIndex(armed_conflict)
            self.classification.name_actor_1.setText(actor1)
            self.classification.name_actor_2.setText(actor2)
            self.classification.combo_type_relation.setCurrentIndex(relationship_atores)
            
        else:
            dlg = WarningMessageBox(title="Informação", txt="O processo de classificação de noticías foi finalizado!")
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
        query = int(self.classification.button_query.isChecked())
        if accept_res:
            country = self.classification.combo_country.currentData()
            region = self.classification.combo_region.currentData()
            city = self.classification.combo_city.currentData()
            data_event = self.classification.input_date_event.text()
            deaths = int(self.classification.input_deaths.text())
            conflict = self.classification.combo_conflict.currentIndex()
            type_narcotic = self.classification.combo_type_narcotic.currentData()
            type_relation = self.classification.combo_type_relation.currentData()
            actor_1 = self.classification.name_actor_1.text()
            actor_2 = self.classification.name_actor_2.text()
            cod_actor_1 = cod_actor_2 = None
            if not (actor_1 == ""):
                cod_actor_1 = self.random_integer_code(actor_1)
            if not (actor_2 == ""):
                cod_actor_2 = self.random_integer_code(actor_2)
            
            edit = {"manual_relevance_class": accept_res, "data_evento": data_event, "quant_mortes": deaths, "tipo_conflito_armado": conflict, "pais": country, "regiao": region, "municipio": city, "ator1_nome": actor_1, "ator1_cod": cod_actor_1, "ator2_nome": actor_2, "ator2_cod": cod_actor_2, "tipo_droga": type_narcotic, "tipo_relacao_entre_atores": type_relation}
        elif query:
            edit = {"manual_relevance_class": 2}
        else:
            edit = {"manual_relevance_class": accept_res}
        self.__news_repository.edit_registry_news(self.title_news, edit)
            
    def finish_class(self):
        dlg = WarningMessageBoxOption(title="Questão", txt="Gostaria de finalizar o processo de anotação? O seu progresso será salvo!")
        dlg.setIcon(QMessageBox.Question)
        if dlg.exec_() == QMessageBox.Yes:
            self.save_infos()
            self.title_list.clear()
            self.show_page_table_class()

    def back_table_page(self):
        dlg = WarningMessageBoxOption(title="Atenção", txt="Gostaria de retornar ao menu inicial?\nO seu progresso será perdido!")
        dlg.setIcon(QMessageBox.Warning)
        dlg.setButtonText(QMessageBox.Yes, "Sim")
        if dlg.exec_() == QMessageBox.Yes:
            self.title_list.clear()
            self.show_page_table_class()
            
    def disable_widgets(self):
        for widget in self.classification.frame_extraction.findChildren(QFrame):
            widget.setStyleSheet("background-color: transparent; color: #8C8C8C")
            widget.setEnabled(False)
    
    def enabled_widgets(self):
        for widget in self.classification.frame_extraction.findChildren(QFrame):
            widget.setStyleSheet("QLabel{background-color: transparent; color: black; max-width: 12em}")
            widget.setEnabled(True)
            
    def check_selected_country(self, index):
        self.selected_country = self.classification.combo_country.currentText()
        self.classification.combo_region.setEnabled(True)
        if self.selected_country == "Brasil":
            self.classification.combo_region.clear()
            self.classification.combo_city.clear()
            self.dict_geo = self.geo.geo_state_br()
            self.classification.init_combo_box(self.classification.combo_region, self.dict_geo)

        elif self.selected_country == "Argentina":
            self.classification.combo_region.clear()
            self.classification.combo_city.clear()
            self.dict_geo = self.geo.geo_state_arg()
            self.classification.init_combo_box(self.classification.combo_region, self.dict_geo)
        else:
            self.classification.combo_region.clear()
            self.classification.combo_state.clear()
            self.classification.combo_city.clear()
            self.classification.combo_region.setEnabled(False)
            self.classification.combo_state.setEnabled(False)
            self.classification.combo_city.setEnabled(False)
            
    def check_selected_region(self, index):
        self.classification.combo_city.clear()
        self.classification.combo_city.setEnabled(True)
        index = self.classification.combo_region.currentData()

        if self.selected_country == "Brasil":
            self.dict_geo = self.geo.geo_city_br(index)
        if self.selected_country == "Argentina":
            self.dict_geo = self.geo.geo_city_arg(index)

        self.classification.init_combo_box(self.classification.combo_city, self.dict_geo)

    def random_integer_code(self, word):
        """Gera um número inteiro aleatório com base em uma palavra.

        Argumentos:
            palavra: A palavra que será usada para gerar o número aleatório.

        Retorna:
            Um número inteiro aleatório.
        """
        word_low = word.lower()

        # Cria um objeto hash usando o algoritmo SHA-256.
        hash_obj = hashlib.sha256()

        # Atualiza o objeto hash com a palavra codificada em bytes.
        hash_obj.update(word_low.encode('utf-8'))

        # Obtém o hash digest como um valor hexadecimal.
        digest_hexa = hash_obj.hexdigest()

        seed_number = int(digest_hexa, 16)
        random.seed(seed_number)
        # Definie um numero de até 8 digitos
        rand_number = random.randint(1, 100000000)

        return rand_number
        