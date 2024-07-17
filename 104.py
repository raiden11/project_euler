

a = 1 
b = 1

def is_pandigital(nine_digits):
    """Helper function to check if a number of 9 digits is pandigital."""
    digits = set()
    while nine_digits > 0:
        digit = nine_digits % 10
        if digit == 0 or digit in digits:
            return False
        digits.add(digit)
        nine_digits //= 10
    return len(digits) == 9

def extract_first_9_digits(number):
    """Extract the first 9 digits of a large number."""
    while number >= 10**9:
        number //= 10
    return number

def extract_last_9_digits(number):
    """Extract the last 9 digits of a large number."""
    return number % 10**9

def check_pandigital_first_and_last_9_digits(number):
    # Extract the first and last 9 digits
    first_9_digits = extract_first_9_digits(number)
    last_9_digits = extract_last_9_digits(number)
    
    # Check if both first 9 and last 9 digits are pandigital
    is_first_9_pandigital = is_pandigital(first_9_digits)
    is_last_9_pandigital = is_pandigital(last_9_digits)
    
    return is_first_9_pandigital and is_last_9_pandigital

# print(check_pandigital_first_and_last_9_digits(2465279381829598263586239510035097230562836512000087125145697283))

for i in range(3, 100000):
    c = a + b
    # if i == 541:
    #     print(i, c)
    if i >= 2748 and check_pandigital_first_and_last_9_digits(c):
        print("ans:", i)
    a = b
    b = c

