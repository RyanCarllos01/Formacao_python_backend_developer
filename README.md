# Formação Python Backend Developer
 
Este repositório reúne exercícios e práticas de Python para formação em desenvolvimento backend, com foco nos seguintes temas:
 
- Primeiros passos com Python e manipulação de listas
- Gestão de ambientes virtuais com Pipenv
- Acesso a banco de dados SQLite com Python
- Prevenção de SQL Injection
- Controle de transações com commit e rollback
 
## Estrutura do Projeto
 
### Módulo 1: Fundamentos de Python e Banco de Dados
 
- `01_boas_praticas.py`
Exercícios iniciais com listas e conceitos básicos da linguagem.
 
- `01 - Ambiente virtual/Pipfile`
Configuração e gerenciamento do ambiente virtual utilizando Pipenv.
 
- `bancoDeDados/01_dbapi.py`
Exemplo de acesso ao SQLite utilizando a API padrão de banco de dados do Python (DB-API).
 
- `bancoDeDados/02_injecao_sql.py`
Demonstração de vulnerabilidade a SQL Injection e sua correção utilizando consultas parametrizadas.
 
- `bancoDeDados/03_transacao.py`
Exemplo de controle de transações utilizando `commit` e `rollback`.
 
## Como Executar
 
```bash
python 01_boas_praticas.py
python bancoDeDados/01_dbapi.py
```
 
---
 
## Módulo 2: Desenvolvimento de APIs com Flask
 
O projeto localizado em `2 modulo_desenvolvimento_api_com_flask/` implementa uma API REST utilizando:
 
- Flask
- SQLAlchemy
- Flask-Migrate
- JWT (JSON Web Token)
- Controle de permissões por perfil (roles)
- Testes unitários
- Testes de integração
 
### Executar a API
 
```powershell
cd "2 modulo_desenvolvimento_api_com_flask"
 
poetry install
 
$env:PYTHONPATH = (Get-Location).Path
 
poetry run flask --app src.app run --debug
```
 
### Executar os Testes
 
```powershell
poetry run pytest -vv
```
 
## Observações
 
Arquivos locais e gerados automaticamente não são versionados, incluindo:
 
- Banco de dados SQLite
- Ambientes virtuais
- Arquivos de cache
- Diretórios temporários
 
## Objetivo
 
Este repositório tem como objetivo consolidar conhecimentos em Python para desenvolvimento backend, abordando desde conceitos fundamentais da linguagem até a construção de APIs robustas com Flask e boas práticas de desenvolvimento.
