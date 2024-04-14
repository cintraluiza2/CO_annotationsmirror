class News():
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        
    def set_keys(self):
        model_doc = {
            "keyword": None,
            "acquisition_date": None,
            "publication_date": None,
            "last_update": None,
            "newspaper": None,
            "url":None,
            "title": None,
            "article": None,
            "tags": None,
            "manual_relevance_class": None,
            "automatic_relevance_class": None,
            "confidence": None, 
            "relevance_model": None,
            "relevance_classification_date": None,
            "id_evento": None,
            "resumo": None,
            "data_evento": None,
            "quant_mortes": None,
            "tipo_droga": None,
            "quant_droga": None,
            "pais": None,
            "regiao": None,
            "municipio": None,
            "coordenados_GPS": None,
            "tipo_conflito_armado": None,
            "ator1_nome": None,
            "ator1_cod": None,
            "ator2_nome": None,
            "ator2_cod": None,
            "tipo_relacao_entre_atores": None
        }
        
        if hasattr(self, 'manual_relevance_class'):
            value = getattr(self, 'manual_relevance_class')
            if (value == '' or value == None):
                setattr(self, 'manual_relevance_class', None)
            else:
                setattr(self, 'manual_relevance_class', int(value))
        
        if hasattr(self, "automatic_relevance_class"):
            setattr(self, "automatic_relevance_class", None)
            
        if hasattr(self, "certainty_level"):
            setattr(self, "certainty_level", None)
                
        for key, value in model_doc.items():
            if key not in self.__dict__:
                self.__dict__[key] = value
                
    def get_dict(self):
        return self.__dict__
    