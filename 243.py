from collections import defaultdict
import math

def factorize(n):
    factors = set()
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors.add(2)
        n = n // 2
    
    # n must be odd at this point
    # so we can skip one element (i.e., i = i + 2)
    for i in range(3, int(n**0.5) + 1, 2):
        # while i divides n, add i and divide n
        while n % i == 0:
            factors.add(i)
            n = n // i
    
    # This condition is to check if n is a prime number
    # greater than 2
    if n > 2:
        factors.add(n)
    
    return factors    


limit = 0.16358819555
# limit = 0.4
mini = 0.4

num = 2*3*5*7*11*13*17*19*23
while num <= 2*3*5*7*11*13*17*19*23*29:
    factor_list = list(factorize(num))
    factors_count = len(factor_list)
    answer = 0
    for i in range(1, 1 << factors_count):
        factor = 1
        primes = 0
        for j in range(factors_count):
            if (i & (1 << j)) != 0:
                factor = factor * factor_list[j]
                primes += 1
        if primes & 1:
            answer += math.floor((num - 1) / factor)
        else:
            answer -= math.floor((num - 1) / factor)
        # print(factor, primes, math.floor((num - 1) / factor), answer)
    # print(num, factor_list, answer)

    fraction = (num - 1 - answer) / (num - 1)
    # print("combinations for number: ", num, factor_list, answer, fraction, (num - 1 - answer), (num-1))
    if fraction < mini:
        print(num, factor_list, answer, fraction, (num - 1 - answer), (num-1))
        mini = fraction
        if fraction < limit:
            print("FOUND IT: ", num)
        # break
    num += 2*3*5*7*11*13*17*19











