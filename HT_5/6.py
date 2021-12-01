#Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
def iterate(a, b, step=1):
    x = 0
    while abs(x) < abs(b-a):
        yield a+x
        x += step
print(type(iterate(20, 2, -2)))
for i in iterate(20, 2, -2):
    print(i)
