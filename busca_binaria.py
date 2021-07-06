min_num = 1
max_num = 101

numbers = [number for number in range(min_num, max_num)]

def change_max_num(list):
    busca = round(len(list) / 2)
    num_medio = list[busca]
    return num_medio

def change_min_num(list):
    busca = round(len(list) / 2)
    num_medio = list[busca]
    return num_medio


def busca(min_num, max_num):
    numbers = [number for number in range(min_num, max_num)]
    print(numbers)
    return numbers

loop = True
print("Vou adivinhar o número em que está pensando!")
usuario = str(input(f"Seu número é maior (>) ou menor (<) que {round(max_num / 2)}? "))
while loop:
    if usuario == "<":
        max_num = change_max_num(numbers)
        numbers = busca(min_num, max_num)
        usuario = str(input(f"Seu número é maior (>) ou menor (<) que {numbers[round(len(numbers) / 2)]}? "))
        
    elif usuario == ">":
        min_num = change_min_num(numbers)
        numbers = busca(min_num, max_num)
        usuario = str(input(f"Seu número é maior (>) ou menor (<) que {numbers[round(len(numbers) / 2)]}? "))
    
    elif usuario == "=":
        print(f"Seu número é igual {numbers[round(len(numbers) / 2)]}")
        loop = False
    else:
        print("Erro")
    