from collections import defaultdict

def factorize(n):
    factors = defaultdict(int)
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors[2] += 1
        n = n // 2
    
    # n must be odd at this point
    # so we can skip one element (i.e., i = i + 2)
    for i in range(3, int(n**0.5) + 1, 2):
        # while i divides n, add i and divide n
        while n % i == 0:
            factors[i] += 1
            n = n // i
    
    # This condition is to check if n is a prime number
    # greater than 2
    if n > 2:
        factors[n] += 1
    
    return factors    

# The idea is that x and y on the left would always be greater than n, so represent them as n + a and n + b
# The equation would then reduct to n**2 = a*b
# Then just find number of factors of n**2 that are less than or equal to n


curr = 2
required_solutions = 1000

while True:
    solutions = 0
    factors = factorize(curr)
    sq_factors = 1
    for k, v in factors.items():
        sq_factors = sq_factors * (2*v+1) 
    # print(curr, sq_factors)
    solutions = sq_factors // 2 + 1

    if solutions >= required_solutions:
        print(f"Found: {curr} {solutions}")
        break
    
    curr += 1

