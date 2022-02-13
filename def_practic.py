'''print('skjhbdkwjhegckijhxhn'.upper())
print('nxnnxJJJSnnzlkAK'.lower())
print ('djshcjhdcjkhsdbvj sjhcjhdcjhdcv ikejdhvfjhkb vfd'.title())
print ('kjsdckjc qjdckcj wsxsliochj'.capitalize())
z = 'jhsdckjlcvkj'
y = z.replace('jh', 'DOOM')
x = print
x(y)
x(y.isdecimal())'''

x = input('Введите Email')
val = True
if len(x) < 8:
    val = False
elif '@' not in x:
    val = False
y = x.split('@')

print (y)
