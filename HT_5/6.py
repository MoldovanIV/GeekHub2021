#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
def iterate(*args):
    try:
        if len(args) == 1:
            a = 0
            b = int(args[0])
            step = 1
        elif len(args) == 2:
            a = int(args[0])
            b = int(args[1])
            step = 1
        elif len(args) == 3:
            a = int(args[0])
            b = int(args[1])
            step = int(args[2])
            if step == 0:
                raise ValueError("Крок не може дорівнювати 0")
        else:
            raise TypeError("Надто багато аргументів")
    except ValueError as e:
        print(e)
        return
    except TypeError:
        print("Генератор приймає від 1 до 3 аргументів!")
        return

    if a <= b and step>=0:
        x = a
        while x < b:
            yield x
            x += step
    elif b <= a and step<0:
        x = a
        while x > b:
            yield x
            x += step
    elif a<=b and step <0 or a >= b and step >0:
        print("Юзер... Ти не думаюча людина! :)")


print(type(iterate(1, 10, 2)))

for i in iterate(2,20,-2):
    print(i)
