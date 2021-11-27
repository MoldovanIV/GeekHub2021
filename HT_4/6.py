#Вводиться число.
#Якщо це число додатне, знайти його квадрат,
#якщо від'ємне, збільшити його на 100,
#якщо дорівнює 0, не змінювати.
def num_oper(n):
    if n > 0:
        print(n*n)
    elif n < 0:
        print(n+100)
    else:
        print(n)
    return 
num = float(input("Введіть число: "))
num_oper(num)
                     
