# Módulo que acessa o arquivo config.yaml, que armazena
# as credenciais de acesso ao servidor ao banco de dados em si

from yaml import safe_load
from os import path

dir = path.dirname(path.abspath(__file__)) 
path_config = path.join(dir, "config.yaml")  

with open(path_config, 'r', encoding='utf-8') as file:
    configs = safe_load(file)
    
server_configs = configs['server']
mongo_db_infos = configs['mongodb']
