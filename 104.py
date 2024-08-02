
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

# print(check_pandigital_first_and_last_9_digits(246579381829598263586239510035097230562836512000087125145697283))

# assuming both matrices are 2X2
def matmul(m1, m2):
    return [[m1[0][0]*m2[0][0] + m1[0][1]*m2[1][0], m1[0][0]*m2[0][1] + m1[0][1]*m2[1][1]], 
            [m1[1][0]*m2[0][0] + m1[1][1]*m2[1][0], m1[1][0]*m2[0][1] + m1[1][1]*m2[1][1]]]
    
def matrix_power(base, power):
    if power == 1:
        return base
    m_half_power = matrix_power(base, power//2)
    m_power = matmul(m_half_power, m_half_power)
    if power % 2 == 0:
        return m_power
    else:
        return matmul(m_power, base)

def generate_ith_fibonacci(f1, f2, i):
    m_power_n = matrix_power([[1, 1], [1, 0]], i)
    f_n_plus_1 = m_power_n[0][0]*f1 + m_power_n[0][1]*f2
    f_n = m_power_n[1][0]*f1 + m_power_n[1][1]*f2
    return f_n

# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
for i in range(3, 1000000):
    c = a + b
    if c >= 1000000000:
        c%=1000000000
    if is_pandigital(c):
        number = generate_ith_fibonacci(1, 1, i-1)
        print(f"checking for {i}")
        if is_pandigital(extract_first_9_digits(number)):
            print(f"Found the answer for i = {i} !!")
            exit(1)
    a = b
    b = c
