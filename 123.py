
# equation reduces to n*p_n + 1 + n*p_n*(-1)**(n-1) + (-1)**n
import numpy as np

def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]

    # Only consider odd numbers
    sieve = np.ones((n // 2,), dtype=bool)
    
    for i in range(1, int(n**0.5) // 2 + 1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = False
    
    primes = [2] + [2*i + 1 for i in range(1, n // 2) if sieve[i]]
    return primes

# Example usage
limit = 1000000
prime_numbers = sieve_of_eratosthenes(limit)
print(f"number of primes: {len(prime_numbers)}")
# print(f"Prime numbers from 1 to {n}: {sieve_of_eratosthenes(n)}")

cnt = 1
for prime in prime_numbers:
    value = cnt*prime + 1
    if cnt & 1: # cnt is even
        value -= 1
        value += (cnt*prime)
    else: # cnt is odd
        value += 1
        value -= (cnt*prime)
    
    cnt += 1
    remainder = value % (prime*prime)
    # print(prime, value, remainder)
    if remainder >= 10000000000:
        print("Found: ", prime, cnt - 1, value, remainder)
        break
