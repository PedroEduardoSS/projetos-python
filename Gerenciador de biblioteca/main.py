from dearpygui.core import *
from dearpygui.simple import *
from functions import *

set_main_window_pos(2, 2)
set_main_window_size(1300, 900)
set_main_window_title("Gerenciador da biblioteca")

with window("Gerenciar Clientes", width=600, height=500, x_pos=1, y_pos=1, no_close=True):
    with group("clientes-row-1", horizontal=True):
        add_text("Nome: ")
        add_input_text("##nome")

    with group("clientes-row-2", horizontal=True):
        add_text("Sexo: ")
        add_input_text("##sexo")
    
    add_button("Adicionar cliente", callback=adicionar_cliente)
    add_separator()
    with group("clientes-row-3", horizontal=True):
        add_text("ID do cliente")
        add_input_int("##cliente_id")
    
    add_button("Excluir cliente", callback=excluir_cliente)
    add_separator()
    add_button("Mostrar dados ##clientes", callback=ler_clientes)
    add_table("tabela-clientes", ["Cliente ID", "Clientes", "Sexo"])

with window("Gerenciar livros", width=600, height=500, x_pos=650, y_pos=1, no_close=True):
    with group("livros-row-1", horizontal=True):
        add_text("Livro: ")
        add_input_text("##livro")

    with group("livros-row-2", horizontal=True):
        add_text("Gênero:")
        add_input_text("##genero")

    with group("livros-row-3", horizontal=True):
        add_text("Autor: ")
        add_input_text("##autor")

    add_button("Adicionar livro", callback=adicionar_livro)
    add_separator()
    with group("livros-row-4", horizontal=True):
        add_text("ID do livro")
        add_input_int("##livro_id")
    
    add_button("Excluir livro", callback=excluir_livro)
    add_separator()
    add_button("Mostrar dados ##livros", callback=ler_livros)
    add_table("tabela-livros", ["Livro ID", "Livros","Gênero","Autor"])

with window("Registros", width=1250, height=600, x_pos=1, y_pos=500, no_close=True):
    with group("registros-row-1"):
        add_text("ID do cliente:")
        add_input_int("##cliente-id")

    with group("registros-row-2"):
        add_text("ID do livro:  ")
        add_input_int("##livro-id")

    add_button("Adicionar registro", callback=adicionar_registro)
    add_separator()
    add_button("Mostrar dados ##registros", callback=ler_registros)
    add_table("tabela-registros", ["Cliente","Livro"])

start_dearpygui()