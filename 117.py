

def count_tiles(tile_lengths, row_length):
    dp = [0]*(row_length + 1)
    dp[0] = 1
    for i in range(1, row_length + 1):
        for tile_length in tile_lengths:
            if (i >= tile_length):
                dp[i] += dp[i-tile_length]
    return dp[row_length]

required_length = 50
print(count_tiles([1, 2, 3, 4], required_length))

