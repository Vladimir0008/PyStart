#кортежи


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