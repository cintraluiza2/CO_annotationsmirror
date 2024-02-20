# ----------------------------Imports--------------------------
# Imports Modules
import sys
import os

# Import QT Core
from qt_core import *

# Import Main Window
from controller.view_control import *

# -----------------------Main ---------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
    