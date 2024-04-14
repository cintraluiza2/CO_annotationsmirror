from qt_core import *
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# IMPORTS DATA
from models.connection_options.connection import DBConnectionHandler
from models.repository.newsClass_repository import NewsClassRepository

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
        self.actor1 = ""
        self.actor2 = ""
        self.bool_save = False
                
        self.classification.combo_actor.currentIndexChanged.connect(self.name_actor)
        self.classification.name_actor.editingFinished.connect(self.edit_actor)
        self.classification.button_reject_news.clicked.connect(self.disable_widgets)
        self.classification.button_accept_news.clicked.connect(self.enabled_widgets)
        
        # self.classification.button_accept.clicked.connect(self.accept_news)
        # self.classification.button_rejected.clicked.connect(self.rejected_news)
        self.classification.button_finish.clicked.connect(self.save_infos)
        self.classification.button_cancel.clicked.connect(self.back_table_page)
        
    def set_title_list(self, title_list):
        self.title_list = title_list
        
    def set_text_class(self):
        if self.title_list:
            title_news = self.title_list.pop()
            news = self.__news_repository.select_one_news(title={"$regex": title_news}, optionsReturn={"title": 1, "article": 1})
            text_news = news["article"]
            self.title_news = news["title"]
            self.classification.title_article.setText(title_news)
            self.classification.text_box_article.setText(text_news)
        else:
            dlg = WarningMessageBox(title="Information", txt="The news classification process has been completed.")
            dlg.setIcon(QMessageBox.Information)
            dlg.exec()
            self.show_page_table_class()
            
    def accept_news(self):
        edit = {"manual_relevance_class": 1}
        self.__news_repository.edit_registry_news(self.title_news, edit)
        # self.set_text_class()
        
    def rejected_news(self):
        edit = {"manual_relevance_class": 0}
        self.__news_repository.edit_registry_news(self.title_news, edit)
        # self.set_text_class()
        
    def save_infos(self):
        accept_res = int(self.classification.button_accept_news.isChecked())
        if accept_res:
            data_event = self.classification.input_date_event.text()
            deaths = int(self.classification.input_deaths.text())
            conflict = self.classification.combo_conflict.currentIndex()
            type_narcotic = self.classification.combo_type_narcotic.currentIndex()
            actor_1 = self.actor1
            actor_2 = self.actor2
        

    def back_table_page(self):
        dlg = WarningMessageBoxOption(title="Question", txt="Just to confirm, you would like to return?")
        dlg.setIcon(QMessageBox.Question)
        if dlg.exec_() == QMessageBox.Yes:
            self.title_list.clear()
            self.show_page_table_class()
            
    def name_actor(self):
        selected_text = self.classification.combo_actor.currentText()
        # Atualizando o QLineEdit
        if selected_text == "Primeiro Ator":
            self.classification.label_name_actor.setText("Nome do Primeiro Ator:")
            self.classification.name_actor.clear()
        elif selected_text == "Segundo Ator":
            self.classification.label_name_actor.setText("Nome do Segundo Ator:")
            self.classification.name_actor.clear()
            
    def edit_actor(self):
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
            