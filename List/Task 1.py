# Заполнить список ста нулями, кроме первого и последнего элементов, которые должны быть равны единице;
n = 0
zilik = []
for i in range(100):
    zilik.append(n)
zilik[0] = 1
zilik[99] = 1
print(zilik)
