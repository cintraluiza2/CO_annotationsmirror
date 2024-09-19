class News():
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
        
    def set_keys(self):
        """
        Define chaves padrão para o objeto `News` e ajusta valores 
        de atributos relacionados à classificação e nível de certeza.

        Cria um dicionário modelo com chaves como "keyword", "acquisition_date", 
        "publication_date", etc., e seus valores padrão como `None`. 
        As chaves que ainda não estão presentes no dicionário do objeto serão 
        adicionadas com seus valores padrão.

        Também ajusta os atributos `manual_relevance_class`, `automatic_relevance_class`, 
        e `certainty_level`, caso esses atributos estejam presentes no objeto:
        - Se `manual_relevance_class` for uma string vazia ou `None`, 
        será definido como `None`. Caso contrário, será convertido para inteiro.
        - `automatic_relevance_class` e `certainty_level` são definidos como `None`, 
        se já existirem no objeto.

        Retorno:
            None
        """
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
            "accepted_by": None,
            "gangs": None,
            "id_event": None,
            "notes": []
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
        """
        Retorna o dicionário de atributos do objeto `News`.

        Retorno:
            dict: O dicionário de atributos da instância atual.
        """
        return self.__dict__
    