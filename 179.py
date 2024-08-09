
# Number of factors of n is the defintion of sigma function
# Below code calculates sigma for first n numbers and finds the answer

def get_sigma_first_n(n):
    sigma = [1]*(n+1)
    for i in range(2, n+1):
        if sigma[i] == 1:
            sigma[i] = 2
            j = 2*i
            while j <= n:
                count = 0
                num = j
                while num % i == 0:
                    count += 1
                    num //= i
                sigma[j] *= (count + 1)
                j += i
    return sigma

answer = 0
limit = 10000000
sigma = get_sigma_first_n(limit)
for i in range(2, limit):
    if sigma[i] == sigma[i+1]:
        answer += 1
print(answer)

