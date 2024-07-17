
def count_tiles(tile_length, row_length):
    dp = [0]*(row_length + 1)
    dp[0] = 1
    for i in range(1, row_length + 1):
        dp[i] += dp[i-1]
        if (i >= tile_length):
            dp[i] += dp[i-tile_length]
    return dp[row_length] - 1

required_length = 50
print(count_tiles(2, required_length) + count_tiles(3, required_length) + count_tiles(4, required_length))
