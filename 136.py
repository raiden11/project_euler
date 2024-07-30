
import numpy as np

# Approach: Assuming AP as (a-d), a, a+d, I solved that d = (x+a^2)/(4a)
# Irrelevant -> Using modular arithmetic, since numberator is always divisible by 4, x could be of form 4k or 4k+3 only
# Irrelevant -> if x is of form 4k, a could only be even. If x is of form 4k+3, x could be of form 4m+1 and 4m+3 only
# Now, d = (x+a^2) is divisible by a means x is divisible by a. Let's x = p*a, then d = (p + a)/4. We will check what x and a can be by casework
# 
# CASE A: When X is odd
# Prime factorization of X can only be of form (4k+3) to have a single solution. 
# If x has 2 factors modulo 3 factors (4k+3)*(4m+3), we get no solutions. For x = (4k+3)*(4m+3)*(4n+3), we get multiple solutions: a = 1 and a = 4k+3 and a = 4m+3 and a = 4n+3
# If x has only factors that give 1 modulo 4 (x=4k+1), we get no solution as sum of any factors will not be divisible by 4.
# If x has all 4k+1 type factors, but just one 4k+3 type factor, we will get multiple solutions: a = 1, p = (4k+1)*(4n+3) and a = (4k+1), p = (4n+3)  
# Hence, if x is odd, it can be only of type 4k+3
# 
# CASE B: When X is even
# A single 2 in prime factorization can never yield any solution as one of a and p will be divisible by 2, and other not
# So x is divisible by 4. And both 2s must be on different side to ensure both a and p are divisible by 2
# Apart from 4, x cannot have more than 1 prime factor of form 4k+1, otherwise we get mnultiple solutions as 4n+1 does not change modulo of any side
# Also, x cannot have more than 1 factor of form 4k+3. Proof: Let x = 4*(4k+3)*(4m+3), then a = 2*(4k+3) and a = 2 both are value solutions
# power of 2 can also be 4 as both a and p would be divisible by 4 in that case. More power of 2 would lead to multiple solutions.
# Conclusion: prime factorization of x can only be (4n+3) or 2^p*(4n+3) or 2^p*(4n+1) where p is either 2 or 4
# 
#  All Solutions:
# For x = (4n+3), solution is a = 1, p = 4n+3, and this is the only solution
# For x = 2^2*m where m is either 4n+1 or 4n+3 is a = 2, p = 2*m, and this is the only solution
# For x = 2^4*m where m is either 4n+1 or 4n+3 is a = 4, p = 4*m, and this is the only solution
# Unique solutions not covered by our algo: x = 4 and x = 16
# Hence, a could only be 1, 2 or 4 and x must be of the above form only

# ------------------------------- BRUTE FORCE SOLUTION -------------------------------------------
# unique_sol = set()
# for num in range(1, 101):
#     count = 0
#     sol = ()
#     for a in range (1, num+1):
#         for d in range(1, a):
#             if num == ((a+d)*(a+d)-a*a-(a-d)*(a-d)):
#                 # print(f"Found solution for {num}: {a} and {num//a}, Terms {a-d}, {a}, {a+d}")
#                 sol = (a-d, a, a+d)
#                 count +=1
#     if count == 1:
#         print(f"----------------------- Found solution for {num}: {sol[1]} and {num//sol[1]}, Terms {sol}")
#         unique_sol.add(num)
# print(sorted(unique_sol))
# print(len(unique_sol))

def sieve_of_eratosthenes(n):
    # DO NOT COPY THIS
    # This sieve does not return prime number 2
    if n < 2:
        return []
    if n == 2:
        return [2]
    sieve = np.ones((n // 2,), dtype=bool)    
    for i in range(1, int(n**0.5) // 2 + 1):
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = False

    primes = [2*i + 1 for i in range(1, n // 2) if sieve[i]]
    return primes

limit = 50000000
answer = 0
# s = set()
primes = sieve_of_eratosthenes(limit)
for prime in primes:
    if prime % 4 == 3:
        answer += 1
        # s.add(prime)
        if 4*prime <= limit:
            answer += 1
            # s.add(4*prime)
        if 16*prime <= limit:
            answer += 1
            # s.add(16*prime)
    elif prime %4 == 1:
        if 4*prime <= limit:
            # s.add(4*prime)
            answer += 1
        if 16*prime <= limit:
            answer += 1
            # s.add(16*prime)
print(answer + 2)
# print(len(s) + 2)