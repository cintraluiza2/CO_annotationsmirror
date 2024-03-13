# ----------------------------Imports--------------------------
# Imports Modules
import sys
import os

# Import QT Core
from qt_core import *

# Import Main Window
from controller.main_control import *
from controller.login_control import *
from controller.host_control import *

# -----------------------Main ---------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HostWindow()
    window.show()
    sys.exit(app.exec())
    