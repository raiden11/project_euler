

# Logic 
# Let the 3 numbers in AP be x-a, x and x+a. Simplifying the condition leads to a = (n+x*x)/(4*x).
# It means that n is divisible by x and n+x*x is divisible by 4. But square numbers can only leave remainders 0 and 1 modulo 4
# Hence, n can only be 0 or 3 modulo 4.
# For finding the solution, we use a sieve and iterate over all divisors x of every n, where n = 0/3 modulo 4 number
# If (n+x*x)/(4*x) is an integer and it is less than x, them x-a, x, x+a is the AP satisfying the condition for n

limit = 1000000
solutions = [0]*(limit+10)
numbers = [[] for i in range(limit+2)]

def compute_prime_divisors_of_first_n_numbers(lim):
    for x in range(2, lim+1):
        n = x
        while n <= lim:
            if n % 4 == 0 or n % 4 == 3:
                if (n + x*x) % (4*x) == 0 and (n + x*x) // (4*x) < x:
                    solutions[n]+=1
                    numbers[n].append(x)
            n+=x

compute_prime_divisors_of_first_n_numbers(limit)

answer = 0
for i in range(0, limit + 1):
    if solutions[i] == 10:
        answer += 1
print(answer)


