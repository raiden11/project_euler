import math

for i in range(100//4, 10000000//4):
# for i in range(1000000000000 // 4, 10000000000000//4):
    num1 = (2*i)*(4*i-1)
    x = num1**0.5
    num2 = (2*i)*(4*i+1)
    y = num2**0.5
    if math.floor(x)*math.ceil(x) == num1:
        print("Found 0: ", i, 4*i, x)

    if math.floor(y)*math.ceil(y) == num2:
        print("Found 1: ", i, 4*i+1, y)

