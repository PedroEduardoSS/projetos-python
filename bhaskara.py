from math import sqrt

def bhaskara(a, b, c):
    arg1 = f"{a}x²"
    if a == 1:
        arg1 = "x²"
    
    arg2 = f"+ {b}"
    if b < 0:
        arg2 = f"{b}"

    arg3 = f"+ {c}"
    if c < 0:
        arg3 = f"{c}"

    equation = f"{arg1} {arg2}x {arg3} = 0"

    x1 = (- b + sqrt((b ** 2) - 4 * a * c)) / (2 * a)
    x2 = (- b - sqrt((b ** 2) - 4 * a * c)) / (2 * a)

    resultado = f"Equação: {equation}\nRaízes da equação:\nx1 = {x1}, x2 = {x2}\n"
    
    print(resultado)

#bhaskara(1, 8, -9)
#bhaskara(4, 2, -6)
bhaskara(1, -5, 6)