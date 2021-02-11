import random as rd
user = int(input("Qual tipo de senha? \n 4 = 4 digitos(somente números), \n 6 = 6 digitos, \n 8 = 8 digitos \n tipo:"))

password = []


def tipo_4():
    for i in range(0, 4):
        i = rd.choice(['1','2','3','4','5','6','7','8','9','0'])
        password.append(i)

def tipo_6():
    for i in range(0, 6):
        i = rd.choice(['1','2','3','4','5','6','7','8','9','0',
                        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                        'p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','&','*','?'])
        password.append(i)
        
def tipo_8():
    for i in range(0, 8):
        i = rd.choice(['1','2','3','4','5','6','7','8','9','0',
                        'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                        'p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','&','*','?'])
        password.append(i)
               
if user == 4:
    tipo_4()
elif user == 6:
    tipo_6()
elif user == 8:
    tipo_8()
else:
    print("Erro")
print(password)