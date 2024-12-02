# ----------------------------Imports--------------------------
# Imports Modules
import sys
from config import server_configs
# Import QT Core
from qt_core import *
# Import Main Window
from controller.main_control import *
# Imports SSHTUNNEL
from sshtunnel import open_tunnel, BaseSSHTunnelForwarderError # https://sshtunnel.readthedocs.io/en/latest/

# -----------------------Main ---------------------------
if __name__ == "__main__":
    try:
        # Tenta abrir um túnel SSH usando as configurações fornecidas
        with open_tunnel(
            (server_configs['ip_server'], server_configs['port']),
            ssh_username=server_configs['username'],
            ssh_password=server_configs['password'],
            local_bind_address=(server_configs['local_address'], server_configs['local_port_ssh']),
            remote_bind_address=(server_configs['remote_address'], server_configs['remote_port_ssh'])
        ) as server:
            app = QApplication(sys.argv)
            window = MainWindow()
            sys.exit(app.exec())
    except BaseSSHTunnelForwarderError:
        app = QApplication(sys.argv)
        window = MainWindow()
        window.erro_connect()
        