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
# Imports SSHTUNNEL
from sshtunnel import open_tunnel, BaseSSHTunnelForwarderError

# -----------------------Main ---------------------------
# Redireciona a saída de erro para o dispositivo nulo
sys.stderr = open(os.devnull, 'w')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    try:
        server = open_tunnel(
        )
        server.start()
        sys.exit(app.exec())
        server.close()
    except BaseSSHTunnelForwarderError:
        window.erro_connect()
        
