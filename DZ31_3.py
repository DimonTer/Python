y = []
x = ['a', 'b', 'a', 'c', 'g', 'd', 'g', 'e', 'f', 'g', 'i', 'v']
for i in x:
    if i not in y:
        y.append(i)
print(y)
