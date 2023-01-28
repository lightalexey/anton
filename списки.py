a = [1, 2, 5, -3, 0, 9, 32, 4, 0, 5]
print(a[0], len(a), a[len(a)-1], a[-1])
summa = 0
for i in a:
    summa += i
print(summa)
summa = 0
for i in range(len(a)):
    summa += a[i]
print(summa)
print(sum(a))