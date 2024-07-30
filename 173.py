
import math

count = 0
for a in range(1, 100):
    for b in range(1, 100):
        lamina = a*a-b*b
        if (a > b + 1) and ((a-b) % 2 == 0) and (lamina <= 100):
            # print(a, b, lamina, lamina/4 - 1)
            count += 1

print("Brute force solution till 100: ", count)

# Let the outer square side be a and inner square side be b
# Then, a > b and a - b should be multiple of 2 for it to become a square laminae
# If a*a - b*b <= limit, then it is one of the valid laminae
# Coming to the solution of our problem, let's iterate a from 3 to limit/2 and find least possible b for which a*a - b*b <= limit
# solving the equation, b >= sqrt(a*a-limit)

limit = 1000000
answer = 0
for a in range(3, limit//2):
    max_diff = a*a-limit
    if max_diff <= 0:
        min_b = 1
    else:
        min_b = math.ceil(math.sqrt(max_diff))
    if (a - min_b) % 2 == 1:
        min_b += 1
    answer += (a-min_b)//2

print(f"Final answer is {answer}")



