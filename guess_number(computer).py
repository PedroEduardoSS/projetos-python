from random import randint

def guess_number():
    low_number = 1
    high_number = 10
    hint = ''
    while hint != "c":
        if low_number != high_number:
            guess = randint(low_number, high_number)
        else:
            guess = low_number
        hint = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if hint == "h":
            high_number = guess - 1
            guess_number()
        elif hint == "l":
            low_number = guess + 1
            guess_number()
    print("Yeah, You're correct!")
            
guess_number()