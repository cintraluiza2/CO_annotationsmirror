import requests

class GeoReference:
    def __init__(self) -> None:
        self.__link_paises = "https://servicodados.ibge.gov.br/api/v1/localidades/paises?view=nivelado"
        self.__link_regioes_br = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes?view=nivelado"
        self.__link_municipios_br = "https://servicodados.ibge.gov.br/api/v1/localidades/regioes/{}/municipios?view=nivelado"
        
    def geo_country(self):
        data = {}
        response = requests.get(self.__link_paises).json()
        for pais in response:
            data[pais['pais-nome']] = pais['pais-M49']
        
        return data
    
    def geo_region_br(self):
        data = {}
        response = requests.get(self.__link_regioes_br).json()
        for region in response:
            data[region['regiao-nome']] = region['regiao-id']
        
        return data
    
    def geo_city_br(self, index):
        data = {}
        string = self.__link_municipios_br.format(index)
        response = requests.get(string).json()
        for city in response:
            data[city['municipio-nome']] = city['municipio-id']
        
        return data
    