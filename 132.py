import numpy as np

# Logic 
# This problem looks daunting at first, but is easy once the main idea is clear
# A replunit with k digits can be written as (10^k-1)/9, 
# For k = 10^9, sum of digits is not divisible by 3, so 3 cannot be its prime factor
# Hence, all primes p such that 10^k leaves 1 modulo p would divide R(k), except p = 3

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

# Returns value of a to the power b modulo p
def get_power_modulo_p(a, b, p):
    if b == 1:
        return a % p
    else:
        half_power = get_power_modulo_p(a, b//2, p)
        if b & 1:
            return (half_power*half_power*a)%p
        else:
            return (half_power*half_power)%p

# This function checks ir Repunit(k) i.e. a number having k 1s is divisible by num or not
def check_repunit_divisbility(k, num):
    if get_power_modulo_p(10, k, num) == 1:
        return True
    else:
        return False    

primes = sieve_of_eratosthenes(10000000)
required_primes = 40
answer, count = 0, 0

for prime in primes:
    if check_repunit_divisbility(1000000000, prime) and prime != 3:
        count += 1
        print(count, prime)
        if count <= required_primes:
            answer += prime
print(answer)
