
import math 

# Brute force
# limit = 100
# for u in range(1, limit+1):
#     for v in range(1, u):
#         for k in range(1, limit+1):
#             b_2 = 2*u*v*k
#             h = (u*u-v*v)*k
#             if h >= b_2:
#                 if abs(2*b_2-h) == 1:
#                     print(f"Found 1 {u} {v} and sides {2*b_2*k} and {h*k}")
#             else:
#                 if abs(2*h-b_2) == 1:
#                     print(f"Found 2 {u} {v} and sides {b_2*k} and {2*h*k}")

v, count, answer = 1, 1, 0
while True:
    d1 = math.sqrt(5*v*v+1)
    if d1 % 1 == 0 and d1*d1 == 5*v*v+1:
        u = int(2*v + d1)

    d2 = math.sqrt(5*v*v-1)
    if d2 % 1 == 0 and d2*d2 == 5*v*v-1:
        u = int(2*v + d2)
    
    side_a = 2*u*v
    side_b = u*u-v*v
    L = math.sqrt(side_a*side_a + side_b*side_b)
    v = u
    answer += int(L)
    
    if count == 12:
        break
    count += 1

print(answer)

