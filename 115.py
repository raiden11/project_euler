
def count_tiles(smallest_tile_size, row_length):
    dp = [0]*(row_length + 1)
    dp[0] = 1
    for i in range(1, row_length + 1):
        dp[i] += dp[i - 1]
        for tile_len in range(smallest_tile_size, row_length + 1):
            last_end = i - tile_len - 1
            if last_end == -1:
                last_end = 0
            if last_end >= 0:
                dp[i] += dp[last_end]
        if dp[i] >= 1000000:
            answer = i
            break
    # print(dp)
    return answer

m = 50; n = 1000
print(count_tiles(m, n))
