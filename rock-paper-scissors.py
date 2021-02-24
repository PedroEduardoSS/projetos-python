from random import randint
it = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
def jogo():
    print('''Suas opções:
    [0]Pedra
    [1]Papel
    [2]Tesoura''')
    pl = int(input('Qual sua jogada?'))
    print(f'Você escolheu {it[pl]}')
    print(f'O computador escolheu {it[pc]}')
    if pc == 0:
        if pl == 0:
            print('Empate')
        elif pl == 1:
            print('Jogador ganhou!')
        else:
            print('Jogador Perdeu')

    elif pc == 1:
        if pl == 1:
            print('Empate')
        elif pl == 2:
            print('Jogador ganhou!')
        else:
            print('Jogador Perdeu')

    elif pc == 2:
        if pl == 2:
            print('Empate')
        elif pl == 0:
            print('Jogador ganhou!')
        else:
            print('Jogador Perdeu')

    else:
        print('Inválido')

playAgain = 'sim'
while playAgain == 'sim' or playAgain == 's':
    jogo()

    print('Deseja jogar novamente?')
    playAgain = input()
print('GAME OVER!')
