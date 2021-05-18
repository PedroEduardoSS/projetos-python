from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(400, 400)

def create(sender, data):
    text = get_value("Your text")
    with open("file.txt", "w") as file:
        file.write(text)

with window("File Creator", x_pos=0, y_pos=0, width=400, height=400):
    add_input_text("Your text", multiline=True)
    add_button("Create", callback=create)

start_dearpygui()