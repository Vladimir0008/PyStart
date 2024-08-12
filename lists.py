lst = ['1', '2', '3'] # строки
lst = [1, 2, 3] # числа
lst = [True, False] # булевые значения
lst = [['a', 'b'], ['c', 'd']] # списки

#Также в списке одновременно могут находиться разные типы данных:

lst = [1, 'a', True] # число, строка, булевое значение

print(lst)

lst1 = ['ab', 'cd', 'ef']
print(lst1)

lst = list('abcde')
print(lst)

tst = list('5678')
print(tst)

txt = '1-2-3-4'
print(txt.split('-')) # выведет ['1', '2', '3', '4']

txt = 'ab 12 cd'
print(txt.split(' '))

txt = '123_45'
print(txt.split())

lst = [1, 2, 3, 4, 5]
print(lst[-1])

lst = [2, 4, 6, 8]
res = lst[3] - lst[0]

print(res)

tst = '12abc45'
lst = list(tst)
print(len(lst))

lst = []
lst.append('1')
print(lst)
lst.append('a')
lst.append('b')
lst.append('c')
print(lst)

lst = [1, 2, 3, 4, 5]
lst.insert(2, 'a')
print(lst)
lst.insert(0,0)
lst.append(0)
print(lst)

lst1 = [1, 2, 3]
lst2 = [4, 5, 6]

lst1.extend(lst2)
print(lst1) # выведет [1, 2, 3, 4, 5, 6]

lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst3 = [1, 2, 3]

print(lst1 + lst2 + lst3)

lst1.extend(lst3)
lst1.extend(lst2)
print(lst1)

lst = [1, 2, 3]
del lst[0]

print(lst) # выведет [2, 3]

lst = ['a', 1, 'b', 2, 'c', 3]
del lst[0]
del lst[1]
del lst[2]
print(lst)

lst33 = ['b', 'c', 1, 2, 'b', 'c']
i = 0
while i < len(lst33):
    val = lst33[i]
    print(val)
    j = i+1
    i = i + 1
    while j < len(lst33):
        if str(val) == str(lst33[j]):
            lst33.remove(val)
            lst33.remove(val)
            i = 0
            break
        else: j = j + 1
print('aaa')
print(lst33)


lst = [1, 2, 3]
print(lst.pop()) # выведет 3
print(lst) # выведет [1, 2]

lst = [1, 2, 3]
lst2 = [4, 5, 6]
print(lst + lst2)
lst.clear()

print(lst) # выведет []

lst = [1, 3, 'a', 'b', 3, 6]
tst = 3

print(lst.index(tst))

lst = [1, 2, 3]
print(lst.index(1)) # выведет 0

lst = [1, 2, 3]
res = 33 in lst
if res:
    print(lst.index(res))
else: print('none')


lst = [1, 2, 1, 3]
print(lst.count(4)) # выведет 0
print(lst.count(1)) # выведет 2