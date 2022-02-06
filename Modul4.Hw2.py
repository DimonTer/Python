c = 0
x = int(input('первое число '))
y = int(input('первое число '))
for i in range (x, y):
    if i % 5 == 0 and i % 2 != 0:
        #print (i)
        c += i
print (c)
