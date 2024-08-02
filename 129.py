
max_power_number = -1
max_power = -1
start = 1000000
for num in range(start, 100000000):
    if num % 2 == 0 or num % 5 == 0:
        continue
    exponent = 1
    remainder1 = 1
    remainder2 = 1
    while True:
        # print(num, remainder, exponent)
        remainder1 = remainder1 * 10
        remainder2 = remainder2 + remainder1
        if remainder1 >= num:
            remainder1 %= num
        if remainder2 >= num:
            remainder2 %= num
        if remainder2 == 0:
            break
        exponent += 1
        
    print(f"Number is {num} {exponent + 1}")
    if exponent + 1 > start:
        print("Found it!!!!")
        exit(0)






