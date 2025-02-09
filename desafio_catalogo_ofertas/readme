# Desafio - Catálogo de Ofertas

## Descrição

Este é um projeto que visa criar um catálogo de ofertas a partir de um **web scraping** no Mercado Livre. O sistema é composto por um **Script** em python que realiza o scraping
e salva os dados em um banco e uma API em **Django** que serve os dados salvos para o frontend. A interface do usuário é alimentada por **JavaScript** e exibe os produtos em cards dinâmicos, permitindo a filtragem das ofertas.

## Tecnologias Utilizadas

- **Backend**:
  - Django
  - Django Rest Framework (para a criação da API)
  - Selenium e WebDriver (para o scraping de dados)

- **Frontend**:
  - HTML
  - CSS
  - JavaScript

- **Banco de Dados**:
  - SQLite (para desenvolvimento e testes)

## Funcionalidades

- **Web Scraping**: Coleta os dados dos produtos no Mercado Livre, como título, preço e link da oferta.
- **API**: Exposição dos dados coletados através de uma API, que retorna as ofertas em formato JSON.
- **Frontend Dinâmico**: A interface exibe os produtos em cards, com a possibilidade de filtrar as ofertas.

## Como Rodar o Projeto

### Pré-requisitos

1. **Python 3.6+**: O projeto foi desenvolvido em Python 3.6 ou superior.
2. **Navegador**: Necessário possui a instalação do navegador Google Chrome, Edge ou Firefox.

### Passo 1: Clonando o Repositório

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/Pedro-Novais/desafio-catalogo-ofertas.git
```

### Passo 2: Rodar o projeto

1. Na raiz do projeto, será possível visualizar um executável, **run.bat**, 
Esse que realiza todos os passos necessárias para a execução do projeto
Desde a criação do ambiente virtual, intalação de dependências e a raspagem de dados
É necessário apenas rodas o comando em modo de administrador e aguardar que o servidor esteja em execução


### Passo 3: Testando a Aplicação

1. Abra o navegador e acesse `http://127.0.0.1:8000/` para visualizar a interface.
2. Você poderá ver os produtos do Mercado Livre sendo exibidos em cards e terá a opção de filtrá-los.

## Como Funciona

1. **Scraping de Dados**: O scraping é feito a partir de uma página do Mercado Livre. O script coleta os dados relevantes, e ao finalizar o processo salva os mesmo no banco de dados.
   
2. **API**: A API expõe os dados do scraping em formato JSON, permitindo que o frontend consuma e exiba esses dados de forma dinâmica.

3. **Frontend**: O frontend faz a requisição para a API e exibe os produtos como cards. É possível filtrar os itens com base em critérios como preço e categoria.

## Estrutura de Pastas

```
desafio-catalogo-ofertas/
├── scripts/                # Script que realiza a raspagem dos dados
│   ├── web_scrapping.py   
│   
├── config/                 # Códigos de configuração do Django
|   ├── asgi.py             
|   ├── setting.py          
|   ├── urls.py.py          
|   └── wsgi.py.py 
│   
├── database/               # Pasta que armazena o arquivo do banco de dados
|    ├── data.db
└── src/                    # Pasta que armazena o código das rotas e interactor da API
    ├── api/                
    ├── routes/
    ├── static/ 
    ├── templates/
    ├── views/                                
```