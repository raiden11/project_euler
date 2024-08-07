
import numpy as np
from math import sqrt
from collections import defaultdict

# This is a simple implementation based problem
# Generate all numbers with 10 digits with 9 same, and add sum of primes. Similar for numbers with 10 digits with 8 same

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

primes = sieve_of_eratosthenes(100000)

def check_prime(num):
    sqrt_num = sqrt(num)
    for prime in primes:
        if prime > sqrt_num:
            break
        if num % prime == 0:
            return False
    return True

sum = defaultdict(int)
count = 0
# digits_in_number = 4 # solves the case given as example in the problem
digits_in_number = 10
for digit in range(1, 10):
    for other_digit in range(0, 10):
        if (digit*9+other_digit) % 3 == 0:
            continue
        if other_digit != digit:
            for other_digit_place in range(0, digits_in_number):
                if digit in set({2, 4, 6, 8, 5}) and other_digit_place != digits_in_number - 1:
                    continue
                if other_digit_place == digits_in_number - 1 and other_digit in set({2, 4, 6, 8, 5, 0}):
                    continue
                number = ""
                for place in range(0, digits_in_number):
                    if other_digit_place == place:
                        number += str(other_digit)
                    else:
                        number += str(digit)
                if check_prime(int(number)):
                    # print(f"Found for digit {number} {digit}")
                    sum[digit] += int(number)
                count +=1
print(sum)

other_digits_places = []  # List of all possible places where other 2 digits can be placed when our number has 8 same digits
for dig1 in range(0, 10):
    for dig2 in range(0, 10):
        for place1 in range(0, digits_in_number - 1):
            for place2 in range(place1 + 1, digits_in_number):
                other_digits_places.append(((str(dig1), place1), (str(dig2), place2)))

print(len(other_digits_places))  # 4500 = 10*10*(10 choose 2)

count = 0
# Only 0, 2 and 8 had all composites in 9 same digit numbers
for digit in [0, 2, 8]:
    for combination in other_digits_places:
        number_array = [str(digit)]*digits_in_number
        places = [combination[0][1], combination[1][1]]
        if digit == 0 and 0 not in places:
            continue
        if (digit == 2 or digit == 8) and (digits_in_number - 1) not in places:
            continue
        number_array[combination[0][1]] = combination[0][0]
        number_array[combination[1][1]] = combination[1][0]
        if number_array[0] == '0':
            continue
        number = int(''.join(number_array))
        if check_prime(number):
            # print(f"Found prime {number}")
            sum[digit] += number

answer = 0
for k, v in sum.items():
    answer += v
print(f"Final answer is {answer}")
