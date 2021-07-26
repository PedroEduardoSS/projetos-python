def celsius_to_fahrenheit(Celsius):
    F = (Celsius/5)*9 + 32
    return F

def celsius_to_kelvin(Celsius):
    K = Celsius + 273
    return K

def kelvin_to_celsius(Kelvin):
    C = Kelvin - 273
    return C

def kelvin_to_fahrenheit(Kelvin):
    F = (((Kelvin - 273) / 5) * 9) + 32
    return F

def fahrenheit_to_kelvin(Fahrenheit):
    K = (((Fahrenheit - 32) / 9) * 5) + 273
    return K

def fahrenheit_to_celsius(Fahrenheit):
    C = ((Fahrenheit - 32) / 9) * 5
    return C