
import numpy as np

# Logic 
# We are looking for prime numbers under 100000 that will never divide R(10^k) for k >= 1
# It follows that they will never divide 10^m-1 where m is of the form 10^k, except 3, which will divide 10^m-1, but not R(10^k)
# We will generate all primes below 100000 and find the ones that leave remainder 1 for at least 1 number of type 10^m
# For every p, we will find remainder of 10^10 mod p. Then, we take keep taking 10th power of remainder, until we get 1
# If we get 1, the prime p must divide some R(10^k). If the remainders start repeating, we shall never get remainder 1 

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

def get_power_modulo_p(a, b, p):
    if b == 1:
        return a % p
    else:
        half_power = get_power_modulo_p(a, b//2, p)
        if b & 1:
            return (half_power*half_power*a)%p
        else:
            return (half_power*half_power)%p

limit = 100000
primes = sieve_of_eratosthenes(limit)

answer, div, nondiv = 2 + 3, 0, 0
for prime in primes:
    if prime <= 3:
        continue
    remainders = set()
    remainder = 10
    power = 1
    while True:
        remainder = get_power_modulo_p(remainder, 10, prime)
        if remainder == 1:
            print(f"Found answer for prime={prime} when power is 10 to the power of 1 with {power} zeroes")
            div += 1
            break
        else:
            if remainder in remainders:
                answer += prime
                nondiv += 1
                # print(f"Found cycle for prime={prime} when power is 10 to the power of 1 with {power} zeroes")
                break
            else:
                remainders.add(remainder)
        power += 1

print(f"Under {limit}, there are {div} primes that will divide R(10^k) and {nondiv} that will not divide and sum of them is {answer}")


