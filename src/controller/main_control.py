# ----------------------------Imports--------------------------
# Import QT Core
from qt_core import *

# Import Windows
from view.windows.ui_main_window import UiMainWindow
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# Imports Data
from controller.db_control_connection import DBControlConnections


# ----------------------------Main Window--------------------------

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Setup Main Window
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        
        # DB_CONTROL
        self.db = DBControlConnections()
        
        # TABLE PAGE
        self.table = self.ui.table_news_page.table
        self.table_init()
        # CLASSIFICATION
        self.classification = self.ui.classification_page
                
        # Toggle Button
        self.ui.toggle_button_menu.clicked.connect(self.toggle_button)
        
        # BUTTON HOME / TABLE
        self.ui.button_home.clicked.connect(self.show_page_table)
        
        # BUTTON CLASSIFICATION
        self.ui.button_class.clicked.connect(self.show_page_class)
        
        # BUTTON EXIT
        self.ui.button_exit.clicked.connect(self.show_dialog_exit)

        self.show()

# ---------------------------- Methods
    def reset_selection(self):
        for button in self.ui.left_menu.findChildren(QPushButton):
            try:
                button.set_active(False)
            except:
                pass
            
    # BUTTONS ACTIONS
    def toggle_button(self):
        # Get Menu Width
        menu_width = self.ui.left_menu.width()

        # Check Width
        width = 50
        if menu_width == 50:
            width = 160

        # Start Animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InQuint)
        self.animation.start()
        
    
    def show_page_table(self):
        self.reset_selection()
        self.ui.button_home.set_active(True)
        
        self.ui.pages.setCurrentIndex(0)
    
    def show_page_class(self):
        self.reset_selection()
        self.ui.button_class.set_active(True)
        
        self.ui.pages.setCurrentIndex(1)
        
    def show_dialog_exit(self):        
        dlg = WarningMessageBoxOption(title="Attention!", txt="Do you want to close the app?")
        
        if dlg.exec_() == QMessageBox.Yes:
            self.close()
        
# ------------------ TABLE CONTROL
    def table_init(self):
        list_news = self.db.news_list_table()
        
        for row, text in enumerate(list_news):
            for column, label in enumerate(text):
                self.table.setItem(row, column, QTableWidgetItem(str(text[label])))
            
        
        self.table.resizeColumnsToContents()
        
    def set_text_class(self, title_news):
        news = self.db.news_text(title_news)
        text_news = news["article"]
        self.classification.title_article.setText(title_news)
        self.classification.text_box_article.setText(text_news)
        