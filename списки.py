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

umn = 1
for i in a:
    if i != 0:
        umn *= i
print(umn)

print(sum(a) / len(a))

q = 0
w = 0
for i in a:
     if  i > 0:
         q += i
         w += 1
print(q / w)

e = 0
for i in a:
    if i % 2 == 0:
        e += 1
print(e)

