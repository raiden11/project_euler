
called = 0
def is_palindrome(num):
    global called
    called += 1
    str_num = str(num)
    return str_num == str_num[::-1]

answer_set = set()
cnt = 0
for i in range(1, 10000):
    j = i + 1
    sum = i*i + j*j
    while sum < 100000000:
        if is_palindrome(sum):
            print(f"{sum} is sum of number from {i} to {j}")
            answer_set.add(sum)
        j += 1
        sum += j*j

print(len(answer_set))
answer = 0
for num in answer_set:
    answer += num
print(f"answer: {answer}")
# print(sum(answer_set))
# print("called: ", called)
