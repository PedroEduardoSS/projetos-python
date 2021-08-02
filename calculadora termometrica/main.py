from dearpygui.dearpygui import *
from functions import *

setup_viewport()
set_viewport_title(title='termocalc')
set_viewport_width(200)
set_viewport_height(500)

conversoes = ["Celsius para Fahrenheit", "Celsius para Kelvin", "Fahrenheit para Celsius", "Fahrenheit para Kelvin", "Kelvin para Celsius", "Kelvin para Fahrenheit"]

def converter():
    temperatura = get_value(valor)
    item = get_value(items)
    if item == "Celsius para Fahrenheit":
        result = celsius_to_fahrenheit(temperatura)
        configure_item(resultado, default_value=f"Resultado: {round(result, 2)}°F")
    elif item == "Celsius para Kelvin":
        result = celsius_to_kelvin(temperatura)
        configure_item(resultado, default_value=f"Resultado: {round(result, 2)}K")
    elif item == "Fahrenheit para Celsius":
        result = fahrenheit_to_celsius(temperatura)
        configure_item(resultado, default_value=f"Resultado: {round(result, 2)}°C")
    elif item == "Fahrenheit para Kelvin":
        result = fahrenheit_to_kelvin(temperatura)
        configure_item(resultado, default_value=f"Resultado: {round(result, 2)}K")
    elif item == "Kelvin para Celsius":
        result = kelvin_to_celsius(temperatura)
        configure_item(resultado, default_value=f"Resultado: {round(result, 2)}°C")
    elif item == "Kelvin para Fahrenheit":
        result = kelvin_to_fahrenheit(temperatura)
        configure_item(resultado, default_value=f"Resultado: {round(result, 2)}°F")

with window(label="TermoCalc", width=250, height=400):
    add_text("Escolha a conversão", bullet=True)
    add_separator()
    valor = add_input_int(min_value=-10000, max_value=10000)
    items = add_radio_button(items=conversoes)
    add_button(label="Converter", callback=converter)
    resultado = add_text("")

start_dearpygui()