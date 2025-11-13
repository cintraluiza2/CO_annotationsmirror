APP_NAME = "Anotador do Crime Organizado 🚨📰📝"

APP_ICON = "📝"

APP_DESCRIPTION = (
    "Este é um anotador de notícias sobre o Crime Organizado. " \
    "Seu principal objetivo é servir como interface na classificação e extração " \
    "de informações de eventos sobre o crime organizado. Este software é fruto de um projeto da Universidade Federal de Goiás (UFG)."  \
)

APP_INSTRUCTIONS = (
    "↖️ Para começar a buscar notícias, preencha os filtros ao lado."
)

ITEMS_PER_PAGE = 20

CONFIDENCE_SCALE = [
    "#B0C4DE",  # LightSteelBlue (low saturation)
    "#A4C6E0",  # Soft Blue
    "#88B7D5",  # Muted Blue
    "#6A9ECF",  # Sky Blue
    "#4E89D3",  # Medium Blue
    "#3178C6",  # Strong Blue
    "#1F6BB0",  # Deep Blue
    "#155A99",  # Rich Blue
    "#0D4A80",  # Dark Blue
    "#003366",  # Midnight Blue (high saturation)
    "#002855",  # Deep Midnight Blue
]

DEFAULT_SORTING_FIELD = "Data de publicação"

FIELDS_MAPPING = {
    "automatic_relevance_class": "Anotação automática",
    "automatic_relevance_pipeline_confidence": "Confiança",
    "id_event": "ID",
    "publication_date": "Data de publicação",
    "newspaper": "Fonte",
    "title": "Título da notícia",
    "manual_relevance_class": "Anotação manual",
    "validated": "Validada",
}

INVERSE_FIELDS_MAPPING = {value: key for key, value in FIELDS_MAPPING.items()}

COLUMNS_ORDER = [
    "Abrir", "ID", "Data de publicação", "Fonte", "Título da notícia",
    "Anotação manual", "Anotação automática", "Confiança", "Validada"
]

LATIN_AMERICA_CONTRIES = [
    "Argentina", "Bolívia", "Brasil", "Chile", "Colômbia", "Costa Rica", 
    "Cuba", "Equador", "El Salvador", "Guatemala", "Haiti", "Honduras", 
    "México", "Nicarágua", "Panamá", "Paraguai", "Peru", 
    "República Dominicana", "Uruguai", "Venezuela"
]

ACTORS_RELATIONS = [
    "Cooperação",
    "Competição",
    "Confronto",
    "Integração",
    "Rivalidade",
]

DRUGS_DATA_MAPPING = {
    "drug_type": "Tipo de droga",
    "amount": "Quantidade",
    "metric": "Métrica",
}

OTHER_DRUGS_DATA_MAPPING = {
    "drug_type": "Outro tipo de droga",
    "amount": "Quantidade",
    "metric": "Métrica",
}

GUNS_DATA_MAPPING = {
    "gun_type": "Tipo de arma", 
    "quantity": "Quantidade"
}

ACTORS_DATA_MAPPING = {
    "actor 1": "Ator 1",
    "actor 2": "Ator 2",
    "relationship": "Relação",
}

DEFAULT_DRUGS_METRICS = ["Quilos (kg)", "Gramas (g)", "Toneladas (t)", "Tabletes", "Pacotes"]

DEFAULT_DRUGS = [
    'Álcool',
    'Anfetamina',
    'Cocaína',
    'Chetamina',
    'Crack',
    'Ecstasy (MDMA)',
    'Fentanil',
    'Fumaça/vapor de tabaco',
    'Haxixe',
    'Heroína',
    'LSD (ácido lisérgico)',
    'Maconha (cannabis)',
    'Maconha sintética',
    'Metanfetamina',
    'Psilocibina (cogumelos alucinógenos)',
    'Skunk',
]  
