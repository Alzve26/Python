import random
n = []
for i in range(10):
    n.append(random.randint(1, 10))
n.sort()
maxi = n[-1]
mini = n[0]
n[0] = maxi
n[-1] = mini
print(n)