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

# Since our solution is sol = factors // 2 + 1, and we need sol to exceed 4 million, find a number above 8 million, let's say x
# prime factors for x would be 2*v + 1 of powers of prime factors of our required number n
# Thus, the goal is to minimize n, not x
# I used hit and trial to find the factors of n such that n is minimized but the solutions are still above 4,000,000


numb = 2*2*2*3*3*3*5*5*7*7*11*13*17*19*23*29*31*37
factors = factorize(numb)
print(factors)
sq_factors = 1
for k, v in factors.items():
    sq_factors = sq_factors * (2*v+1) 
    # print(curr, sq_factors)
    solutions = sq_factors // 2 + 1

print(numb, solutions)


# Answer = numb : 9350130049860600

