
import math

# Logic 
# First of all, all numbers n would be repunit in base n-1. We have to find the second base where they would be a repunit
# All strong repunits are of form 1 + base + base^2 + ... + base^k for k >= 2
# Hence, we maintain a set of strong repunits and insert all numbers that are of the above form

limit = 10**12
strong_repunits = set({1})
for base in range(2, math.ceil(math.sqrt(limit))):
    res = 1 + base
    num = base
    while True:
        num *= base
        if res + num > limit:
            break
        res += num
        strong_repunits.add(res)

answer = sum(strong_repunits)
print(answer)