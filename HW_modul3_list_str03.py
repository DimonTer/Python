x = str(input('Enter text  '))
y = str(input('searching for  '))
n = 0
for i in x:
    if i == y:
        n += 1

print(n)
