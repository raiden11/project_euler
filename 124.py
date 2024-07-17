from collections import defaultdict

def factorize(n):
    factors = set()
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors.add(2)
        n = n // 2
    
    # n must be odd at this point
    # so we can skip one element (i.e., i = i + 2)
    for i in range(3, int(n**0.5) + 1, 2):
        # while i divides n, add i and divide n
        while n % i == 0:
            factors.add(i)
            n = n // i
    
    # This condition is to check if n is a prime number
    # greater than 2
    if n > 2:
        factors.add(n)
    
    return factors    

limit = 100000
rad_dict = []
for i in range(1, limit + 1):
    factors = factorize(i)
    rad = 1
    for factor in factors:
        rad *= factor
    rad_dict.append((rad, i))

rad_dict = sorted(rad_dict)
print(rad_dict[10000-1][1])

