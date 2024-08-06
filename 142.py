
import time
from collections import defaultdict

# Logic:
# This is a simple implementation based problem. The only catch is to search for square numbers first, rather than x, y or z 
# Assuming the equations to be x+y=a^2, x-y=b^2, x+z=c^2, x-z=d^2, y+z=p^2, y-z=q^2
# Note that since x > y > z, so a > c > p and a > b, c > d and p > q
# Also, note that all x, y, z, must be of same parity. And all (a, b) and (c, d) and (p, q) must be of same parity to be divisible by 2
# x can be written as x = (a^2+b^2)/2 = (c^2+d^2)/2. Similarly z = (p^2-q^2)/2 = (c^2-d^2)/2. Same for y
# We start by iterating over all possible sum of squares x that have two solutions as x is sum of squares of (a, b) as well as (c, d) 
# Then possible y and possible z would be difference of these solutions (a^2-b^2) or (c^2-d^2)/2
# Complete all the missing pieces using if conditions and you get the solution!

# Trivia (from discussion thread):
# 1. This is a well known problem whose solutions were known back in 1642. Someone solved it by hand. Euler found the smallest solution.
#    Here is the paper explaining a general solution: https://www.austms.org.au/wp-content/uploads/Gazette/2005/Sep05/Buchholz.pdf
# 2. Some members solved it using diophantine equation
# 3. Further reduction in cases is also possible 


start_time = time.time()
addition_dict = defaultdict(list)
subtraction_dict = defaultdict(list)
sq_limit = 1500

for i in range(1, sq_limit):
    if i & 1:
        start_j = 1
    else:
        start_j = 2
    for j in range(start_j, i, 2):
        addition_dict[i*i+j*j].append((i, j))
        subtraction_dict[i*i-j*j].append((i, j))

keys = list(addition_dict.keys())

for k in keys:
    v = addition_dict[k]
    if len(v) > 1:
        for pair in v:
            possible_y = pair[0]*pair[0] - pair[1]*pair[1]
            if len(addition_dict[possible_y]) > 0:
                # print(f"Found possible x and y: {k} and {possible_y} for {pair}")
                for pair1 in addition_dict[possible_y]:
                    possible_z = pair1[0]*pair1[0] - pair1[1]*pair1[1] 
                    if len(subtraction_dict[possible_z]) > 1:
                        for pair2 in subtraction_dict[possible_z]:
                            if pair2 != pair1:
                                possible_x = pair2[0]*pair2[0] + pair2[1]*pair2[1] 
                                if possible_x == k:
                                    print(f"Found possible x and y and z: for (a, b)={pair} and (p, q)={pair1} and (c, d)={pair2}")
                                    x = (pair[0]*pair[0] + pair[1]*pair[1])//2
                                    y = (pair1[0]*pair1[0] + pair1[1]*pair1[1])//2
                                    z = (pair1[0]*pair1[0] - pair1[1]*pair1[1])//2
                                    print(f"(x, y, z) is {(x, y, z)} and sum is {x+y+z}")
            if len(subtraction_dict[possible_y]) > 1:
                # print(f"Found possible x and z: {k} and {possible_y} for {pair}")
                for pair1 in subtraction_dict[possible_y]:
                    if pair != pair1:
                        possible_again_y = pair1[0]*pair1[0] + pair1[1]*pair1[1] 
                        if len(subtraction_dict[possible_y]) > 0:
                            for pair2 in subtraction_dict[possible_y]:
                                possible_x = pair2[0]*pair2[0] + pair2[1]*pair2[1] 
                                if possible_x == k and pair2 != pair:
                                    print(f"Found possible x and y and z: for (c, d)={pair} and (p, q)={pair1} and (a, b)={pair2}") 
                                    x = (pair2[0]*pair2[0] + pair2[1]*pair2[1])//2
                                    y = (pair1[0]*pair1[0] - pair1[1]*pair1[1])//2
                                    z = (pair1[0]*pair1[0] + pair1[1]*pair1[1])//2
                                    print(f"(x, y, z) is {(x, y, z)} and sum is {x+y+z}")

end_time = time.time()
print(f"Seconds taken to run this code: {end_time-start_time}")

# Runs under 4 seconds for sq_limit = 1000 and under 10 seconds for sq_limit = 1500

