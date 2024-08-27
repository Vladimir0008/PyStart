import sys

dct1 = {
	'a': 1,
	'b': 2,
	'c': 3
}

dct2 = {
	'x': 4,
	'y': 5,
	'z': 6
}

dct1.update(dct2) 
print(dct1)

dct1 = {
	'3': 'c',
	'4': 'd',
	'5': 'e'
}

dct2 = {
	'1': 'a',
	'2': 'b'
}

dct2.update(dct1) 
print(dct2)


result = []
for i in dct2:
    result.append(dct2[i])
    print(dct2[i])
    print(result)


    dct1 = {
	'z': 2,
	'w': 8,
	'f': 10
}

dct2 = {
	'x': 4,
	'y': 5,
	'z': 6
}

dct1.update(dct2)
print(dct1)

dct1 = {
	2: 'a',
	4: 'b',
	6: 'c'
}

dct2 = {
	1: 'd',
	3: 'e',
	4: 'f',
	7: 'j'
}

dct2.update(dct1)
print(dct2)

del dct2[1]
del dct2[3]
print(dct2)
print(dct2[4])
print(dct2.get(4))
print(dct2)
print(dct2.pop(4))
print(dct2)

print(dct2.pop(4,'sss'))

dct = {
	'surn': 'smith',
	'name': 'john',
	'age': 30
}

print(dct.keys())

dct = {
	1: 'text1',
	2: 'text2',
	3: 'text3'
}

dct.clear()
dct['sss'] = 'text4'
print(dct)
print('sss' in dct)
print('sss' not in dct)

print(dct['sss'])
print(dct.get('sss'))
print(dct.get('sssw'))

dct = {
	'aa': 'text1',
	'bb': 'text2',
	3: 'text3'
}

res = []
for i in dct:
	res.append(i)
	res.append(dct[i])
print(res)


lst = [['a', '1'], ['b', '2'], [33, 44]]
dct = dict(lst)

print(dct) # выведет {'a': '1', 'b': '2'}

tlp = ((1, 'a'), (2, 'b'))
dct = dict(tlp)

print(dct) # выведет {1: 'a', 2: 'b'}

tst = ('a', 1), ('b', 2), ('c', 3)
print(tst)
dct = dict(tst)

print(dct)

tst =(('a', 1, 3), ('b', 2, 4), ('c', 3, 0)),(('a', 1, 3), ('b', 2, 4), ('c', 3, 0))
print(tst)


dct = {
	'x': '1',
	'y': '2',
	'z': '3'
}

res = 0
for i in dct:
	res = res + int(dct[i])**2
print(res)


dct1 = {
	'1': 12,
	'2': 24,
	'3': 36
}

dct2 = {
	'a': '3',
	'b': '6',
	'c': '9'
}

res1 = 0
for i in dct1:
	res1 = res1 + dct1[i]
print(res1)

res2 = 0
for i in dct2:
	res2 = res2 + int(dct2[i])
print(res2)
print(res1 - res2)

dct = {
	1: '4',
	2: '5',
	3: '6'
}
res = ''
for i in dct:
	res = str(i) + str(dct[i])
	print(res)

dct = {
	'x': '1',
	'y': '2',
	'z': '3'
}

ress = ''
resss = ''
res = []
for i in dct:
	ress = ress + dct[i]
	resss = resss + dct[i]
	res.append(dct[i]*(int(dct[i])+1))

print((str(res)))
print('/'.join(ress))
print('-'.join(resss))