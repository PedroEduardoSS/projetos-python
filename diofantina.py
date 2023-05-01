def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclidean(b, a % b)
        return d, y, x - (a // b) * y

def linear_diophantine(a, b, c):
    d, x, y = extended_euclidean(a, b)
    if c % d == 0:
        x0, y0 = x * (c // d), y * (c // d)
        return x0, y0
    else:
        return None

a, b, c = 23, 71, 1729
solution = linear_diophantine(a, b, c)

if solution:
    x, y = solution
    print(f"Solution: x = {x}, y = {y}")
else:
    print("No solution")
