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