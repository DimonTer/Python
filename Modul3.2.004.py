min = 0
max = 0
sum = 0

while True:
    x = int(input ('Введите число '))
    sum += x
    if x == 7:
        break
    elif x > max:
        max = x
    elif x < max:
        min = x
print (max)
print (min)
print ((sum - 7))
print('Good bay')
