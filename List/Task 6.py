# Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран это значение
import random

n = []
fix = []
lop = 0
for i in range(10):
    n.append(random.randint(1, 10))
    if n.count(n[i]) > 1:
        fix.append(n[i])
        i += 1
for x in fix:
    if fix.count(x) > 1:
        fix.remove(x)
print(n)
print("Повторяющееся значения: ", fix)
