x = int(input('Enter 1st nomber  '))
y = int(input('Enter 2d nomber  '))
a = 0
b = 0
c = 0
a1 = 0
b1 = 0
c1 = 0
for i in range(x,y):
    if (i % 2) != 0:
        a += 1
        a1 += i
for i in range(x,y):
    if (i % 9) == 0:
        b += 1
        b1 += i
for i in range(x,y):
    if (i % 2) == 0:
        c += 1
        c1 += i
print ('сумма нечетных', a1)
print ('средне арефметическое в группе не четных', a1/a)
print ('сумма четных', c1)
print ('средне арефметическое в группе не четных', c1/c)
print ('сумма кратных 9ти', b1)
print ('средне арефметическое в группе кратных 9ти' , b1/b)
