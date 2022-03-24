n = int(input("Digite um número: "))

for i in range(1, n+2, 2):
    e = "*" * i
    print(e.center(n))
print("*".center(n))
print("***".center(n))