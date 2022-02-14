guests = ['Ратушный', 'Высоцкая', 'Иванова', 'Щепетков', 'Климчук']
in_list = guests
while True:
    x = str(input('Фамилия? '))
    if x in in_list:
        in_list.remove(x)
        print ('Проходи')
    elif len(in_list) == 0:
        break
print("Вход закрыт")
