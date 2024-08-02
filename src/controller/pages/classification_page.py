from qt_core import *
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository
# IMPORTS DATA GEO
from models.utils.geo_reference import GeoReference
from models.utils.data import *
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
        self.id_news = -1
        self.title_select = ""
        self.bool_save = False
        
        # INIT COMBOBOX
        self.geo = GeoReference()
        self.dict_geo = self.geo.get_geo_country()
        self.init_combo_box(self.classification.combo_country, self.dict_geo)
        self.init_combo_box(self.classification.combo_narcotic_1, data_type_narcotic)
        self.init_combo_box(self.classification.combo_narcotic_2, data_type_narcotic)
        self.init_combo_box(self.classification.combo_narcotic_3, data_type_narcotic)
        self.init_combo_box(self.classification.combo_type_relation, data_type_relation)
        
        # CONNECT CURRENT COMBO BOX
        self.classification.combo_country.currentIndexChanged.connect(self.check_selected_country)
        self.classification.combo_region.currentIndexChanged.connect(self.check_selected_region)
        self.classification.button_geo_city.clicked.connect(self.active_button_geo)
        
        # BUTTONS EXTRACTION        
        self.classification.button_accept_news.clicked.connect(self.enabled_widgets)
        self.classification.button_reject_news.clicked.connect(self.disable_widgets)
        self.classification.btt_add_weapons.clicked.connect(self.add_weapons)
        self.classification.btt_rmv_weapons.clicked.connect(self.remove_weapons)
        
        # Buttons Action
        self.classification.button_back.clicked.connect(self.back_news)
        self.classification.button_next.clicked.connect(self.next_news)
        self.classification.button_finish.clicked.connect(self.finish_class)
        self.classification.button_cancel.clicked.connect(self.back_table_page)
        
    def set_title_list(self, title_list, title_select, model_table):
        self.title_list = title_list
        self.title_select = title_select
        self.model_table = model_table
        
    def set_text_class(self):
        if self.title_list:
            title_news = self.title_list[self.title_select]
            self.id_news = title_news
            news = self.__news_repository.select_one_news(self.id_news, optionsReturn={"title": 1, "article": 1, "publication_date": 1, "last_update": 1, "notes": 1})
            
            title_news = news["title"]
            publication_news = news["publication_date"]
            update_news = news['last_update']
            text_news = news["article"]
            
            self.classification.title_article.setText(title_news)
            self.classification.data_update.setText(update_news)
            self.classification.text_box_article.setText(text_news)
            self.classification.data_publication.setText(publication_news)
            data = QDate.fromString(publication_news, "dd-MM-yyyy")
            self.classification.input_date_event.setDate(data)
            
        else:
            dlg = WarningMessageBox(title="Informação", txt="O processo de classificação de noticías foi finalizado!")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            self.show_page_table_class()
            
    def set_note_class(self):
        note =  self.__news_repository.select_note_news(self.id_news, self.id_user)

        if note:
            manual_news = note['manual_relevance_class']
            if manual_news == 1: 
                self.classification.button_accept_news.setChecked(True)
                self.classification.button_query.setChecked(False)
                self.enabled_widgets()
                
                mapping = {0: 'rejeite', 1: 'aceite', None: "SClasse"}
                # automatic_news = mapping.get(note['automatic_relevance_class'])
                confidence_news = note['confidence_relevance_class']
                armed_conflict = 0 if note["tipo_conflito_armado"] == None else note["tipo_conflito_armado"]
                actor1 = note["ator1_nome"]
                actor2 = note['ator2_nome']
                relationship_atores = 0 if note['tipo_relacao_entre_atores'] == None else note['tipo_relacao_entre_atores']
                type_narcotic = note['tipo_droga']
                qty_narcotic = note['quant_droga']
                weapons = note['weapons']
                pais = 0 if note["pais"] == None else int(note["pais"])
                regiao = 0 if note["regiao"] == None else int(note["regiao"])
                municipio = 0 if note["municipio"] == None else int(note["municipio"])
                coordenadas_GPS = note['coordenadas_GPS']
                lati, long = coordenadas_GPS['coordinates']
                
                self.classification.combo_country.currentData(pais)
                self.classification.combo_region.currentData(regiao)
                self.classification.combo_city.currentData(municipio)
                if lati != 0 and long != 0: self.classification.latitude.setText(f"{lati}, {long}")
                else: self.classification.latitude.setText("")
                self.classification.confidence_machine.setText(confidence_news)
                self.classification.check_conflict.setChecked(armed_conflict)
                self.classification.combo_narcotic_1.setCurrentIndex(type_narcotic[0])
                self.classification.input_qty_narcotic_1.setValue(qty_narcotic[0])
                self.classification.combo_narcotic_2.setCurrentIndex(type_narcotic[1])
                self.classification.input_qty_narcotic_2.setValue(qty_narcotic[1])
                self.classification.combo_narcotic_3.setCurrentIndex(type_narcotic[2])
                self.classification.input_qty_narcotic_3.setValue(qty_narcotic[2])
                self.set_list_weapons(weapons)
                self.classification.name_actor_1.setText(actor1)
                self.classification.name_actor_2.setText(actor2)
                self.classification.combo_type_relation.setCurrentIndex(relationship_atores)
                
            elif manual_news == 2:
                self.classification.button_query.setChecked(True)
                self.disable_widgets()
            else: 
                self.classification.button_reject_news.setChecked(True)
                self.classification.button_query.setChecked(False)
                self.disable_widgets()

            
    def next_news(self):
        self.save_infos()
        self.title_select = self.title_select + 1
        self.set_text_class()
        
    def back_news(self):
        self.save_infos()
        self.title_select = self.title_select - 1
        self.set_text_class()
        
    def get_infos_note(self):
        country = self.classification.combo_country.currentData()
        region = self.classification.combo_region.currentData()
        city = self.classification.combo_city.currentData()
        lati_long_txt = self.classification.latitude.text()
        if lati_long_txt == '':
            lati, long = self.geo.get_lati_long(country, region, city)
        else:
            lati, long = lati_long_txt.split(',')
        data_event = self.classification.input_date_event.text()
        deaths = int(self.classification.input_deaths.text())
        conflict = int(self.classification.check_conflict.isChecked())
        type_narcotic_1 = self.classification.combo_narcotic_1.currentData()
        qty_narcotic_1 = self.classification.input_qty_narcotic_1.value()
        type_narcotic_2 = self.classification.combo_narcotic_2.currentData()
        qty_narcotic_2 = self.classification.input_qty_narcotic_2.value()
        type_narcotic_3 = self.classification.combo_narcotic_3.currentData()
        qty_narcotic_3 = self.classification.input_qty_narcotic_3.value()
        weapons, weapons_codes = self.get_list_weapons()
        actor_1 = self.classification.name_actor_1.text()
        actor_2 = self.classification.name_actor_2.text()
        type_relation = self.classification.combo_type_relation.currentData()
        cod_actor_1 = cod_actor_2 = None
        if not (actor_1 == ""):
            cod_actor_1 = self.random_integer_code(actor_1)
        if not (actor_2 == ""):
            cod_actor_2 = self.random_integer_code(actor_2)
            
        # List type narcotic
        type_narcotic = [type_narcotic_1, type_narcotic_2, type_narcotic_3]
        qty_narcotic = [qty_narcotic_1, qty_narcotic_2, qty_narcotic_3]
        
        coordenadas_GPS = {"type": "Point", "coordinates": [float(lati), float(long)]}
        
        edit = {"manual_relevance_class": 1, "data_evento": data_event, "quant_mortes": deaths, "tipo_conflito_armado": conflict, "pais": country, "regiao": region, "municipio": city, "coordenadas_GPS": coordenadas_GPS,  "tipo_droga": type_narcotic, "quant_droga": qty_narcotic, "weapons": weapons, "weapons_codes": weapons_codes, "ator1_nome": actor_1, "ator1_cod": cod_actor_1, "ator2_nome": actor_2, "ator2_cod": cod_actor_2, "tipo_relacao_entre_atores": type_relation}
        
        return edit
        
    def save_infos(self):
        """
            Salvar as informações extraidas do texto.
        """
        accept_res = int(self.classification.button_accept_news.isChecked())
        query = int(self.classification.button_query.isChecked())
    
        if accept_res:
            edit = self.get_infos_note()
            
        elif query:
            edit = {"manual_relevance_class": 2}
        else:
            edit = {"manual_relevance_class": accept_res}
            
        self.__news_repository.edit_registry_news(self.id_news, edit)
        
        mapping = {0: "Irrelevante", 1: "Relevante", 2: "Dúvida"}
        new_status = QStandardItem(str(mapping.get(edit["manual_relevance_class"])))
        new_status.setTextAlignment(Qt.AlignCenter)
        self.model_table.setItem(self.title_select, 3, new_status)
        
            
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
            widget.setStyleSheet("color: #8C8C8C")
            widget.setEnabled(False)
    
    def enabled_widgets(self):
        for widget in self.classification.frame_extraction.findChildren(QFrame):
            widget.setStyleSheet("QLabel{background-color: transparent;}")
            widget.setEnabled(True)
            
    def check_selected_country(self, index):
        self.classification.combo_region.clear()
        self.classification.combo_city.clear()
        self.selected_country = self.classification.combo_country.currentText()
        self.classification.combo_region.setEnabled(True)
        
        self.dict_geo = self.geo.get_geo_state(self.selected_country)
        
        if self.dict_geo: # Se a lista não estiver vazia
            self.init_combo_box(self.classification.combo_region, self.dict_geo)
        else:
            self.classification.combo_region.setEnabled(False)
            self.classification.combo_city.setEnabled(False)
            
    def check_selected_region(self, index):
        self.classification.combo_city.clear()
        self.classification.combo_city.setEnabled(True)
        index = self.classification.combo_region.currentData()
        self.dict_geo = self.geo.get_geo_city(index)

        if self.dict_geo:
            self.init_combo_box(self.classification.combo_city, self.dict_geo)
        else:
            self.classification.combo_city.setEnabled(False)
        
    def add_weapons(self):
        arm = self.classification.input_weapons.text()
        self.classification.list_weapons.addItem(arm)
        
    def remove_weapons(self):
        if self.classification.list_weapons.currentItem() is not None:
            # Remover o item selecionado
            self.classification.list_weapons.takeItem(self.classification.list_weapons.currentRow())
        
    def set_list_weapons(self, weapons):
        for item in weapons:
            self.classification.list_weapons.addItem(item)
        
    def get_list_weapons(self):
        items_list = []
        items_cod_list = []
        list_widget = self.classification.list_weapons
        for index in range(list_widget.count()):
            item = list_widget.item(index).text()
            item_cod = self.random_integer_code(item)
            items_list.append(item)
            items_cod_list.append(item_cod)
            
        return items_list, items_cod_list

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
    
    def active_button_geo(self):
        country = self.classification.combo_country.currentData()
        region = self.classification.combo_region.currentData()
        city = self.classification.combo_city.currentData()
    
        lati, long = self.geo.get_lati_long(country, region, city)
        
        if lati != 0 and long != 0: self.classification.latitude.setText(f"{lati}, {long}")
        
    
    def init_combo_box(self, combo_box, data):
                for key, value in data.items():
                        combo_box.addItem(key, value)
        