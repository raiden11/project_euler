import time

start_time = time.time()
limit = 100000000
answer = 0
primes = [0]*(limit+10)
for i in range(2, limit):
    if primes[i] == 2:
        answer += 1 
        # print(i)
    if primes[i] == 0:
        j = 2*i
        while j < limit:
            num = j
            while num % i == 0:
                num //= i
                primes[j]+=1
            j+=i
print(f"Final answer is {answer}")
end_time = time.time()
print("time taken: ", end_time - start_time)
# Took ~80 seconds on my PC

