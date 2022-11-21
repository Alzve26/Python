# Найти наибольший элемент списка и вывести его на экран
import random

n = []
for i in range(10):
    n.append(random.randint(1, 100))
n.sort()
print(n)
print(n[9])
