import math

# Logic
# The total number of discs are always increasing by a factor of 5.8284xxxxx
# By brute force, I found one of the solution for total discs to be 137904
# Next solution would be between 137904*5.8284 and 137904*5.8285 and so on...

# Brute force
# limit = 1000000000000
# limit = 1
# for i in range(limit, 10000000000000000000):
#     if i % 4 == 0 or i % 4 == 1:
#         sq = i*i + (i-1)*(i-1)
#         sq_root = round(math.sqrt(sq))
#         if sq_root * sq_root == sq:
#             # print(sq_root, sq, sq_root*sq_root)
#             print(f"Total disks = {i}, Blue disks = {(sq_root + 1)//2}")
#             # break

last_solution = 137904
while last_solution < 1000000000000:
    start = math.floor(5.8284*last_solution)
    end = math.ceil(5.8285*last_solution)
    for i in range(start, end+1):
        if i % 4 == 0 or i % 4 == 1:
            sq = i*i + (i-1)*(i-1)
            sq_root = round(math.sqrt(sq))
            if sq_root * sq_root == sq:
                # print(sq_root, sq, sq_root*sq_root)
                last_solution = i
                print(f"Total disks = {i}, Blue disks = {(sq_root + 1)//2}")
                break

# Solutions
# Total disks = 1, Blue disks = 1
# Total disks = 4, Blue disks = 3
# Total disks = 21, Blue disks = 15
# Total disks = 120, Blue disks = 85
# Total disks = 697, Blue disks = 493
# Total disks = 4060, Blue disks = 2871
# Total disks = 23661, Blue disks = 16731
# Total disks = 137904, Blue disks = 97513
# Total disks = 803761, Blue disks = 568345
# Total disks = 4684660, Blue disks = 3312555
# Total disks = 27304197, Blue disks = 19306983
# Total disks = 159140520, Blue disks = 112529341
# Total disks = 927538921, Blue disks = 655869061
# Total disks = 5406093004, Blue disks = 3822685023
# Total disks = 31509019101, Blue disks = 22280241075
# Total disks = 183648021600, Blue disks = 129858761425
# Total disks = 1070379110497, Blue disks = 756872327473
