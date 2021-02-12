from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(400, 400)

def callback(sender, data, i):
    with window('To do list'):
        i = get_value('Tarefa')
        add_text(i)

with window('To do list'):
    add_input_text('Tarefa')
    add_button('Adicione', callback=callback)


start_dearpygui(primary_window='To do list')