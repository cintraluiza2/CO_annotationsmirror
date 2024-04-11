from yaml import safe_load
from os import path

dir = path.dirname(path.abspath(__file__)) 
path_config = path.join(dir, "config.yml")  

with open(path_config, 'r', encoding='utf-8') as file:
    configs = safe_load(file)
    
server_configs = configs['server']
mongo_db_infos = configs['mongodb']
