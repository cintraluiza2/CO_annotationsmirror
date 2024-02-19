# Imports Modules
import sys
import os

# Import QT Core
from qt_core import *

# Import Main Window
from view.windows.ui_main_window import UiMainWindow


# --------------- Main Window ------------------
class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Setup Main Window
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        # Toggle Button
        self.ui.toggle_button_menu.clicked.connect(self.toggle_button)

        self.show()

    def toggle_button(self):
        # Get Menu Width
        menu_width = self.ui.left_menu.width()

        # Check Width
        width = 50
        if menu_width == 50:
            width = 155

        # Start Animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(300)
        self.animation.setEasingCurve(QEasingCurve.InQuint)
        self.animation.start()


# -----------------------Main ---------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
