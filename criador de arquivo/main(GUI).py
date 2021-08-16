from dearpygui.dearpygui import *

import os

def create():
    file_name = str(get_value(name))
    file_extension = str(get_value(extension))
    file = open(f"{file_name}{file_extension}", "x")

def write():
    file_name = str(get_value(name))
    file_extension = str(get_value(extension))
    file_content = str(get_value(content_file))
    with open(f"{file_name}{file_extension}", "w") as file:
        content = file.write(file_content)

def append():
    file_name = str(get_value(name))
    file_extension = str(get_value(extension))
    file_content = str(get_value(content_file))
    with open(f"{file_name}{file_extension}", "a") as file:
        content = file.write(file_content)

def read():
    file_name = str(get_value(name))
    file_extension = str(get_value(extension))
    with open(f"{file_name}{file_extension}", "r") as file:
        read_file = file.read()
        with window(label="Output file"):
            output = add_text(f"{read_file}")

def delete():
    file_name = str(get_value(name))
    file_extension = str(get_value(extension))
    if os.path.exists(f"{file_name}{file_extension}"):
        os.remove(f"{file_name}{file_extension}")
    else:
        print("The file does not exist")

with window(label="Criador de arquivo"):
    add_text("File items:", bullet=True)
    with group(label="Row0", horizontal=True):
        add_text("File name: ")
        name = add_input_text(label="##file_name")
    with group(label="Row1", horizontal=True):
        add_text("File extension: ")
        extension = add_input_text(label="##file_extension")
    with group(label="Row2", horizontal=True):
        add_text("File content: ")
        content_file = add_input_text(label="##file_content", multiline=True)
    add_separator()
    add_text("Select the command:\n[X] = Create\n[W] = Write\n[A] = Append\n[R] = Read\n[D] = Delete")
    with group(label="file commands", horizontal=True):
        add_button(label="X", callback=create)
        add_button(label="W", callback=write)
        add_button(label="A", callback=append)
        add_button(label="R", callback=read)
        add_button(label="D", callback=delete)


start_dearpygui()