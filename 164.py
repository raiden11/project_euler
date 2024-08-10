
dp = [[[-1 for i in range(12)] for j in range(12)] for k in range(510)]

# Logic 
# Simple digit dp problem
# dp[place][last][sec_last] represents number of solutions having `places` digits and its last, second last digits are last, sec_last

def count(n, place, last, sec_last): 
    if place == n:
        return 1
    if dp[place][last][sec_last] != -1:
        return dp[place][last][sec_last]
    start = 0
    if place == 0:
        start = 1
    answer = 0
    for dig in range(start, 10):
        if last + sec_last + dig <= 9:
            answer += count(n, place+1, sec_last, dig)
    dp[place][last][sec_last] = answer
    return answer

answer = count(500, 0, 0, 0)
print(answer)
