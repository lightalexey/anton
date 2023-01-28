a = [1, 2, 5, -3, 0, 9, 32, 4, 0, 5]
mx = a[0]
mn = a[0]
for i in range(len(a)):
    if a[i] > mx:
        mx = a[i]
    if a[i] < mn:
        mn = a[i]
print(mx,  mn)


