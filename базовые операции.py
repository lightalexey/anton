a = 'мама мыла раму'
b = 'а папа мыл пол.'
s = a + ', ' + b
print('Исходная строка:',s)
print('Первый символ:', s[0])
print('Длина:', len(s))
print('Последний символ:', s[len(s)-1])
print('или так:', s[-1])
# s[0] = 'М' : так работать не будет!!! Строку изменить нельзя!!!
s = 'М' + s[1:]
print(s)
s = s.replace('М', 'м')
print(s)
s = s.replace('м', 'М', 1)
print(s)
s = s.replace('папа', 'брат')
print(s)
k_a = 0 # количество букв а
for i in s:
    if i == 'а':
        k_a += 1
print('1 способ. Количество букв а равно', k_a)
k_a = 0 # количество букв а
for i in range(len(s)):
    if s[i] == 'а':
        k_a += 1
print('2 способ. Количество букв а равно', k_a)
k_a = s.count('а')
print('2 способ. Количество букв а равно', k_a)
if 'брат' in s:
    print('В строке есть слово брат')
else:
    print('В строке нет слова брат')
# количество гласных
k = 0
for i in s:
    if i in 'аоеиуэюя':
        k += 1
print(k)
