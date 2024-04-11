# ----------------------------Imports--------------------------
# Imports Modules
import sys
import os
import yaml
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
        with open('src\\configs.yml', 'r', encoding='utf-8') as file:
            server_configs = yaml.safe_load(file)['server']
            
        server = open_tunnel(
            (server_configs['ip_server'], server_configs['port']),
            ssh_username=server_configs['username'],
            ssh_password=server_configs['password'],
            local_bind_address=(server_configs['local_address'], server_configs['local_port_ssh']),
            remote_bind_address=(server_configs['remote_address'], server_configs['remote_port_ssh'])
        )
        server.start()
        sys.exit(app.exec())
        server.close()
    except BaseSSHTunnelForwarderError:
        window.erro_connect()
        
