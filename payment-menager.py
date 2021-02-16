from dearpygui.core import *
from dearpygui.simple import *

set_main_window_size(600, 600)

def callback(sender, data):
    with window("Gerenciador de pagamento"):
        valor = get_value("Preço das compras")
        item = get_value("Opções")
        parc = get_value("Parcelas")
        if item == 0:
            total = valor - (valor * 20/100)
            add_text(f"Valor das compras: R${valor}")
            add_text("Forma de pagamento: à vista no dinheiro/cheque")
            add_text("Desconto: 20%")
            add_text(f"Total:{total}")
        
        elif item == 1:
            total = valor - (valor * 5/100)
            add_text(f"Valor das compras: R${valor}")
            add_text("Forma de pagamento: à vista no cartão")
            add_text("Desconto: 5%")
            add_text(f"Total:{total}")
        
        elif item == 2:
            total = valor/2
            add_text(f"Valor das compras: R${valor}")
            add_text("Forma de pagamento: 2x no cartão")
            add_text(f"Preço das parcelas: {total}")
            add_text(f"Total:{valor}")
        
        elif item == 3:
            total = valor + (valor * 10/100)
            valor_parcelado = total/parc
            add_text(f"Valor das compras: R${valor}")
            add_text(f"Forma de pagamento: {parc}x no cartão")
            add_text("Juros: 10%")
            add_text(f"Preço das parcelas: {valor_parcelado}")
            add_text(f"Total:{total}")

        add_text(f"Obrigado pelas compras! Volte sempre")

def clear(sender, data):
    delete_item("Gerenciador de pagamento")
    with window("Gerenciador de pagamento", width=600, height=600):
        set_window_pos("Gerenciador de pagamento", 0, 0)
        add_input_float("Preço das compras", format='%.2f')
        add_text("Escolha uma opção de pagamento:")
        add_radio_button("Opções", items=["à vista no dinheiro/cheque", "à vista no cartão", "2x no cartão", "3x ou mais parcelas"])
        add_text("Total de parcelas (se houver):")
        add_input_int("Parcelas")
        add_button("Calcular", callback=callback)
        add_button("Limpar", callback=clear)

with window("Gerenciador de pagamento", width=600, height=600):
    set_window_pos("Gerenciador de pagamento", 0, 0)
    add_input_float("Preço das compras", format='%.2f')
    add_text("Escolha uma opção de pagamento:")
    add_radio_button("Opções", items=["à vista no dinheiro/cheque", "à vista no cartão", "2x no cartão", "3x ou mais parcelas"])
    add_text("Total de parcelas (se houver):")
    add_input_int("Parcelas")
    add_button("Calcular", callback=callback)
    add_button("Limpar", callback=clear)


start_dearpygui()