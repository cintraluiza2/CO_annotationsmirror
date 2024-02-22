# ----------------------------Imports--------------------------
# Import QT Core
from qt_core import *

# Import Windows
from view.windows.ui_login_window import UiLoginWindow
from view.windows.ui_main_window import UiMainWindow
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox, WarningMessageBoxOption
# Imports Data
from controller.db_control_connection import DBControlConnections

# ----------------------------Login Window--------------------------

class LoginWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()
        
        # DB CONTROL
        self.__db_control = DBControlConnections()
        
        # Setup Login Window
        self.ui = UiLoginWindow()
        self.ui.setup_ui(self)
        self.setWindowTitle("Login - QTSorting Hat")
        
        # Check Username and Password
        self.ui.butons_access.clicked.connect(self.access_permission)
        
        self.show()
        
    def access_permission(self):
        # DATABASE CHECK
        txt_user = self.ui.txt_user.text()
        txt_pass = self.ui.txt_pass_word.text()
        result = self.__db_control.check_password(txt_user, txt_pass)
        
        if result[0]:
            self.win = MainWindow()
            self.win.show()
            self.close() 
        else:
            if result[1] == "USER":
                dlg = WarningMessageBox(title="Error", txt="Invalid username or password")
            elif result[1] == "CPF":
                dlg = WarningMessageBox(title="Error", txt="Invalid CPF. Please check the number.")

            dlg.exec()

# ----------------------------Main Window--------------------------

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Setup Main Window
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

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
        
    # BUTTONS ACTIONS
    def reset_selection(self):
        for button in self.ui.left_menu.findChildren(QPushButton):
            try:
                button.set_active(False)
            except:
                pass
    
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
        