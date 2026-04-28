import cmath


def solve(a, b, c):
    if a == 0:
        raise ValueError("Коэффициент a не может быть равен нулю")

    discriminant = b**2 - 4 * a * c
    x1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return x1, x2