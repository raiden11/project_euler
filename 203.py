
import numpy as np

answer, last_row, max_row = 0, [1, 1], 51
square_free_numbers = set()

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

primes = sieve_of_eratosthenes(2*10**7)
prime_squares = list(map(lambda prime: prime*prime, primes))

def is_squarefree(num):
    squarefree = 1
    for prime_square in prime_squares:
        if prime_square > num:
            break
        if num % prime_square == 0:
            squarefree = 0
            break
    return squarefree
    
mx = -1
for row in range(3, max_row+1):
    cur_row = [1]
    for i in range(len(last_row)-1):
        cur_row.append(last_row[i] + last_row[i+1])
    cur_row.append(1)
    for num in cur_row:
        if is_squarefree(num):
            square_free_numbers.add(num)
    last_row = cur_row

# print(square_free_numbers)
print(sum(square_free_numbers))
