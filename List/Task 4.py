# Найдите сумму и произведение элементов списка. Результаты вывести на экран
import random
n = []
for i in range(11):
    n.append(random.randint(1, 100))
print(n)
l = n[0]
p = n[0]
for k in range(10):
    k += 1
    l *= n[k]
    p += n[k]
print("Произведение: ", l, "\nСложение: ", p)
