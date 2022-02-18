in_menu = ['Гамбургер', 'Кола', 'Картошка','Соус']
while True:
    x = input("Введите название блюда ")
    if x == '':
        break
    if x in in_menu:
        in_menu.remove(x)
        print (in_menu)
    else:
        print('Такого блюда нет')
