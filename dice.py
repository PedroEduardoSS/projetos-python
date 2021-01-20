from random import randint

class dice():
    def dice4(self):
        self.d4 = randint(1, 4)
        print(self.d4)
    def dice6(self):
        self.d6 = randint(1, 6)
        print(self.d6)
    def dice8(self):
        self.d8 = randint(1, 8)
        print(self.d8)
    def dice10(self):
        self.d10 = randint(1, 10)
        print(self.d10)
    def dice12(self):
        self.d12 = randint(1, 12)
        print(self.d12)
    def dice20(self):
        self.d20 = randint(1, 20)
        print(self.d20)

def game():
    player = int(input("Digite um número:"))
    d = dice()    
    if player == 4:
        d.dice4()
    elif player == 6:
        d.dice6()
    elif player == 8:
        d.dice8()
    elif player == 10:
        d.dice10()
    elif player == 12:
        d.dice12()
    elif player == 20:
        d.dice20()
    else:
        print("ERROR!")

game()

replay = input("(r)")
if replay == "r":
    game()
    replay = input("(r)")
print("GAME OVER!")