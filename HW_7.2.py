x_tupele = (1, 2, 3, 4, 5, 6, 7, 8, 9)
x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
try:
    x_list.pop(3)
    print (x_list)
    x_tupele.pop(2)
    print(x_list)
except AttributeError:
    print('не допустимая операция с данными  ')
