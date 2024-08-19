

# Logic 
# This is not so difficult, you just have to find an optimal way iterating through all triangles - pre-computation helps here 
# I pre-computed cumulative sums of every row in the triangle, every top-to-left diagonal and every top-to-right diagonal
# Then, assuming top of the triangle as first element of each row, I calculated sum till last row of the triangle where last row ranges from start+1 to 1000
# We can calculate sums of subsequent triangles in the same start row by adding and subtracting parts of pre-computed diagonal cumulative sums
# I estimated earlier that total number of triangles are ~1.67 * 10**8, and finding sum using pre-computed arrays takes O(1)

# Estimating number of triangles
# triangles = 0
# rows = 1000
# for i in range(1, 1001):
#     triangles += i*rows
#     rows -= 1
# print(triangles)

answer = -1
solution = None
rows_count = 1000

rows_cum_sum = [[] for i in range(rows_count+1)]
top_left_diagonals = [[] for i in range(rows_count+1)]
top_right_diagonals = [[] for i in range(rows_count+1)]

def pre_calculate_cum_sums(limit):
    global answer, solution
    t, current_row, row_target, row_pushed_count = 0, 1, 1, 0
    for _ in range(1, limit+1):
        t = (615949*t + 797807) % 1048576
        s = t-524288

        if row_pushed_count >= 1:
            rows_cum_sum[current_row].append(s + rows_cum_sum[current_row][row_pushed_count-1])
        else:
            rows_cum_sum[current_row].append(s)
        row_pushed_count += 1

        left_digonal_len = len(top_left_diagonals[row_pushed_count])
        if left_digonal_len == 0:
            top_left_diagonals[row_pushed_count].append(s)
        else:
            top_left_diagonals[row_pushed_count].append(s + top_left_diagonals[row_pushed_count][left_digonal_len - 1])
        
        right_row_number = current_row - row_pushed_count
        right_digonal_len = len(top_right_diagonals[right_row_number])
        if right_digonal_len == 0:
            top_right_diagonals[right_row_number].append(s)
        else:
            top_right_diagonals[right_row_number].append(s + top_right_diagonals[right_row_number][right_digonal_len - 1])        
        
        answer = min(answer, s)
        solution = ('single')
        if row_pushed_count == row_target:
            row_pushed_count = 0
            current_row += 1
            row_target += 1

pre_calculate_cum_sums((rows_count*(rows_count+1))//2)
print("pre-calculation done")

for start_row in range(1, rows_count + 1):
    left_most_sum = rows_cum_sum[start_row][0]
    last_row_len = 1
    # print(f"working on start+row={start_row}")
    for last_row in range(start_row + 1, rows_count + 1):
        last_row_len += 1
        left_most_sum += rows_cum_sum[last_row][last_row_len-1]
        rolling_sum = left_most_sum
        if rolling_sum < answer:
            answer = min(answer, left_most_sum)
            solution = (start_row, start_row+1, 0)

        for j in range(1, start_row):
            rolling_sum -= (top_left_diagonals[j][last_row-j] - top_left_diagonals[j][start_row-j-1])
            rolling_sum += (top_right_diagonals[start_row-j-1][last_row-start_row+j] - top_right_diagonals[start_row-j-1][j-1])
            if rolling_sum < answer:
                answer = min(answer, rolling_sum)
                solution = (start_row, last_row, j)

# solution prints (first row, last row, j) of the minimum triangle where j is distance from the left end, j = 0 being the leftmost triangle
print(answer, solution) 








