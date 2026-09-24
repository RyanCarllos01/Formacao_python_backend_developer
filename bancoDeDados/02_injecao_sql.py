# arquivo com vulnerabilidade para ser atacado com injeção sql
# nos inputs podemos inserir comandos sql por conta do {id_cliente}

import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "cliente.db")
# cursor permite que eu execute comandos SQL
cursor = con.cursor()
# Deixando row_factory como global
cursor.row_factory = sqlite3.Row

id_cliente = input("Informe o id do cliente")
#metodo com falha
# cursor.execute(f"SELECT * FROM cliente WHERE id={id_cliente}")

#metodo corrigido
cursor.execute(f"SELECT * FROM cliente WHERE id=?", (id_cliente))
clientes = cursor.fetchall()


for cliente in clientes:
    print(dict(cliente))