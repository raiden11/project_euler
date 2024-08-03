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

primes = sieve_of_eratosthenes(1000)

# check few cases for which it is true
# for prime in primes:
#     for i in range(1, 10000):
#         cube = i*i*(i+prime)
#         cube_root = cube**(1./3.)
#         if round(cube_root) ** 3 == cube:
#             print(f"Found for prime = {prime}, number = {i}, p+n={prime+i}, cube={cube}")

# LOGIC
# n*n*(n+p) =k^3 is cubic leads to the big possibility that n divides k, so let k = an
# which means that p = (a^3-1)*n, but p is prime, but a^3-1 is factorable so it is not prime for any a > 2
# Hence, either a = 2 and n = 1 in every case, or our assumption is wrong.
# So let n does not divide k
# But (n+p) could be multiple of n. Let n+p = a*n. Then p = (a-1)*n. This is only possible if n = 1 every time.
# But, n cannot be 1 except when p=7, because our equation would become p+1 is cubic, which is true only for p=7
# Hence, for p>7, n is not 1. Which means n neither divides n+p, nor k. So gcd(n, n+p)=1
# But n*n*(n+p) is still cubic, so n and n+p both are cubic
# So we would check every cubic n for every prime p where p < 10^6

# => Upper bound for n could be obtained by the fact that (n+1)^3-n^3 = 3n^2+x
# Let n = a^3. Then difference of cubes (n+p)-(n) = (a^3+p)-(a^3) = p >= 3*a*a
# Which means a <= sqrt(p/3). But max value of p can be 10^6, so a <= 578. hence we will use max bound of a = sqrt(n) = 600 


limit, answer = 1000000, 0
primes = sieve_of_eratosthenes(limit)
for prime in primes:
    for a in range(1, 600):
        n = a*a*a
        possible_cube = n + prime
        cube_root = possible_cube**(1./3.)
        if round(cube_root) ** 3 == possible_cube:
            # print(f"Found for prime = {prime}, number n = {n}, p+n={possible_cube}, final cube = {(a**6)*possible_cube}")
            answer+=1
            break
print(f"Number of primes below {limit} satisfying this property is {answer}")















