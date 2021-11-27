#Написати функцію, яка приймає на вхід список
#і підраховує кількість однакових елементів у ньому.
def num_repet(my_list):
    a = list(my_list)
    result = dict((i, a.count(i)) for i in a)
    return result
my_list = str(input("Введіть список: \n"))
print(num_repet(my_list))
