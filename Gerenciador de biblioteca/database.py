import sqlite3

class database:
    def insert_clientes(self, clienteNome, clienteSexo):
        #conexão com o banco de dados
        con = sqlite3.connect("biblioteca.db")
        #cursor
        c = con.cursor()
        c.execute(f"INSERT INTO clientes (clienteNome, clienteSexo) VALUES('{clienteNome}','{clienteSexo}')")
        con.commit()
        con.close()

    def delete_clientes(self, clienteID):
        #conexão com o banco de dados
        con = sqlite3.connect("biblioteca.db")
        #cursor
        c = con.cursor()
        c.execute(f"DELETE FROM clientes WHERE clienteID = {clienteID}")
        con.commit()
        con.close()

    def select_clientes(self, list):
        #conexão com o banco de dados
        con = sqlite3.connect("biblioteca.db")
        #cursor
        c = con.cursor()
        c.execute(f"SELECT * FROM clientes")
        rows = c.fetchall()
        for row in rows:
            list.append(row)
        con.commit()
        con.close()

    def insert_livros(self, livroNome, livroGenero, livroAutor):
        #conexão com o banco de dados
        con = sqlite3.connect("biblioteca.db")
        #cursor
        c = con.cursor()
        c.execute(f"INSERT INTO livros (livroNome, livroGenero, livroAutor) VALUES('{livroNome}','{livroGenero}','{livroAutor}')")
        con.commit()
        con.close()

    def delete_livros(self, livroID):
        #conexão com o banco de dados
        con = sqlite3.connect("biblioteca.db")
        #cursor
        c = con.cursor()
        c.execute(f"DELETE FROM livros WHERE livroID = {livroID}")
        con.commit()
        con.close()

    def select_livros(self, list):
        #conexão com o banco de dados
        con = sqlite3.connect("biblioteca.db")
        #cursor
        c = con.cursor()
        c.execute("SELECT * FROM livros")
        rows = c.fetchall()
        for row in rows:
            list.append(row)
        con.commit()
        con.close()

    def insert_registros(self, clienteId, livroId):
        #conexão com o banco de dados
        con = sqlite3.connect("biblioteca.db")
        #cursor
        c = con.cursor()
        c.execute(f"INSERT INTO registros (clienteID, livroID) VALUES('{clienteId}','{livroId}')")
        con.commit()
        con.close()

    def select_registros(self, list):
        #conexão com o banco de dados
        con = sqlite3.connect("biblioteca.db")
        #cursor
        c = con.cursor()
        c.execute('''SELECT clientes.clienteNome, livros.livroNome
                    FROM clientes JOIN livros JOIN registros 
                    ON registros.clienteID = clientes.clienteID AND
                    registros.livroID = livros.livroID
                    ORDER BY clientes.clienteNome, livros.livroNome''')
        rows = c.fetchall()
        for row in rows:
            list.append(row)
        con.commit()
        con.close()