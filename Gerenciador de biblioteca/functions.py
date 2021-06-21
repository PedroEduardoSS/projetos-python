from dearpygui.core import *
from dearpygui.simple import *
from database import database

banco_de_dados = database()

def adicionar_cliente(sender, data):
    cliente_nome = get_value("##nome")
    cliente_sexo = get_value("##sexo")
    banco_de_dados.insert_clientes(cliente_nome, cliente_sexo)

def excluir_cliente(sender, data):
    cliente_id = get_value("##cliente_id")
    banco_de_dados.delete_clientes(cliente_id)

def ler_clientes(sender, data):
    data_in_table = get_table_data("tabela-clientes")
    if data_in_table == []:
        pass
    else:
        clear_table("tabela-clientes")
    table_data = []
    banco_de_dados.select_clientes(table_data)
    for data in table_data:
        add_row("tabela-clientes", data)

def adicionar_livro(sender, data):
    livro_nome = get_value("##livro")
    livro_genero = get_value("##genero")
    livro_autor = get_value("##autor")
    banco_de_dados.insert_livros(livro_nome, livro_genero, livro_autor)

def excluir_livro(sender, data):
    livro_id = get_value("##livro_id")
    banco_de_dados.delete_livros(livro_id)

def ler_livros(sender, data):
    data_in_table = get_table_data("tabela-livros")
    if data_in_table == []:
        pass
    else:
        clear_table("tabela-livros")
    table_data = []
    banco_de_dados.select_livros(table_data)
    for data in table_data:
        add_row("tabela-livros", data)

def adicionar_registro(sender, data):
    cliente_id = get_value("##cliente-id")
    livro_id = get_value("##livro-id")
    banco_de_dados.insert_registros(cliente_id, livro_id)

def ler_registros(sender, data):
    data_in_table = get_table_data("tabela-registros")
    if data_in_table == []:
        pass
    else:
        clear_table("tabela-registros")
    table_data = []
    banco_de_dados.select_registros(table_data)
    for data in table_data:
        add_row("tabela-registros", data)