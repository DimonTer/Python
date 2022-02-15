y = [3, 4, 6, 77, 3, 11, 54, 3, 11, 6, 7]
while True:
    try:
        x = input('Введите номер ячейки  ')
        print(y[int(x)])
    except ValueError:
        print('Вы ввели не число')
    except IndexError:
        print('Вы ввели не корректный  номер ячейки')
