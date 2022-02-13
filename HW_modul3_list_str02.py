x = str(input('Enter text  '))
c = 0
n = 0
for i in x:
    if i.isalpha():
        c += 1
    elif i.isdigit():
        n += 1

print(c, n)

