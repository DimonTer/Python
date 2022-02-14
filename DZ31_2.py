y = []
x = str(input('Enter  '))
for i in x:
    if i not in y:
        y.append(i)

print( "Колличество символов"  ,  len(x))
print( "Колличество уникальных символов"  ,  len(y))
