

for num in range(3, 100):
    if num % 2 == 0 or num % 5 == 0:
        continue
    consecutive_1 = 1
    exponent = 1
    
    print(f"Number is {num}")
    while True:
        power_10 = 10**exponent
        consecutive_1 += power_10
        remainder1 = None
        remainder2 = None
        if power_10 >= num:
            remainder1 = power_10 % num
        if consecutive_1 >= num:
            remainder2 = consecutive_1 % num
        print(exponent, consecutive_1, remainder1, remainder2)
        if remainder2 == 0:
            break

        exponent += 1
    print()



