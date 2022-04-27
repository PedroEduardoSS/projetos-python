import random

n = int(input("N: "))

m = []
for i in range(0, n):
    x = random.random()
    y = random.random()
    c = (x - 1/2)**2 + (y - 1/2)**2
    if c <= 0.25:
        m.append(c)

res = 4 * len(m)
print(res)
print("pi ~= " + str(res/n))
