# Eventex

Sistema de Eventos enconmendado pela Morena

[![Build Status](https://travis-ci.org/gustavo7lagoas/eventex_wttd.svg?branch=master)](https://travis-ci.org/gustavo7lagoas/eventex_wttd)
[![Code Health](https://landscape.io/github/gustavo7lagoas/eventex_wttd/master/landscape.svg?style=flat)](https://landscape.io/github/gustavo7lagoas/eventex_wttd/master)

## Como desenvolver?

1. Clone o repositório
2. Crie um virtualenv com o Python 3.6
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes.
7. Execute as migrações
8. Execute o servidor

``` console
git clone https://github.com/gustavo7lagoas/eventex_wttd.git wttd
cd wttd
python -m venv .wttd
./.wttd/Scripts/activate.bat
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
python manage.py migrate
python manage.py runserver
```

## Como fazer o deploy?

1. Crie uma instância no heroku
2. Envie as configurações para o heroku
3. Defina uma SECRET_KEY segura para a instância
4. Defina DEBUG=False
5. Configure o serviço de email
6. Envie o código para o heroku

``` console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
```
