#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
def iterate(*args):
    try:
        if len(args) == 1:
            a = 0
            b = float(args[0])
            step = 1
        elif len(args) == 2:
            a = float(args[0])
            b = float(args[1])
            step = 1
        elif len(args) == 3:
            a = float(args[0])
            b = float(args[1])
            step = float(args[2])
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
    else:
        yield ""

print(type(iterate(1, 10, 2)))

for i in iterate(12,2,-2):
    print(i)
