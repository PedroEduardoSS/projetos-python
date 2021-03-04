from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(400, 400)
index = ['None']
def callback(sender, data, i):
    with window('Lista de Tarefas'):
        i = get_value('Tarefa')
        t = get_value('Tarefa')
        index.append(i)
        add_text(f"{index.index(i)} {t}")

def clear(sender, data):
    delete_item('Lista de Tarefas')
    index.pop()
    with window('Lista de Tarefas', width=400, height=400):
        set_window_pos('Lista de Tarefas', 0, 0)
        add_input_text('Tarefa')
        add_button('Adicione', callback=callback)
        add_button('Limpar', callback=clear)

with window('Lista de Tarefas', width=400, height=400):
    set_window_pos('Lista de Tarefas', 0, 0)
    add_input_text('Tarefa')
    add_button('Adicione', callback=callback)
    add_button('Limpar', callback=clear)


start_dearpygui()