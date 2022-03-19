def f(l):
    rp = 0
    tem = [128, 64, 32, 16, 8, 4, 2, 1]
    for x in range(0, 8):
        if l[x] == 1:
            rp += tem[x]
    return rp

l = []
code  = str(input("Codigo binario: "))
for i in code:
    l.append(int(i))

char = f(l)

print(chr(char))