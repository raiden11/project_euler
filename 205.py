
from collections import defaultdict

# Logic
# We recursively calculate the frequency of each sum appearing for both boys. This can also be done with 9 loops for peter and 6 for colin
# Then we iterate over possible sums for peter's die and find the sum of frequencies of colin's die when colin's sum < peter's sum

peter = [1, 2, 3, 4]
colin = [1, 2, 3, 4, 5, 6]
peter_die_count = 9
colin_die_count = 6

def generate_sum_frequencies(dice_id, max_dices, faces, rolling_sum, frequencies):
    if dice_id > max_dices:
        frequencies[rolling_sum] += 1
        return
    for face in faces:
        generate_sum_frequencies(dice_id + 1, max_dices, faces, rolling_sum + face, frequencies)

peter_freq = defaultdict(int)
generate_sum_frequencies(1, peter_die_count, peter, 0, peter_freq)
colin_freq = defaultdict(int)
generate_sum_frequencies(1, colin_die_count, colin, 0, colin_freq)

assert len(peter)**peter_die_count == sum(peter_freq.values())
assert len(colin)**colin_die_count == sum(colin_freq.values())

denominator = len(peter)**peter_die_count*len(colin)**colin_die_count
numerator = 0
for peter_sum, peter_sum_freq in peter_freq.items():
    for colin_sum, colin_sum_freq in colin_freq.items():
        if colin_sum < peter_sum:
            numerator += (peter_sum_freq*colin_sum_freq)

print(round(numerator/denominator, 7))

