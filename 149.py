
generated_numbers = [0]
matrix = []
matrix_size = 2000

# Logic 
# To solve this, we generate a 2000 by 2000 matrix as described in the problem statement
# Then, for every row, column, diagonal and anti-diagonal, apply Kadane's algorithm that finds the maximum sum continuous subarray
for i in range(1, matrix_size*matrix_size+1):
    if i <= 55:
        generated_numbers.append(((100003 - 200003*i + 300007*i*i*i)%1000000)-500000)
    else:
        generated_numbers.append(((generated_numbers[i-24] + generated_numbers[i-55] + 1000000)%1000000)-500000)
    if i % matrix_size == 0:
        matrix.append(generated_numbers[len(generated_numbers)-matrix_size:])

generated_numbers = []

def find_largest_subsequence_sum(array):
    result = -10000000000000000
    sum = 0
    for i in range(len(array)):
        sum += array[i]
        if sum <= 0:
            sum = 0
        if sum > result:
            result = sum
    return result

answer = -10000000000000000
for row in matrix:
    answer = max(answer, find_largest_subsequence_sum(row))

# All rows
for col in range(0, matrix_size):
    column_array = []
    for row in range(0, matrix_size):
        column_array.append(matrix[row][col])
    answer = max(answer, find_largest_subsequence_sum(column_array))

# All columns
for start_col in range(0, matrix_size):
    row = 0
    col = start_col
    column_array = []
    while row < matrix_size and col < matrix_size:
        column_array.append(matrix[row][col])
        row += 1
        col += 1
    answer = max(answer, find_largest_subsequence_sum(column_array))

# All diagonals that start from top and move towards bottom right
for start_row in range(1, matrix_size):
    row = start_row
    col = 0
    column_array = []
    while row < matrix_size and col < matrix_size:
        column_array.append(matrix[row][col])
        row += 1
        col += 1
    answer = max(answer, find_largest_subsequence_sum(column_array))

# All diagonals that start from left and move towards bottom right
for start_row in range(1, matrix_size):
    row = start_row
    col = 0
    column_array = []
    while row < matrix_size and col < matrix_size:
        column_array.append(matrix[row][col])
        row += 1
        col += 1
    answer = max(answer, find_largest_subsequence_sum(column_array))

# All diagonals that start from bottom and move towards top right
for start_col in range(0, matrix_size):
    row = matrix_size - 1
    col = start_col
    column_array = []
    while row > 0 and col < matrix_size:
        column_array.append(matrix[row][col])
        row -= 1
        col += 1
    answer = max(answer, find_largest_subsequence_sum(column_array))

# All diagonals that start from left and move towards top right
for start_row in range(0, matrix_size):
    row = start_row
    col = 0
    column_array = []
    while row > 0 and col < matrix_size:
        column_array.append(matrix[row][col])
        row -= 1
        col += 1
    answer = max(answer, find_largest_subsequence_sum(column_array))

print(answer)
