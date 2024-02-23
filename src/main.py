# ----------------------------Imports--------------------------
# Imports Modules
import sys
import os

# Import QT Core
from qt_core import *

# Import Main Window
from controller.view_control import *
from controller.db_control_connection import *

# -----------------------Main ---------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
    