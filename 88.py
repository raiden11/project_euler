
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

limit = 24000
result = [-1]*(6*limit)

def analyze(number, factors_list, unique_factors, cur, product, multiplied_factors_sum, multplied_factors_count):

    if cur == unique_factors:
        remaining = number // product
        if product == 1:
            return
        # if remaining == 1:
        #     k = multplied_factors_count
        k = (number - (remaining + multiplied_factors_sum)) + multplied_factors_count + 1        
        # print(product, k, multiplied_factors_sum, multplied_factors_count)

        # if product == num or product == 1:
        #     return
        if result[k] == -1:
            # print(f" Found answer for {k}: {product}")
            result[k] = number
        return

    cur_product = product
    cur_multiplied_factors_sum = multiplied_factors_sum
    cur_multplied_factors_count = multplied_factors_count

    analyze(number, factors_list, unique_factors, cur + 1, cur_product, cur_multiplied_factors_sum, cur_multplied_factors_count)
    for _ in range(factors_list[cur][1]):
        cur_product*=factors_list[cur][0]
        cur_multiplied_factors_sum += factors_list[cur][0]
        cur_multplied_factors_count += 1
        analyze(number, factors_list, unique_factors, cur + 1, cur_product, cur_multiplied_factors_sum, cur_multplied_factors_count)


for num in range(4, limit):
    factors_list = []
    factors_dict = factorize(num)
    for k, v in factors_dict.items():
        factors_list.append((k, v))
    print(f"Number is {num}")
    analyze(num, factors_list, len(factors_list), cur=0, product=1, multiplied_factors_sum=0, multplied_factors_count=0)
    print()

k_set = set()
answer = 0
for i in range(2, limit+1):
    if result[i] == -1:
        print(f"Not found answer for {i}")
    else:
        print(f"i = {i}, answer = {result[i]}")
        k_set.add(result[i])

for num in k_set:
    answer += num

print(f"Final answer is {answer}")



