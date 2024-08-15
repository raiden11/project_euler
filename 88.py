
import time
from collections import defaultdict

start_time = time.time()
limit = 12000
prime_divisors = [[] for _ in range(2*limit+2)]
divisors = [set() for _ in range(2*limit+2)]

def compute_prime_divisors_of_first_n_numbers(n):
    for i in range(2, n+1):
        if len(prime_divisors[i]) == 0:
            prime_divisors[i].append(i)
            j = 2*i
            while j <= n:
                num = j
                while num % i == 0:
                    num //= i
                    prime_divisors[j].append(i)
                j+=i

def compute_divisors_of_first_n_numbers(n):
    for num in range(n+1):
        prime_divisors_count = len(prime_divisors[num])
        for i in range(1 << prime_divisors_count):
            divisor = 1
            for j in range(prime_divisors_count):
                if (i & (1 << j)) != 0:
                    divisor *= prime_divisors[num][j]
            divisors[num].add(divisor)

compute_prime_divisors_of_first_n_numbers(2*limit)
compute_divisors_of_first_n_numbers(2*limit)

product_sum_pairs = defaultdict(set)
product_sum_pairs[1] = set({(0, 0)})
minimal_product_sum = [limit*100000]*(limit+2)

for i in range(2, 2*limit+1, 1):
    for d in divisors[i]:
        if d == 1:
            continue
        for pair in product_sum_pairs[i//d]:
            product_sum_pairs[i].add((pair[0]+d, pair[1]+1))
    for pair in product_sum_pairs[i]:
        k = pair[1] + (i - pair[0])
        if k <= limit:
            minimal_product_sum[k] = min(minimal_product_sum[k], i)

answer_set = set()
for i in range(2, limit + 1):
    answer_set.add(minimal_product_sum[i])

print(sum(answer_set))
end_time = time.time()
print(f"Time taken: {end_time - start_time}")    # Runs in less than 2 seconds for limit = 12000

