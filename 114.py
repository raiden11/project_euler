
def count_tiles(row_length):
    dp = [0]*(row_length + 1)
    dp[0] = 1
    for i in range(1, row_length + 1):
        dp[i] += dp[i - 1]
        for tile_len in range(3, row_length + 1):
            last_end = i - tile_len - 1
            if last_end == -1:
                last_end = 0
            if last_end >= 0:
                dp[i] += dp[last_end]
    # print(dp)
    return dp[row_length]

required_length = 50
print(count_tiles(required_length))
