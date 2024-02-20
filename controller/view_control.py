# ----------------------------Imports--------------------------
# Import QT Core
from qt_core import *

# Import Windows
from view.windows.ui_login_window import UiLoginWindow
from view.windows.ui_main_window import UiMainWindow
# IMPORT WIDGETS
from view.widgets.py_message_options import WarningMessageBox

class LoginWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        
        # Setup Login Window
        self.ui = UiLoginWindow()
        self.ui.setup_ui(self)
        
        self.show()

# --------------- Main Window ------------------
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
        dlg = WarningMessageBox(title="Attention!", text="Do you want to close the app?")
        
        if dlg.exec_() == QMessageBox.Yes:
            self.close()
        