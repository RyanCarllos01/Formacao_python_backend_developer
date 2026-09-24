import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "cliente.db")
# cursor permite que eu execute comandos SQL
cursor = con.cursor()
# Deixando row_factory como global
cursor.row_factory = sqlite3.Row


# Esse def serve para quando for chamar a ação chamar pelo nome no caso
# criar_tabela
def criar_tabela(cursor):
    # para executar comandos SQL, se utiliza o método execute do cursor
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS cliente (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    con.commit()


def inserir_registro(con, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO cliente (nome, email) VALUES (? , ?)", data)
    # Precisa commitar com o conn.commit(), para subir a inserção no banco de dados
    con.commit()


def atualizar_registro(con, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE cliente SET nome=?, email=? WHERE id=?;", data)
    con.commit()


def excluir_registro(con, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM cliente WHERE id=?;", data)
    con.commit()

def inserir_muitos(con, cursor, dados):
    cursor.executemany("INSERT INTO cliente (nome, email) VALUES (?,?)", dados)
    con.commit()
    
# Inserindo consulta fetchone(busca uma linha)
def recuperar_cliente(cursor, id):
  
    cursor.execute('SELECT * FROM cliente where id=?', (id,))
    return cursor.fetchone()

# cliente = recuperar_cliente(cursor, 1)
# print (dict(cliente))
   
def listar_clientes(cursor):
   
    return cursor.execute("SELECT * FROM cliente ORDER BY nome ASC")

cliente = listar_clientes(cursor)
for cliente in cliente:
    print (dict(cliente))
    

cliente = recuperar_cliente(cursor, 2)
print(dict(cliente))

# esse print abaixo é possível graças ao row_factory
# É menos sujeito a erros
print (f'Seja bem vindo ao sistema {cliente["nome"]}')

# dados = [
#     ("Ana", "anajulia@gmail.com"),
#     ("Shirlene", "Shirlene@gmail.com"),
#     ("Wellington", "Shirlene@gmail.com"),
# ]
# inserir_muitos(con, cursor, dados)
#excluir_registro(con, cursor, 1)
#criar_tabela(cursor)
#inserir_registro(con, cursor, "Ryan", "ryancarllos.negro@gmail.com.br")

#atualizar_registro(con, cursor, "Ryan", "ryancarllos.jac@gmail.com.br", 1)
#atualizar_registro(con, cursor, "basquete", "basquete.jac@gmail.com.br", 2)
