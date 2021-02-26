from dearpygui.core import *
from dearpygui.simple import *
from random import randint

set_main_window_size(400, 500)

def jogar(sender, data):
    items = ('Pedra', 'Papel', 'Tesoura')
    computador = randint(0, 2)
    player = get_value("Objeto")
    if computador == 0:
        if player == 0:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[0]}")
                add_same_line(spacing=50)
                add_text(f"{items[0]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Empate')
        elif player == 1:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[1]}")
                add_same_line(spacing=50)
                add_text(f"{items[0]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Jogador ganhou!')
        else:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[2]}")
                add_same_line(spacing=50)
                add_text(f"{items[0]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Jogador Perdeu')

    elif computador == 1:
        if player == 1:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[1]}")
                add_same_line(spacing=50)
                add_text(f"{items[1]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Empate')
        elif player == 2:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[2]}")
                add_same_line(spacing=50)
                add_text(f"{items[1]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Jogador ganhou!')
        else:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[0]}")
                add_same_line(spacing=50)
                add_text(f"{items[1]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Jogador Perdeu')

    elif computador == 2:
        if player == 2:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[2]}")
                add_same_line(spacing=50)
                add_text(f"{items[2]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Empate')
        elif player == 0:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[0]}")
                add_same_line(spacing=50)
                add_text(f"{items[2]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Jogador ganhou!')
        else:
            with window("Pedra-Papel-Tesoura", width=380, height=450):
                set_window_pos("Pedra-Papel-Tesoura", 0, 0)
                add_same_line(spacing=80)
                add_text("VOCÊ")
                add_same_line(spacing=50)
                add_text("COMPUTADOR")
                add_spacing(count=5)
                add_same_line(spacing=80)
                add_text(f"{items[1]}")
                add_same_line(spacing=50)
                add_text(f"{items[2]}")
                add_spacing(count=5)
                add_same_line(spacing=110)
                add_text('Jogador Perdeu')

    else:
        add_text('Inválido')

def rematch(sender, data):
    delete_item("Pedra-Papel-Tesoura")
    with window("Pedra-Papel-Tesoura", width=380, height=450):
        set_window_pos("Pedra-Papel-Tesoura", 0, 0)
        add_text("Bem-vindo(a) ao jogo Pedra, Papel e Tesoura")
        add_text("No espaço abaixo: ")
        add_text("Digite 0 se quiser PEDRA")
        add_text("Digite 1 se quiser PAPEL")
        add_text("Digite 2 se quiser TESOURA")
        add_input_int("Objeto")
        add_button("Jogar", callback=jogar)
        add_same_line(spacing=10)
        add_button("Jogar novamente", callback=rematch)
        add_spacing(count=5)
    
with window("Pedra-Papel-Tesoura", width=380, height=450):
    set_window_pos("Pedra-Papel-Tesoura", 0, 0)
    add_text("Bem-vindo(a) ao jogo Pedra, Papel e Tesoura")
    add_text("No espaço abaixo: ")
    add_text("Digite 0 se quiser PEDRA")
    add_text("Digite 1 se quiser PAPEL")
    add_text("Digite 2 se quiser TESOURA")
    add_input_int("Objeto")
    add_button("Jogar", callback=jogar)
    add_same_line(spacing=10)
    add_button("Jogar novamente", callback=rematch)
    add_spacing(count=5)

start_dearpygui()