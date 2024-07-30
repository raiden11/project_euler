import itertools

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
operators = ['+', '-', '*', '/']
combinations = list(itertools.combinations(digits, 4))
all_operators_order = [p for p in itertools.product(operators, repeat=3)]
print(len(all_operators_order))

def apply(num1, num2, operator):
    if operator == operators[0]:
        res = num1 + num2
    elif operator == operators[1]:
        res = num1 - num2
    elif operator == operators[2]:
        res = num1 * num2
    else:
        if num2 == 0:
            raise Exception
        else:
            res = num1 / num2
    return res

j = 1
global_max_target = -1
for combination in combinations:
    possible_results = set()
    for perm in itertools.permutations(list(combination)):
        for order in all_operators_order:
            try:
                res1 = apply(apply(apply(perm[0], perm[1], order[0]), perm[2], order[1]), perm[3], order[2])  # (((1*2)*3)*4)
                if res1 > 0 and res1%1 ==0: possible_results.add(res1)
            except:
                pass
            try:
                res2 = apply(apply(perm[0], perm[1], order[0]), apply(perm[2], perm[3], order[2]), order[1])  # ((1*2)*(3*4))
                if res2 > 0 and res2%1 ==0: possible_results.add(res2)
            except:
                pass
            try:
                res3 = apply(perm[0], apply(apply(perm[1], perm[2], order[1]), perm[3], order[2]), order[0])  # (1*((2*3)*4))
                if res3 > 0 and res3%1 ==0: possible_results.add(res3)
            except:
                pass
            try:
                res4 = apply(apply(perm[0], apply(perm[1], perm[2], order[1]), order[0]), perm[3], order[2])  # ((1*(2*3))*4)
                if res4 > 0 and res4%1 ==0: possible_results.add(res4)
            except:
                pass
            try:
                res5 = apply(perm[0], apply(perm[1], apply(perm[2], perm[3], order[2]), order[1]), order[0])  # (1*(2*(3*4)))
                if res5 > 0 and res5%1 ==0: possible_results.add(res5)
            except:
                pass

    targets = list(sorted(possible_results))
    j += 1

    if targets[0] != 1:
        continue
    max_target = 1
    for i in range(1, len(targets)):
        if targets[i] - targets[i-1] != 1:
            break
        else:
            max_target = targets[i]
    if max_target > global_max_target:
        global_max_target = max_target
        print(global_max_target, combination)

    # print(j, combination, targets)
    

