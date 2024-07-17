
from collections import defaultdict, Counter

# DISCLAIMER: THIS CODE WILL NOT PROVIDE THE CORRECT ANSWER 
def preprocessing_words():
    file_name = "problem_98_words.txt"
    words_dict = defaultdict(list)
    with open(file_name, "r") as file:
        for line in file:
            words = line.split(",")
    a = 0
    for word in words:
        a += 1
        word = word[1:-1]
        if len(set(word)) > 10:
            continue
            
        counter = Counter(word)
        wordstr = ""
        for letter in range(65, 91):
            wordstr += str(counter[chr(letter)])
        # wordstr = ''.join(sorted(wordstr, reverse=True))
        words_dict[(wordstr, len(word))].append(word)
    return words_dict


def preprocessing_squares():
    # digits_dict = defaultdict(list)
    possible_numbers = []
    for i in range(1, 100000):
        sq_str = str(i*i)
        consecutive_3 = False
        for j in range(0, len(sq_str)-2):
            if sq_str[j] == sq_str[j+1] and sq_str[j] == sq_str[j+2]:
                consecutive_3 = True
                break
        if consecutive_3:
            continue
        possible_numbers.append(i*i)
        # a = Counter(sq_str)
        # numstr = ""
        # digits = 0
        # for j in range(0, 10):
        #     digit_count = a[str(j)]
        #     numstr += str(digit_count)
        #     digits += digit_count
        # numstr = ''.join(sorted(numstr, reverse=True))
        # digits_dict[(numstr, digits)].append(i*i)
    return possible_numbers

squares_dict = preprocessing_squares()
words_dict = preprocessing_words()
# print(words_dict)
# print(squares_dict)

def word_fits_number(word, number):
    numstr = str(number)
    digitkey = defaultdict(None)
    digitkey_inverted = defaultdict(None)
    if len(numstr) != len(word):
        return False
    # print("trying to match: ", numstr, word)
    for letter, digit in zip(word, numstr):
        # print(word, numstr)
        if (letter in digitkey and digitkey[letter] != digit) or (digit in digitkey_inverted and digitkey_inverted[digit] != letter):
            return False
        digitkey[letter] = digit
        digitkey_inverted[digit] = letter
    return True

# print(word_fits_number("ACT", 100))
# exit(1)
answer = -1
for key, values in words_dict.items():
    anagram_max = 0
    all_matches = []
    if len(values) > 1:
        print(values)
    for word in values:
        any_match = False
        for number in squares_dict:
            if word_fits_number(word, number):
                any_match = True
                all_matches.append((word, number))
        if any_match:
            anagram_max += 1
    if anagram_max > 1:
        print(all_matches)
        for match in all_matches:
            if match[1] > answer:
                answer = match[1]
 
print("Final answer is : ", answer)


# 923187456

ans = 0
for i in range(1, 100000):
    if len(str(i*i)) == 9 and len(set(str(i*i))) == 9:
        print(i*i)

REDUCTION

