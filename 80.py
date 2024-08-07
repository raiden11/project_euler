
import math

# logic 
# This is an implementation of the long division method to calculate square roots
# Someone in the threads solved it using the Newton-Raphson method

answer = 0
limit = 100
required_decimal_digits = 100

for number in range(2, limit):
    first_digit = int(math.floor(math.sqrt(number)))
    remainder = number - first_digit*first_digit 
    running_result = first_digit
    if remainder == 0:      # ignoring square numbers
        continue
    sum = first_digit
    for i in range(0, required_decimal_digits-1):
        dividend = remainder*100
        for j in range(0, 11):
            divisor = running_result*20 + j
            if divisor * j > dividend:
                next_digit = j - 1                
                sum += next_digit
                remainder = dividend - ((running_result*20 + next_digit)*next_digit)
                running_result = running_result * 10 + next_digit
                break

    answer += sum
print(answer)
