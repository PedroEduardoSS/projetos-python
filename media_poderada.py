print("Calcule a media ponderada")
n_casos = int(input("Numero de casos (elementos e pesos):"))

elementos = list()
pesos = list()

m1 = 0
m2 = 0

print("Digite os elementos")
for n in range(0, n_casos):
    e = int(input())
    elementos.append(e)

print("Digite os pesos")
for n in range(0, n_casos):
    e = int(input())
    pesos.append(e)
    
for i in range(0, 3):
    m1 += elementos[i]*pesos[i]
    m2 += pesos[i]
    
media = m1/m2
print(media)