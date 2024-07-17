
def sum_digits(num):
    ans = 0
    while(num):
        ans += num % 10
        num //= 10
    return ans

powers = set()
for i in range(1, 5000):
    powers.add(i**1)

for i in range(1, 10000000):
    powers.add(i**2)
    powers.add(i**3)

for i in range(1, 100000):
    powers.add(i**4)
    powers.add(i**5)

for i in range(1, 10000):
    powers.add(i**6)
    powers.add(i**7)
    powers.add(i**8)
    powers.add(i**9)

for i in range(1, 1000):
    powers.add(i**10)
    powers.add(i**11)
    powers.add(i**12)

print(len(powers))

cnt = 0
for num in sorted(powers):
    # print(num)
    digsum = sum_digits(num)
    for i in range(1, 12):
        if num > 10 and num == digsum**i:
            print(cnt, digsum, num, i)
            cnt += 1


# submitted incorrect: 3904305912313344


