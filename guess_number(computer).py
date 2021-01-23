from random import randint

def guess_number():
    low_number = 1
    high_number = 10
    guess = randint(low_number, high_number)
    print(guess)
    hint = input("Are I right? if not, more(m) or less(l) (c for correct)")
    while guess != "c":
        if low_number != high_number:
            guess = randint(low_number, high_number)
        else:
            guess = low_number
        if hint == "m":
            high_number = guess - 1
            guess_number()
        elif hint == "l":
            low_number = guess + 1
            guess_number()
    print("Yeah, You're correct!")
            
guess_number()