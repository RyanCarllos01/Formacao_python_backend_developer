# Forma��o Python Backend Developer

Este reposit�rio re�ne alguns exerc�cios e pr�ticas de Python para forma��o backend, com foco em:

- primeiros passos e listas em Python
- gest�o de ambiente virtual com Pipenv
- acesso a banco de dados SQLite com Python
- preven��o de SQL Injection
- transa��es e rollback

## Estrutura

- `01_boas_praticas.py` � pr�tica inicial com listas e exerc�cios b�sicos
- `01 - Ambiente virtual/Pipfile` � configura��o do ambiente virtual
- `bancoDeDados/01_dbapi.py` � acesso ao SQLite via DB-API
- `bancoDeDados/02_injecao_sql.py` � exemplo de vulnerabilidade e corre��o
- `bancoDeDados/03_transacao.py` � controle de transa��es com commit e rollback

## Como executar

```bash
python 01_boas_praticas.py
python bancoDeDados/01_dbapi.py
```

## Modulo 2: Desenvolvimento de APIs com Flask

O projeto em `2 modulo_desenvolvimento_api_com_flask/` implementa uma API Flask
com SQLAlchemy, Flask-Migrate, JWT, roles de usuario e testes unitarios e de
integracao.

### Executar a API

```powershell
cd "2 modulo_desenvolvimento_api_com_flask"
poetry install
$env:PYTHONPATH = (Get-Location).Path
poetry run flask --app src.app run --debug
```

### Executar os testes

```powershell
poetry run pytest -vv
```

O banco SQLite, ambientes virtuais e caches locais nao sao versionados.
