from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(500, 500)

def adicionar(sender, data):
    c1 = get_value("Tarefa")
    c2 = get_value("Data")
    c3 = get_value("Hora")
    c4 = get_value("Status")
    if c4 == 0:
        c4 = "Não Feito"
    else:
        c4 = "Feito"
    add_row("Tarefas", [c1,c2,c3,c4])
    
def limpar(sender, data):
    row_to_delete = get_value("Linha")
    delete_row("Tarefas", row_to_delete)

with window("Lista de Tarefas", width=495, height=500):

    set_window_pos("Lista de Tarefas", 0, 0)
    add_text("Bem-vindo(a)!", bullet=True)
    add_text("Organize seu tempo aqui!", bullet=True)
    add_text("Status: 0 = Não feito, 1 = Feito", bullet=True)
    
    add_separator()

    add_input_text("Tarefa", width=150)
    add_same_line()
    add_input_text("Data", width=150)

    add_input_int("Status", width=150, max_value=1)
    add_same_line()
    add_input_text("Hora", width=150)

    add_input_int("Linha", tip="Índice da linha que deseja excluir")
    add_button("Adicione", callback=adicionar)
    add_same_line()
    add_button("Limpar", callback=limpar)
    add_table("Tarefas", ["Tarefa", "Data", "Hora", "Status"])

start_dearpygui()