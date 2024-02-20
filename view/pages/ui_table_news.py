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
        
# -------------------------------------------------------------------- LAYOUTS
        # MAIN LAYOUT
        self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(15, 10, 15, 15)
        self.main_layout.setSpacing(15)
        
# -------------------------------------------------------------------- WIDGETS
        # IN MAIN LAYOUT
        self.main_layout.addWidget(self.title_page_news)
        
        # --------- SET CENTRAL WIDGET ------------
        parent.addWidget(self.central_frame)
