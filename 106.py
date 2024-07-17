
# Function to generate and return all subsets of a given set 
def generate_subsets(candidate_set):
    n = len(candidate_set)
    candidate_set_list = list(candidate_set)
    subsets = []
    for i in range(1, (1 << n) - 1):  # we can ignore the full set and empty set
        subset = set()
        for j in range(0, n):
            if (i & (1 << j)) != 0:
                subset.add(candidate_set_list[j])
        subsets.append(subset)
    return subsets

required_length = 12
representative_set = set() # represents the positions of elements in the set i.e. for n = 5, it is {1, 2, 3, 4, 5}
for i in range(1, required_length + 1):
    representative_set.add(i)

# generate all subsets of the representative set
subsets = generate_subsets(sorted(representative_set))

answer = 0
candidates = 0 # Number of candidate pairs i.e. the have no common element

# iterate over all pairs of subsets (subset, subsets[j]) of the representative set, goal is to find pairs that should be tested
for i in range(len(subsets)):
    for j in range(i + 1, len(subsets)):
        if len(subsets[j].intersection(subsets[i])) == 0: # proceed if the pairs have no common element
            candidates += 1
            if len(subsets[i]) == len(subsets[j]) and len(subsets[i]) > 1: # subset size should be same and one element pairs cannout be same as it's an increasing sequence 
                weight = 0
                 # Main logic: sort both the pairs. If sub1[i] > sub2[i] or sub1[i] < sub2[i] for all i, one set's sum definitely has to be larger. Hence, reject them.
                for num1, num2 in zip(sorted(subsets[i]), sorted(subsets[j])):
                    if num1 > num2:
                        weight += 1
                    else:
                        weight -= 1
                if abs(weight) != len(subsets[i]):
                    # print(subset, subsets[j])
                    answer += 1

print(candidates, answer)
