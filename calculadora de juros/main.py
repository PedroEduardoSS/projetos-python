from dearpygui.core import *
from dearpygui.simple import *

class Juros:
    def __init__(self, C, i, t):
        self.capital = C
        self.taxa = i
        self.tempo = t

    def simples(self):
        self.juros_total = self.capital * self.taxa * self.tempo
        self.montante = self.capital + self.juros_total
        with window("Resultado", x_pos=0, y_pos=200, width=330, height=300, no_close=True, no_collapse=True, no_resize=True):
            add_text(f"Capital: {round(self.capital, 2)}")
            add_text(f"Taxa mensal: {round(self.taxa, 2)}")
            add_text(f"Tempo (meses): {round(self.tempo)}")
            add_text(f"Juros: {round(self.juros_total, 2)}")
            add_text(f"Montante: {round(self.montante, 2)}")
            add_button("Close Window", callback=lambda:delete_item("Resultado"))            

    def compostos(self):
        self.montante = self.capital * ((1 + self.taxa)**self.tempo)
        self.juros_total = self.montante - self.capital
        with window("Resultado", x_pos=0, y_pos=200, width=330, height=300, no_close=True, no_collapse=True, no_resize=True):
            add_text(f"Capital: {round(self.capital, 2)}")
            add_text(f"Taxa mensal: {round(self.taxa, 2)}")
            add_text(f"Tempo (meses): {round(self.tempo)}")
            add_text(f"Juros: {round(self.juros_total, 2)}")
            add_text(f"Montante: {round(self.montante, 2)}")
            add_button("Close Window", callback=lambda:delete_item("Resultado"))

set_main_window_size(350, 500)
set_main_window_title("Calculadora de Juros")

def mostrar(sender, data):
    dados = get_value("##Dados")
    capital = round(dados[0], 2)
    taxa = round(dados[1], 2)
    tempo = round(dados[2], 2)
    montante = Juros(capital, taxa, tempo)
    tipo_juros = get_value("Opção de juros")
    if tipo_juros == 0:
        montante.simples()
    else:
        montante.compostos()

with window("##calculadora de juros", x_pos=1, y_pos=0, width=330, height=200, no_close=True, no_collapse=True, no_resize=True):
    add_text("Digite as inforamções pedidas a seguir", bullet=True)
    add_text("Passe o mouse sobre as legendas para\nmais informações", bullet=True)
    add_separator()
    with group("info", horizontal_spacing=22, horizontal=True):
        add_text("Capital", tip="Capital inicial")
        add_text("Taxa %", tip="Coloque a porcentagem mensal")
        add_text("Tempo", tip="Coloque o período em meses")
    add_input_float3("##Dados", format="%.2f", width=200)
    add_radio_button("Opção de juros", items=["Simples", "Compostos"])
    add_button("Calcular", callback=mostrar)

start_dearpygui()