
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

a, b, c = check_special_sum_set({20, 31, 38, 39, 40, 42, 45})
print(a, b, c)

def read_file_and_create_sets(file_path):
    sets_list = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip any leading/trailing whitespace and split the line by commas
            numbers = line.strip().split(',')
            # Convert each split string to an integer
            number_set = set(map(int, numbers))
            # Append the set to the list
            sets_list.append(number_set)
    return sets_list


file_path = 'problem_105_sets.txt' 
sets_list = read_file_and_create_sets(file_path)
answer = 0

for i, number_set in enumerate(sets_list):
    a, b, c = check_special_sum_set(number_set)
    if a == None:
        answer += sum(list(number_set))
        print(f"found desired set {number_set}")
    print(f"checked {i}")

print(answer)

