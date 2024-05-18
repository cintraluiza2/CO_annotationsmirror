import json
from os import path

class GeoReference:
    def __init__(self) -> None:
        self.path_dir =  "src/models/utils/georeferenced_codes/"
        
    def geo_country(self):
        data = {}
        path_json = path.join(self.path_dir, 'countries.json')
        with open(path_json, 'r') as arquivo:
            response = json.load(arquivo)
            
        for pais in response:
            data[pais['name']] = int(pais['numeric_code'])
        data['Outros'] = 0

        return data

    def geo_state(self, country: str):
        path_json = path.join(self.path_dir, 'states.json')
        with open(path_json, 'r') as arquivo:
            response = json.load(arquivo)
            
        data = {}
        for state in response:
            if state['country_name'] == country:
                data[state['name']] = int(state['id'])
        data['Outros'] = 0

        return data

    
    def geo_city(self, index):
        path_json = path.join(self.path_dir, 'cities.json')
        with open(path_json, 'r') as arquivo:
            response = json.load(arquivo)
            
        data = {}
        for city in response:
            if city['state_id'] == index:
                data[city['name']] = int(city['id'])
        data['Outros'] = 0
        
        return data