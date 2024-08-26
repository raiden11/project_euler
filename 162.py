
# Simple Digit DP problem

def count_numbers(max_places, current_place, zero_used, one_used, a_used, dp):
    if dp[current_place][zero_used][one_used][a_used] != -1:
        return dp[current_place][zero_used][one_used][a_used]
    if current_place >= max_places:
        if a_used + zero_used + one_used == 3:
            return 1
        else:
            return 0

    result = 0
    for digit in range(0, 16):
        if current_place == 0 and digit == 0: 
            continue
        zero_used_1 = zero_used or digit == 0
        one_used_1 = one_used or digit == 1
        a_used_1 = a_used or digit == 10
        result += count_numbers(max_places, current_place+1, zero_used_1, one_used_1, a_used_1, dp)
    dp[current_place][zero_used][one_used][a_used] = result
    return result

answer, digits_limit = 0, 16
for total_digits in range(1, digits_limit+1):
    dp = [[[[-1 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(20)]
    numbers = count_numbers(total_digits, 0, 0, 0, 0, dp)
#     print(total_digits, numbers)
    answer += numbers

print(answer)

