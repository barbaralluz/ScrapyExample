# ScrapyExample

Web Scraping com Python utilizando o framework Scrapy

## Descrição do Projeto
O seguinte projeto tem como objetivo colher as notícias da página da [Secretaria da Educação do Estado de São Paulo](http://www.educacao.sp.gov.br/noticias/) e armazená-los no banco de dados noSQL MongoDB (foi utilizado o Atlas - serviço de Banco de Dados como Serviço oferecido - versão gratuita).  
Para o desenvolvimento foi utilizada a biblioteca [Scrapy](https://scrapy.org/), um framework que facilita a coleta de dados ao utilizar outras bibliotecas do Python como requests e urllib.

* Versão de Python: 3.7.2
* Versão do Scrapy: 1.6.0
* Versão do Pymongo: 3.7.2 (para conexão com o BD) 
* Para a instalação dos pacotes foi utilizado o pip (a partir do Python 3.4 já está incluso na instalação do Python) - Versão do pip: pip 18.1

## Passos para executar o projeto:

> **OBS: O projeto foi criado e executado em um ambiente virtual (virtualenv) no Windows 10, foi necessário instalar os pacotes pypiwin32 e pywin32 para utilizar o Scrapy, porém se o projeto for executado no Linux estes pacotes podem não ser necessários.**

1. Baixe o projeto e vá até o diretório ".\ScrapyExample\scrapy_secretaria_educacao" e execute o seguinte comando para instalar as dependencias do projeto:

```sh
pip install -r requirements.txt
```

2. Feito isso continue no diretório e execute o comando abaixo para coletar todas as notícias da Secretaria da Educação do Estado de São Paulo

```sh
scrapy crawl educacaonoticias_allpages
```

- Caso queira somente colher as notícias da primeira página, execute o comando:

```sh
scrapy crawl educacaonoticias_onepage
```
