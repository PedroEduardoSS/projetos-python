def square():
    a = int(input("Area: "))
    b = int(input("Base: "))
    area = b * a
    print(area)

def triangle():
    a = int(input("Area: "))
    b = int(input("Base: "))
    area = (b * a)/2
    print(area)

def trapeze():
    b1 = int(input("Base maior: "))
    b2 = int(input("Base menor: "))
    a = int(input("Altura: "))
    area = ((b1 + b2) * a)/2
    print(area)

def regular_polygons():
    n = int(input("Número de lados: "))
    n_measure = int(input("Medida dos lados: "))
    a = int(input("Apótema: "))
    p = n * n_measure
    area = (p * a)/2
    print(area)