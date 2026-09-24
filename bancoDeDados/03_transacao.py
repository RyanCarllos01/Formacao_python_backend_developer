import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "cliente.db")
# cursor permite que eu execute comandos SQL
cursor = con.cursor()
# Deixando row_factory como global
cursor.row_factory = sqlite3.Row


try:
    cursor.execute("INSERT INTO cliente (nome, email) VALUES (?,?)", ("Teste 2", "teste2@gmail.com"))
    cursor.execute("INSERT INTO cliente (id, nome, email) VALUES (?,?,?)", (4,"Teste 4", "teste4@gmail.com"))
    cursor.execute("DELETE FROM cliente where id = 6; ")
   # sempre colocar o commit no final, caso dê algum erro nas linhas de cima
    con.commit()
except Exception as exc:
        print (f"Ops! um erro ocorreu! {exc}")
        con.rollback()
