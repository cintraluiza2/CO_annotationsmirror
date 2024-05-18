import json
from os import path

class GeoReference:
    def __init__(self) -> None:
        self.path_dir =  "src/models/utils/georeferenced_codes/"
        
    def get_geo_country(self):
        data = {}
        path_json = path.join(self.path_dir, 'countries.json')
        with open(path_json, 'r') as arquivo:
            response = json.load(arquivo)
            
        for pais in response:
            data[pais['name']] = int(pais['numeric_code'])
        data['Outros'] = 0

        return data

    def get_geo_state(self, country: str):
        path_json = path.join(self.path_dir, 'states.json')
        with open(path_json, 'r') as arquivo:
            response = json.load(arquivo)
            
        data = {}
        for state in response:
            if state['country_name'] == country:
                data[state['name']] = int(state['id'])
        data['Outros'] = 0

        return data

    
    def get_geo_city(self, index):
        path_json = path.join(self.path_dir, 'cities.json')
        with open(path_json, 'r') as arquivo:
            response = json.load(arquivo)
            
        data = {}
        for city in response:
            if city['state_id'] == index:
                data[city['name']] = int(city['id'])
        data['Outros'] = 0
        
        return data
    
    def get_lati_long(self, country_id, state_id, city_id):
        if city_id:
            path_json = path.join(self.path_dir, 'cities.json')
            with open(path_json, 'r') as arquivo:
                response = json.load(arquivo)
                
            for city in response:
                if city['id'] == city_id:
                    return (city['latitude'], city['longitude'])
                
        if state_id:
            path_json = path.join(self.path_dir, 'states.json')
            with open(path_json, 'r') as arquivo:
                response = json.load(arquivo)
                
            for state in response:
                if state['id'] == state_id:
                    return (state['latitude'], state['longitude'])
        
        if country_id:
            path_json = path.join(self.path_dir, 'countries.json')
            with open(path_json, 'r') as arquivo:
                response = json.load(arquivo)
                
            for country in response:
                if int(country['numeric_code']) == country_id:
                    return (country['latitude'], country['longitude'])
        
        
        return (0, 0)