shop_list = ['Морковка', 'Картошка', 'Мороженное', 'Яйца', 'Молоко']
while True:
    x = str(input('Название продукта '))
    if x in shop_list:
        shop_list.remove(x)
        print ('Вы купили', x)
    else:
        print ('Такого нет в списке покупок')
    if len(shop_list) < 1:
        break
print("Покупки завершены")
