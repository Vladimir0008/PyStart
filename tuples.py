#кортежи
import lists

tpl = ('a', 'b', 'c')
tpl2 = ('a', 'b', 'c')
print(tpl[1])

res = tpl + tpl2
print(res)

tst = ([1, 2, 3], True, 'a', 'b')
print(tst)

tpl = tuple('abcde')
print(tpl) # выведет ('a', 'b', 'c', 'd', 'e')


tpl = (1,2,3,4)
print(tpl) # выведет ошибку

tst = 98765
tst = str(tst)
tpl = tuple(tst)
print(tpl)

tst = (True,)
print(tst)

tpl = ('a', 'b', 'c')
print(tpl[0]) # выведет 'a'

tpl = (10, 9, 8, 7, 6)
print(tpl[-1])
result = int(tpl[0]) + int(tpl[1])
print(result)

tpl = ('a', 'b', 'c')
# tpl[0] = '!'
# print(tpl) # выведет ошибку

tpl = ('1', 'b', '3', 'd', '5')
print(len(tpl))


tpl1 = ('a', 'b')
tpl2 = (1, 2)
res = tpl1*2 + tpl2
print(res)

tpl = ('1', '2', '3')
res = '1' in tpl

print(res)

tpl1 = ('ac', '3', 4, 'bd', 5)
tpl2 = (1, 2, 3)

res1 = 4 in tpl1
res2 = 2 not in tpl2
print(res1)
print(res2)

tpl = (2, 6, 14)

i1, i2, i3 = tpl
res = i1 + i2 + i3
print(res)

tpl = ('a', 'b', 'c')
res = list(tpl)

print(res) # выведет ['a', 'b', 'c']

tpl = ('a', 'b', 'c')
txt = '-'.join(tpl)

print(txt) # выведет 'a-b-c'

tpl = ('1', '2', '3', '4', '5')
res = '-'.join(tpl)
print(res)

tpl = ('1', '2', '3', '4', '5')
s = ''.join(tpl)
print(s)

txt = 'abcde'
res = txt[1:3]

print(res) # выведет 'bc'

txt = '12345'
res = txt[1:4]
print(res)

lst = [1, 2, 3, 4, 5, 6, 7]
res = lst[0:3]
print(res)

lst = [1, 2, 3, 4, 5, 6, 7]
res = lst[1:6]
print(res)


txt = 'abcde'
res = txt[2:]
print(res) # выведет 'cde'

lst = ['ab', 1, 'cd', 2, 'ef', 3, 4]
res = lst[-1:]
print(res)

txt = '123456789'
res = txt[0:9:2]

print(res) # выведет '2468'

txt = '123456789'
res = txt[1:-1:2]
print(res)

txt = '123456789'
res = txt[1::2]
print(res)

lst = ['a', 'b', 'c', 'd', 'e']

res = lst[::3]
print(res)

txt = '123456789'
res = txt[2::3]

print(res) # выведет '2468'

lst = (1, 2, 3, 4, 5, 6, 7)
weekdays = lst[:5]
weekdend = lst[5:]
print(weekdays)
print(weekdend)

lst = [1, 2, 3, 4, 5, 6, 7]
weekdays = lst[:5]
weekdend = lst[5:]
print(weekdays)
print(weekdend)

lst = '1234567'
weekdays = lst[:5]
weekdend = lst[5:]
print(weekdays)
print(weekdend)


txt1 = 'abcde'
txt2 = txt1[::-1]

print(txt2) # выведет 'edcba'
print(txt1) # выведет 'abcde'

txt = '123456789'

lst = [1, 2, 3, 4, 5, 6]
del lst[:]

print(lst) # выведет []

#txt = '123456789'
#del txt[1:3] # выведет ошибку

dct = {}
dct = {
	'a': 1,
	'b': 2,
	'c': 3
}

print(dct)

dct = dict(a='1', b='2')
print(dct) # выведет {'a': '1', 'b': '2'}

dct = {
	'x': 1,
	'y': 2,
	'z': 3
}

result = 0
for i in dct:
	print(dct[i])
	result += int(dct[i])
print(result)

dct = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct['asdasda'] = 112321
dct['asdasd1'] = 112322
dct['a'] = 2112

print(dct)