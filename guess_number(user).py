from random import randint

number = randint(1, 10)

class guess_number():
    def __init__(self):
        self.user = int(input("Guess a number:"))
        print(self.user)

    def round(self):
        if self.user < number:
            print("NO, too low")
            r = input("Do you wanna play again?(y/n)")
            if r == "y":
                player = guess_number()
                player.round()
        elif self.user > number:
            print("NO, too high")
            r = input("Do you wanna play again?(y/n)")
            if r == "y":
                player = guess_number()
                player.round()
        else:
            print("You're a Genius")
    
player = guess_number()
player.round()