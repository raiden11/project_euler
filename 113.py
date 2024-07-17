
# DO NOT DEFINE LIKE [[None]*5]*5
# https://stackoverflow.com/questions/2739552/2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
inc_dp = [[-1]*11 for _ in range(105)]
dec_dp = [[-1]*11 for _ in range(105)]

def count_increasing_numbers(cur_place, max_length, last_num):

    ans = 0
    if cur_place > max_length:
        return 1

    for digit in range(1, 10):
        if digit >= last_num:
            if inc_dp[cur_place][digit] == -1:
                tmp_ans = count_increasing_numbers(cur_place + 1, max_length, digit)
                inc_dp[cur_place][digit] = tmp_ans
            ans += inc_dp[cur_place][digit]

    return ans


def count_decreasing_numbers(cur_place, last_num, dec_dp):
    ans = 0
    if cur_place < 1:
        if last_num > 0:
            return 1
        else:
            return 0
    
    for digit in range(0, 10):
        if digit >= last_num:
            if dec_dp[cur_place][digit] == -1:
                tmp_ans = count_decreasing_numbers(cur_place - 1, digit, dec_dp)
                dec_dp[cur_place][digit] = tmp_ans
            ans += dec_dp[cur_place][digit]
    return ans


def count_non_bouncy_numbers(max_length):
    global inc_dp
    increasing_numbers = 0
    decreasing_numbers = 0
    for current_length in range(1, max_length + 1):
        inc_dp = [[-1]*11 for _ in range(105)]
        increasing_numbers += count_increasing_numbers(1, current_length, -1)
        
    for current_length in range(1, max_length + 1):
        inc_dp = [[-1]*11 for _ in range(105)]
        decreasing_numbers += count_decreasing_numbers(current_length, -1, dec_dp)

    # Deducting common answers having all digits same
    ans = increasing_numbers + decreasing_numbers - 9*max_length
    return ans


max_length = 100
print(count_non_bouncy_numbers(max_length))

