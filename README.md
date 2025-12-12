# OrgaExtractor

Esta é a versão Streamlit do software de anotação de dados de notícias sobre o crime organizado na América Latina.

## Instalação

1. Geração do clone deste repositório com o comando:
    ```shell
    git clone -b streamlit-version https://gitlab.com/ivato/textanalysis/crimeorganizado/co_newsannotation.git
    ```

2. Criação e inicialização do ambiente virtual:
    ```shell
    virtualenv .venv
    source .venv/bin/activate
    ```

3. Instalação dos pacotes necessários:
    ```shell
    pip install -r requirements.txt
    ```

4. Configuração do banco de dados:
    
    O arquivo `config.yml` já está configurado no repositório. 
    
    Para desenvolvimento local, você pode criar sua própria cópia:
    - Copie o arquivo de exemplo: `cp config.yml.example config.yml` (se necessário)
    - Edite com suas credenciais locais
    
    Formato do arquivo:
    ```yaml
    lamcad:
        server_ip: <value>
        server_port: <value>
        ssh_username: <value>
        ssh_password: <value>
        local_bind_ip: <value>
        local_bind_port: <value>
        remote_bind_ip: <value>
        remote_bind_port: <value>

    mongodb_lamcad:
        uri: <value>
        database: <value>
        accepted_news_collection: <value>
        unaccepted_news_collection: <value>
    ```

## Execução

Basta executar o comando abaixo para que uma porta local seja disponibilizada para a aplicação, que se torna acessível pelo navegador.
```shell
streamlit run main.py
```
