import math

print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")
print("5 - квадратное уравнение")

button = int(input())

if button  == 1:
   a = int(input())
   b = int(input())
   c = a + b
   print(c)

if button  == 2:
   a = int(input())
   b = int(input())
   c = a - b
   print(c)

if button  == 3:
   a = int(input())
   b = int(input())
   c = a * b
   print(c)

if button  == 4:
   a = int(input())
   b = int(input())
   c = a / b
   print(c)

if button == 5:
    print("Введите a")
    a = int(input())
    print("Введите b")
    b = int(input())
    print("Введите c")
    c = int(input())
    d = (b*b) - 4*a*c
    if d < 0:
        print("корней нет")
    else:
        f = 2 * a
        if d == 0:
            x = -b/f
            print(x)
        else:
            f = 2 * a
            x1 = (-b + math.sqrt(d)) / f
            x2 = (-b - math.sqrt(d)) / f
            print(x1)
            print(x2)