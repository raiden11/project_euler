

def extended_gcd(a, b):
    """ 
    Extended Euclidean Algorithm.
    It returns gcd(a, b) and coefficients x, y such that ax + by = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def solve_diophantine(a, b, c):
    """
    Solves ax + by = c using the extended Euclidean algorithm.
    Returns a particular solution (x, y) if it exists, otherwise raises an error.
    """
    gcd, x, y = extended_gcd(a, b)
    if c % gcd != 0:
        raise ValueError("No solution exists")
    x *= c // gcd
    y *= c // gcd
    return x, y

# Other solutions to the equation could be found by x + k*(b/gcd) and y - k*(a/gcd), where k is an integer
try:
    a = 18
    b = -22
    c = 8
    x, y = solve_diophantine(a, b, c)
    print(f"One solution to {a}x + {b}y = {c} is x = {x}, y = {y}")
except ValueError as e:
    print(e)

