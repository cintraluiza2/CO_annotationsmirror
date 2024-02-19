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
        
        self.show()

# -----------------------Main ---------------------------

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
