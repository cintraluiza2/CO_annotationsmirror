# Organização de `src`

- `data/`: scripts de acesso ao banco de dados.
- `views/`: scripts de criação ou modificação da interface gráfica.
- `controllers/`: scripts de atuação intermediária entre banco de dados e interface gráfica, geralmente responsável pela tradução dos dados do usuário para o banco ou o inverso. Qualquer requisição ao banco de dados deve ser demandada ao módulo `data`.
- `settings.py`: constantes da aplicação (nomes de colunas, mapeamento de valores, opções de seleção etc.).