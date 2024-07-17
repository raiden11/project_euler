
import itertools

candidates = []
def check_magic(perm, size):
    if size == 3 and perm[0] + perm[1] + perm[2] == perm[3] + perm[2] + perm[4] == perm[5] + perm[4] + perm[1]:
        groups = [""]*size
        groups[0] = str(perm[0]) + str(perm[1]) + str(perm[2])
        groups[1] = str(perm[3]) + str(perm[2]) + str(perm[4])
        groups[2] = str(perm[5]) + str(perm[4]) + str(perm[1])
        first_nodes = [(perm[0], 0), (perm[3], 1), (perm[5], 2)]
        first_nodes = sorted(first_nodes)
        count = 0
        index = first_nodes[0][1]
        candidate_string = ""
        while count < size:
            candidate_string += groups[index]
            index = (index + 1) % size
            count += 1
        candidates.append(candidate_string)
    
    elif size == 5 and perm[0] + perm[1] + perm[2] == perm[3] + perm[2] + perm[4] == perm[5] + perm[4] + perm[6] == perm[7] + perm[6] + perm[8] == perm[9] + perm[8] + perm[1]:
        groups = [""]*5
        groups[0] = str(perm[0]) + str(perm[1]) + str(perm[2])
        groups[1] = str(perm[3]) + str(perm[2]) + str(perm[4])
        groups[2] = str(perm[5]) + str(perm[4]) + str(perm[6])
        groups[3] = str(perm[7]) + str(perm[6]) + str(perm[8])
        groups[4] = str(perm[9]) + str(perm[8]) + str(perm[1])
        first_nodes = [(perm[0], 0), (perm[3], 1), (perm[5], 2), (perm[7], 3), (perm[9], 4)]
        first_nodes = sorted(first_nodes)
        count = 0
        index = first_nodes[0][1]
        candidate_string = ""
        while count < size:
            candidate_string += groups[index]
            index = (index + 1) % size
            count += 1
        candidates.append(candidate_string)

for permutation in list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])):
    check_magic(permutation, 5)

sorted_candidates = sorted(candidates)
print(sorted_candidates[-1])
print(len(sorted_candidates))

