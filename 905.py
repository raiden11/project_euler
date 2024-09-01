

# ayush - 16.6 
# ddpigeon - 22.8
# aayush dwiwedi - 28.1
# slfotg - 58.6
# aryanc403 - 381

# import math 
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

# def solve11(a, b, p):
#     if a == b:
#         return 1
#     else:
#         y = max(a, b)
#         x = min(a, b)
#         count = math.ceil((y-x)/x)
#         return count//2 + solve11(x, y-count*x, 1-p)


# def solve1(a, b):
#     y = max(a, b)
#     x = min(a, b)
#     count = math.ceil((y-x)/x)
#     res = count//2 + solve11(x, y-count*x, 0)
#     return res


# def solve22(a, b, p):
#     if a == b:
#         return 1
#     else:
#         y = max(a, b)
#         x = min(a, b)
#         return p + solve22(x, y-x, 1-p)

# def solve2(a, b):
#     y = max(a, b)
#     x = min(a, b)
#     res = solve22(x, y-x, 1)
#     return res


# answer = 0
# for a in range(1, 8):
#     for b in range(1, 20):
#         if a**b == b**a:
#             res = 1
#             answer += 3
#             print(a, b, 1, 1)
#         else:
            
#             res1 = solve1(a**b, b**a)
#             res2 = solve2(a**b, b**a)
#             answer = answer + (res1)*3

#             print(a, b, res1, res2)
#             # print(a**b, b**a, a**b + b**a, res1, res2)
#         # print(a**b, b**a, res)

# # print(solve(2, 5))
# print(answer)

# Tried: 140455941
# Tried: 140456313

# Solution inspired from https://arxiv.org/pdf/0710.2685

answer = 0

for a in range(1, 8):
    for b in range(1, 20):
        print(f"solving for {a, b}")
        x = a**b 
        y = b**a 
        z = x + y

        tup_c = (x, y, z, 2)
        tup_b = (x, x+z, z, 1)
        tup_a = (y+z, y, z, 0)

        conf = [[tup_a, tup_c], [tup_b, tup_c], [tup_c]]
        curr = tup_c

        while True:
            if curr[0] == curr[1] or curr[1] == curr[2] or curr[0] == curr[2]:
                break

            if curr[2] > curr[0] and curr[2] > curr[1]:
                if curr[0] > curr[1]:
                    nt = (curr[0], curr[1], abs(curr[0]-curr[1]), 0)
                else:
                    nt = (curr[0], curr[1], abs(curr[0]-curr[1]), 1)
            elif curr[1] > curr[0] and curr[1] > curr[2]:
                if curr[0] > curr[2]:
                    nt = (curr[0], abs(curr[0]-curr[2]), curr[2], 0)
                else:
                    nt = (curr[0], abs(curr[0]-curr[2]), curr[2], 2)
            else:
                if curr[1] > curr[2]:
                    nt = (abs(curr[1]-curr[2]), curr[1], curr[2], 1)
                else:
                    nt = (abs(curr[1]-curr[2]), curr[1], curr[2], 2)

            for i in range(0, 3):
                conf[i].append(nt)
            curr = nt

        for i in range(0, 3):
            conf[i] = conf[i][::-1]

        res, index = 0, 0
        max_len = min(len(conf[0]), min(len(conf[1]), len(conf[2])))
        row = 0
        while index < max_len:
            if conf[row][index][3] == row:
                index += 1
            row = (row+1)%3
            res += 1
        answer += res

print(answer)







