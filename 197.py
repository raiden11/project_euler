
import math 

u = -1
power = 30.403243784
s = set({-1})
for i in range(1, 550):
    p = math.floor(2**(power-u*u))*(0.000000001)
    if p in s:
        print("founddd: ", i)  # the sequence starts repeating itself at i = 518 and oscillates between two values
        break
    s.add(p)
    u = p

# print(1.029461839 + 0.681175878)
