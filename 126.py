
s = set()
for i in range(1, 50):
    for j in range(1, 50):
        for k in range(1, 50):
            if i*j + j*k + k*i == 59:
                s.add(tuple(sorted([i, j, k])))

print(s)
