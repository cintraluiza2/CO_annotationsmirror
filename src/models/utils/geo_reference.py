import requests
import json

class GeoReference:
    def __init__(self) -> None:
        self.__link_regioes_br = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes?view=nivelado"
        self.__link_municipios_br = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes/{}/municipios?view=nivelado"
        self.__link_city_arg = "https://apis.datos.gob.ar/georef/api/municipios?provincia={}&campos=id,nombre&max=100"
        
    def geo_country(self):
        data = {}
        with open('src/models/utils/georeferenced_codes/countries.json', 'r') as arquivo:
            response = json.load(arquivo)
        for pais in response:
            data[pais['pais-nome']] = pais['pais-M49']
        data['Outros'] = 0
        
        return data
    
    def geo_region_br(self):
        with open('src/models/utils/georeferenced_codes/brazil.json', 'r') as arquivo:
            response = json.load(arquivo)
            
        data = {}
        for item in response:
            data[item['regiao-nome']] = item['regiao-id']
        data['Outros'] = 0
        
        return data

    def geo_state_br(self):
        with open('src/models/utils/georeferenced_codes/brazil.json', 'r') as arquivo:
            response = json.load(arquivo)
            
        data = {}
        for item in response:
            data[item['UF-nome']] = item['UF-id']
        data['Outros'] = 0
        
        return data
    
    def geo_city_br(self, index):
        with open('src/models/utils/georeferenced_codes/brazil.json', 'r') as arquivo:
            response = json.load(arquivo)
        
        # Cria o filtro que só retorna True se o Regiao de x for igual a index.
        filtro = lambda x: x["UF-id"] == index
        response = list(filter(filtro , response))
            
        data = {}
        for item in response:
            data[item['municipio-nome']] = item['municipio-id']
        data['Outros'] = 0
        
        return data
    
    def geo_region_arg(self):
        with open('src/models/utils/georeferenced_codes/argentina.json', 'r') as arquivo:
            response = json.load(arquivo)
            
        data = {}
        for item in response["provicias"]:
            data[item['nombre']] = int(item['id'])
        data['Outros'] = 0
        
        return data

    def geo_state_arg(self):
        with open('src/models/utils/georeferenced_codes/argentina.json', 'r') as arquivo:
            response = json.load(arquivo)
            
        data = {}
        for item in response:
            data[item['provincia']['nombre']] = int(item['provincia']['id'])
        data['Outros'] = 0
        
        return data
    
    def geo_city_arg(self, index):
        with open('src/models/utils/georeferenced_codes/argentina.json', 'r') as arquivo:
            response = json.load(arquivo)

        # Cria o filtro que só retorna True se o Regiao de x for igual a index.
        filtro = lambda x: x['provincia']['id'] == str(index)
        response = list(filter(filtro , response))
        
        data = {}
        for item in response:
            data[item['nombre']] = int(item['id'])
        data['Outros'] = 0
        
        return data