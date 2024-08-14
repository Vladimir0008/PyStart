lst = [3, 2, 1]
lst.sort()

print(lst) # выведет [1, 2, 3]

lst = [1, 2, 3]
lst.sort(reverse=True)

print(lst) # выведет [3, 2, 1]

lst1 = ['a', 'b', 'c']
lst2 = [3, 2, 1]
lst1.sort(reverse=True)
lst2.sort()
res = []
res.extend(lst2)
res.extend(lst1)
print(res)

lst = [3, 2, 1]
res = sorted(lst)

print(res) # выведет [1, 2, 3]

lst = [4, 12, 24]
res = sorted(lst,reverse=True)
print(res)