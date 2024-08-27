for i in range(1,6,4):
    print(i)

count = 0
word = "Hello World!"
for i in word:
    if i=="l":
        count+=1
print("Count:", count)

i = 5
while i<=15:
    print(i)
    i +=2

for i in range(1,11):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

"""isHasCar = True
while isHasCar:
    if input("Enter data: ") == "Stop":
        isHasCar = False"""