a= int(input ('Введите первое число   '))
b=int(input ('Введите второе число   '))
y=str(input ('введите функцию '))
if y=='+':
    z=a+b
    print('результат', z)
elif y== '-':
    z=a-b
    print('результат', z)
elif y=='*':
    z=a*b
    print('результат', z)


elif y=='/':
    if b==0:
        print ('делить на ноль нельзя')
    z=a/b
    print('результат', z)
