import json
from os import path

class GeoReference:
    def __init__(self) -> None:
        self.path_dir =  "src/models/utils/georeferenced_codes/"
        
    def get_geo_country(self):
        """
        Retorna um dicionário de países com seus respectivos códigos numéricos.

        Abre o arquivo JSON contendo os dados dos países e extrai o nome e o código numérico de cada país.
        Adiciona também uma entrada "Outros" com o valor 0 para países não identificados.

        Retorno:
            dict: Um dicionário com o nome dos países como chave e seus códigos numéricos como valor.
        """
        data = {}
        path_json = path.join(self.path_dir, 'countries.json')
        with open(path_json, 'r') as arquivo:
            response = json.load(arquivo)
            
        for pais in response:
            data[pais['name']] = int(pais['numeric_code'])
        data['Outros'] = 0

        return data

    def get_geo_state(self, country: str):
        """
        Retorna um dicionário de estados com seus respectivos códigos numéricos, 
        com base no nome do país fornecido.

        Abre o arquivo JSON contendo os dados dos estados e filtra os estados 
        pertencentes ao país especificado.
        Adiciona também uma entrada "Outros" com o valor 0 para estados não identificados.

        Parâmetros:
            country (str): O nome do país para o qual os estados devem ser buscados.

        Retorno:
            dict: Um dicionário com o nome dos estados como chave e seus códigos numéricos como valor.
        """
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
        """
        Retorna um dicionário de cidades com seus respectivos códigos numéricos, 
        com base no código do estado fornecido.

        Abre o arquivo JSON contendo os dados das cidades e filtra as cidades 
        pertencentes ao estado especificado.
        Adiciona também uma entrada "Outros" com o valor 0 para cidades não identificadas.

        Parâmetros:
            index (int): O código numérico do estado para o qual as cidades devem ser buscadas.

        Retorno:
            dict: Um dicionário com o nome das cidades como chave e seus códigos numéricos como valor.
    """
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
        """
        Retorna as coordenadas de latitude e longitude com base nos IDs 
        fornecidos para o país, estado e cidade.

        Verifica se o ID da cidade, estado ou país foi fornecido e retorna as respectivas coordenadas.
        Se uma cidade for identificada, suas coordenadas são retornadas.
        Se não houver uma cidade, verifica o estado.
        Se nenhum estado for identificado, verifica o país.
        Se nenhuma localização for identificada, retorna as coordenadas (0, 0).

        Parâmetros:
            country_id (int): O código numérico do país.
            state_id (int): O código numérico do estado.
            city_id (int): O código numérico da cidade.

        Retorno:
            tuple: Uma tupla contendo a latitude e a longitude.
        """
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