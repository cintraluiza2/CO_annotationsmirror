# OrgaExtractor

Repositório destinado a armazenar o código do **OrgaExtractor**, um software para anotação de dados sobre o crime organizado a partir de artigos de notícia.

## Instalação

Preferencialmente em um ambiente virtual (`$ virtualenv .venv`)

1. Geração do clone deste repositório com o comando:
    ```console
    $ git clone https://gitlab.com/ivato/textanalysis/crimeorganizado/comlextraction.git
    ```

2. Acesso ao projeto `comlextraction` especificamente:
    ```console
    $ cd .\comlextraction
    ```

3. Instalação dos pacotes necessários:
    ```console
    $ pip install -r requirements.txt
    ```

4. Especificação das credenciais de acesso ao banco de dados no arquivo `src/config.yml`.

## Execução

```console
$ python .\src\main.py
```

## Compilação

...