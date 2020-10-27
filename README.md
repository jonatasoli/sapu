# sapu
Sistema de Autenticação e Permissão de usuários

# Requisitos

* Python 3.9

* Um banco postgresql configurado

* Docker (Opcional)

# Configuração

* Baixar o repositório

* Instalar o poetry

* Usar o poetry install pra instalr as dependencias

```
poetry install
```

* Criar um arquivo de configuração .secrets
** Há um arquivo de exemplo na pasta contrib/secrets-sample

* Configurar a url de conexão no secrets

* Acessar a pasta app

* Rodar os testes
```
poetry install
```


# Inicializar

* Ir pra pasta app

* rodar o uvicorn

```
uvicorn main:app --reload --host 0.0.0.0 --port 7777
```

* Acessar [http://localhost:7777/docs](http://localhost:7777/docs)


* Contribuir

* Acesssar o grupo no Telegram
[Grupo do Telegram](https://t.me/joinchat/C0TRMBgJzNg1OHT5Z2zfPA)
