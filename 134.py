
import math
import numpy as np
from number_theory.solve_linear_two_unknowns_diophantine import solve_diophantine

# Logic 
# The number that ends with p1 could be expressed as (10^k)*(x) + p1 where k is the number of digits in p1. It will always end with p1
# Since it is divisible by p2, (10^k)*(x) must leave remainder (p2-p1) modulo p2 so that the remainder becomes 0 when p1 is added 
# Hence, (10^k)*(x) - (p2)*(y) = (p2-p1) for some y. 
# This is same as solving diophantine ax + by = c where a = (10^k), b = -(p2) and c = p2-p1, where p1 and p2 are consecutive primes
# Also, gcd(a, b) = 1 as p2 is prime and p2-p1 will be divisible by 1, so there is always a solution for this equation
# As per Euclied's algo, for a solution (x, y), all possible solutions are (x + k*(b/g), x - k*(a/g)) for all integers k
# Since our number (10^k)*(x) - (p2)*(y) is always positive and minimum possible, x has to be positive and minimum possible (Note that RHS is always positive for every solution)
# Hence, we use that x1 = x + k*(b/g) >= 0 and g = 1. So, k*b >= -x and since b is always negative, k <= (-x/b)
# Note that as k increases, x + k*(b/g) decreases (b is negative -p2). Hence max integral k below (-x/b) would lead to lowest positive x
# So, the max value of k such that x1 = x + k*(b/g) remains positive is (-x/b). But if x % b == 0, x1 would become 0, so we would reduce it by 1
# Thus, our answer minimum number (10^k)*(x) + p1 such that p2 divides it, for every consecutive primes p1 and p2 would be achieved for x = x1


# returns list of prime numbers from 1 to n
def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    sieve = np.ones((n // 2,), dtype=bool)    
    for i in range(1, int(n**0.5) // 2 + 1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = False

    primes = [2] + [2*i + 1 for i in range(1, n // 2) if sieve[i]]
    return primes

def get_multiplier(num):
    if num > 100000:
        return 1000000
    elif num > 10000:
        return 100000
    elif num > 1000:
        return 10000
    elif num > 100:
        return 1000
    elif num > 10:
        return 100
    else:
        return 10


limit = 1000000
primes = sieve_of_eratosthenes(limit+50)

result1 = []
answer = 0
for i in range(1, len(primes)):
    if primes[i] > limit:
        break

    if primes[i] >= 5:
        a = get_multiplier(primes[i])
        b = -primes[i+1]
        c = primes[i+1]-primes[i]

        # Solving equation ax + by = c
        x, y = solve_diophantine(a, b, c)
        
        first_positive_solution_k = int(math.floor(-x/b))
        if x + b*first_positive_solution_k == 0:
            first_positive_solution_k-=1
        x = x + b*first_positive_solution_k
        y = y - a*first_positive_solution_k
        
        # print(f"First solution for {primes[i]} and {primes[i+1]} is {x*a + primes[i]}")
        answer += (x*a + primes[i])
        result1.append((x*a + primes[i]))

print(answer)

# Brute force
# def last_digits(num1, num2):
#     while num2:
#         if num2 % 10 != num1%10:
#             return False
#         num1 //= 10
#         num2 //= 10
#     return True

# result2 = []
# for i in range(1, len(primes)):
#     if primes[i] > limit:
#         break

#     if primes[i] >= 5:
#         a = get_multiplier(primes[i])
#         j = 2
#         while True:
#             if last_digits(primes[i+1]*j, primes[i]):
#                 break
#             j+=1
#         result2.append(j*primes[i+1])

# k = 0
# ans = 0
# for i, j in zip(result1, result2):
#     if i != j:
#         print(k, i, j)
#     ans+=j
#     k+=1
# print(ans)

