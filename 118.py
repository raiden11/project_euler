
import numpy as np
import time

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

# Filter only those primes that have distinct digits, do not contain zero, and do not have all single digit primes if number lenght is 8
def are_digits_distinct(num):
    num_str = str(num)
    dig_set = set(num_str)
    if len(num_str) != len(dig_set) or '0' in dig_set or (len(num_str) == 8 and '2' in dig_set and '3' and dig_set and '5' in dig_set and '7' in dig_set):
        return False
    else:
        return True

# Run the sieve
# None of the numbers having all 9 digits could be prime, due to 3's divisibility rule, so we can set limit as 1e9
limit = 1000000000
start_time = time.time()
prime_numbers = sieve_of_eratosthenes(limit)
print(f"number of primes below {limit} are {len(prime_numbers)}")
end_time = time.time()
elapsed_time = end_time - start_time
print("Time to calculate prime numbers: ", elapsed_time)

# Run the distinct prime function
distinct_digits_prime = []
for num in prime_numbers:
    if are_digits_distinct(num):
        distinct_digits_prime.append(num)

print(f"distinct digits primes below {limit} are {len(distinct_digits_prime)}")

# Find set of unique digits in a given number
def get_digits(num):
    digits = set()
    while num:
        digits.add(num % 10)
        num //= 10
    return digits

dp = [0]*1024
dp[0] = 1
pandigital_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Main Code
# Dp[i] stores the number of sets that have i unique digits. i is written in binary. Max value can be 1023 as there are 10 unique digits
# So i = 145 stands for 001100100 which means number of sets having digits 2, 5, 6 as we are counting o to 9 from right to left.
# # Algorithm: 1. Iterate over all the distinct digit primes (31490 for 1e9), find complement of its binary representation.
#              2. Iterate over all the subsets of its complement. Create their mask.
#              3. Add dp[mask] to dp[mask | prime_mask] - as we would be getting mask | prime_mask number after adding current prime to mask
for prime in distinct_digits_prime:
    digits_set = get_digits(prime)
    exclusion_set = pandigital_set.difference(digits_set)
    exclusion_list = list(exclusion_set)
    n = len(exclusion_set)
    prime_mask = 0
    for digit in digits_set:
        prime_mask |= (1 << digit)
    for i in range(1 << n):
        mask = 0
        for j in range(n):
            if (i & (1 << j)) != 0:
                mask |= (1 << exclusion_list[j])
        dp[prime_mask | mask] += dp[mask]

print("Our answer is ", dp[1023])


