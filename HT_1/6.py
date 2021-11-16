my_list=[]
n=int(input("Введіть кількість елементів вашого списку n="))
for num in range(n):
    x=int(input("Введіть число (елемент списку):  "))
    my_list.append(x)
a=int(input("Число для перевірки:"))
print(a," =>",my_list,":", a in my_list)
b=int(input("Число для перевірки:"))
print(b," =>",tuple(my_list),":", b in my_list)

