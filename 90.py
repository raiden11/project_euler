
import itertools

def check_valid_pair(a, b):
    if not ((0 in a and 1 in b) or (1 in a and 0 in b)):
        return False
    if not ((0 in a and 4 in b) or (4 in a and 0 in b)):
        return False
    if not ((0 in a and (9 in b or 6 in b)) or ((9 in a or 6 in a) and 0 in b)):
        return False
    if not (((6 in a or 9 in a) and 1 in b) or (1 in a and (9 in b or 6 in b))):
        return False
    if not ((2 in a and 5 in b) or (5 in a and 2 in b)):
        return False
    if not ((3 in a and (6 in b or 9 in b)) or ((9 in a or 6 in a) and 3 in b)):
        return False
    if not (((9 in a or 6 in a) and 4 in b) or (4 in a and (6 in b or 9 in b))):
        return False
    if not ((4 in a and (6 in b or 9 in b)) or ((6 in a or 9 in a) and 4 in b)):
        return False
    if not ((8 in a and 1 in b) or (1 in a and 8 in b)):
        return False
    return True

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
combinations = list(itertools.combinations(digits, 6))
dice_configs = set()

for combination in combinations:
    combo = list(combination)
    combo = sorted(combo)
    dice_configs.add(tuple(combo))

dice_configs = list(dice_configs)
answer = 0
for i in range(0, len(dice_configs)):
    for j in range(i, len(dice_configs)):
        if check_valid_pair(dice_configs[j], dice_configs[i]):
            print("found: ", dice_configs[i], dice_configs[j])
            answer += 1

print(answer)

