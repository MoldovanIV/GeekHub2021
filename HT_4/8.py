#Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку.
def shift(my_list, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            my_list.append(my_list.pop(0))
    else:
        for i in range(steps):
            my_list.insert(0, my_list.pop())
    return my_list 
 
my_l = [4, 5, 6, 7, 8, 9, 0]
print(my_l)
n = int(input("Введіть величину зсуву: "))
print(shift(my_l,n))
 
