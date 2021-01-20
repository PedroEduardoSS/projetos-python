m = [[0, 0], [0, 0]]
for l in range(0, 2):
    for c in range(0, 2):
        m[l][c] = int(input(f'Digite um valor para [{l}, {c}]:'))

for l in range(0, 2):
    for c in range(0, 2):
        print(f'[{m[l][c]:^5}]', end='')
    print()
calculo = m[0][0] * m[1][1] + m[0][1] * m[1][0]
print(f'O cálculo da matriz foi {calculo}.')