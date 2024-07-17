import numpy as np

def sieve_of_eratosthenes(n):
    # DO NOT COPY THIS FUNCTION IT IS MODIFIED
    if n < 2:
        return []
    if n == 2:
        return [2]

    # Only consider odd numbers
    sieve = np.ones((n // 2,), dtype=bool)
    
    for i in range(1, int(n**0.5) // 2 + 1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = False
    
    primes = [2*i + 1 for i in range(1, n // 2) if sieve[i]]
    return primes, sieve

mod1 = [3]
mod2 = [3]
primes, _ = sieve_of_eratosthenes(10000)
_, sieve = sieve_of_eratosthenes(100000000)

for prime in primes:
    if prime == 5:
        continue
    if prime % 3 == 1:
        mod1.append(prime)
    elif prime % 3 == 2:
        mod2.append(prime)

required_size = 5
print(len(mod1), len(mod2))

final_ans = None
min_sum = 1000000

def check_pair(a, b):
    num1 = int(str(a) + str(b))
    num2 = int(str(b) + str(a))
    if not sieve[(num1-1)//2] or not sieve[(num2-1)//2]:
        return False
    return True

def check_min_combo(group):
    global min_sum
    global final_ans
    for n1 in range(0, len(group)-4):
        for n2 in range(n1+1, len(group)-3):
            if not check_pair(group[n1], group[n2]):
                continue
            for n3 in range(n2+1, len(group)-2):
                if not check_pair(group[n1], group[n3]) or not check_pair(group[n2], group[n3]):
                    continue
                for n4 in range(n3+1, len(group)-1):
                    if not check_pair(group[n1], group[n4]) or not check_pair(group[n2], group[n4]) or not check_pair(group[n3], group[n4]):
                        continue
                    for n5 in range(n4+1, len(group)):
                        if not check_pair(group[n1], group[n5]) or not check_pair(group[n2], group[n5]) or not check_pair(group[n3], group[n5]) or not check_pair(group[n4], group[n5]):
                            continue
                        else:
                            combo_sum = group[n1]+group[n2]+group[n3]+group[n4]+group[n5]
                            print("found: ", combo_sum, group[n1], group[n2], group[n3], group[n4], group[n5])
                            if combo_sum < min_sum:
                                min_sum = combo_sum
                                final_ans = (group[n1], group[n2], group[n3], group[n4])

check_min_combo(mod1)
check_min_combo(mod2)

print("Final Answer: ", min_sum, final_ans)