import random as rand

n = rand.randint(3, 20)
print(n)
result = ''

for i in range(1, 20):
    if i > n/2:
        break
    for j in range(1, 20):
        if i == j:
            continue
        elif i+j == n:
            result += str(i)
            result += str(j)
        else:
            continue

print(result)