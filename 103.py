
required_length = 7

# First half i.e. the code for calculating the subset pairs to check for is copied from problem 106
# def generate_subsets(candidate_set):
#     n = len(candidate_set)
#     candidate_set_list = list(candidate_set)
#     subsets = []
#     for i in range(1, (1 << n) - 1):  # we can ignore the full set and empty set
#         subset = set()
#         for j in range(0, n):
#             if (i & (1 << j)) != 0:
#                 subset.add(candidate_set_list[j])
#         subsets.append(subset)
#     return subsets

# representative_set = set() # represents the positions of elements in the set i.e. for n = 5, it is {1, 2, 3, 4, 5}
# for i in range(0, required_length):
#     representative_set.add(i)

# # generate all subsets of the representative set
# subsets = generate_subsets(sorted(representative_set))
# interesting_subset_pairs = []

# # iterate over all pairs of subsets (subset, subsets[j]) of the representative set, goal is to find pairs that should be tested
# for i in range(len(subsets)):
#     for j in range(i + 1, len(subsets)):
#         if len(subsets[j].intersection(subsets[i])) == 0 and len(subsets[i]) > 1 and len(subsets[j]) > 1: # proceed if the pairs have no common element
#             interesting_subset_pairs.append((list(subsets[i]), list(subsets[j])))

def generate_subsets(candidate_set):
    n = len(candidate_set)
    candidate_set_list = list(candidate_set)
    subsets = []
    for i in range(1, 1 << n):
        subset_list = []
        for j in range(0, n):
            if (i & (1 << j)) != 0:
                subset_list.append(candidate_set_list[j])
        subsets.append(subset_list)
    return subsets

def check_special_sum_set(candidate_set):
    subsets = generate_subsets(candidate_set)
    # print(len(subsets), subsets)
    for i in range(0, len(subsets)):
        for j in range(i + 1, len(subsets)):
            if sum(subsets[i]) == sum(subsets[j]):
                return "same sum", subsets[i], subsets[j]
            elif (len(subsets[i]) > len(subsets[j]) and sum(subsets[i]) <= sum(subsets[j])) or (len(subsets[i]) < len(subsets[j]) and sum(subsets[i]) >= sum(subsets[j])):
                return "second fail", subsets[i], subsets[j]
    return None, None, None

# def get_sum(candidate_list, positions):
#     sum = 0
#     for position in positions:
#         sum += candidate_list[position]
#     return sum

# def check_special_sum_set(candidate_list):
#     for pair in interesting_subset_pairs:
#         left_sum = get_sum(candidate_list, pair[0])
#         right_sum = get_sum(candidate_list, pair[1])
#         # print(pair, left_sum, right_sum)
#         if left_sum == right_sum:
#             return False
#     print("FOUND: ", candidate_list)
#     return True

min_sum = 100000000
set_found = []
for first_element in range(15, 26):
    for second_element in range(first_element + 1, first_element + 13):
        last_element_limit = first_element + second_element - 1
        for third_element in range(second_element + 1, last_element_limit - 3):
            for fourth_element in range(third_element + 1, last_element_limit - 2):
                for fifth_element in range(fourth_element + 1, last_element_limit - 1):
                    for sixth_element in range(fifth_element + 1, last_element_limit):
                        for seventh_element in range(sixth_element + 1, last_element_limit + 1):
                            candidate_set = {first_element, second_element, third_element, fourth_element, fifth_element, sixth_element, seventh_element}
                            candidate_set_sum = sum(candidate_set)
                            if candidate_set_sum <= min_sum:
                                # print(candidate_set)
                                a, b, c = check_special_sum_set(candidate_set)
                                if a == None:
                                    print("Found: ", candidate_set)
                                    # print(candidate_set)
                                    if candidate_set_sum < min_sum:
                                        min_sum = candidate_set_sum
                                        set_found = [candidate_set]
                                    else:
                                        set_found.append(candidate_set)

print("answer: ", min_sum, set_found)

# These are the possibilities of a 7 element special sum set - sum of 1st and 2nd element is more than the last element
# Range of first element estimated by the optimum 6 element set
# As per the solution of problem 106, 70 subset pairs need to be checked for same sum, if none matches, it's a special sum set
# let's assume second element is x. Let's search so that first elem + x > last element and x - first <= 12
# 5 blanks need to be filled
# 15, _, _, _, _, _, 30 [13 spaces]
# 16, _, _, _, _, _, 32 [13 spaces]
# 17, _, _, _, _, _, 34 [13 spaces]
# 18, _, _, _, _, _, 36 [13 spaces]
# 19, _, _, _, _, _, 38 [13 spaces]
# 20, _, _, _, _, _, 40 ...
# 21, _, _, _, _, _, 42 ...
# 22, _, _, _, _, _, 44 ...
# 23, _, _, _, _, _, 46 ...
# 24, _, _, _, _, _, 48 ...
# 25, _, _, _, _, _, 50 [23 spaces]

