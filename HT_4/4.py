#Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона,
#і вертатиме список простих чисел всередині цього діапазона.
def prime_list(first,last):
    if first >= 2 and last>=first:
        rez=[]
        for num in range(first,last+1):
            prime = True
            for i in range(2,num):
                if (num%i==0):
                    prime = False
            if prime:
                rez.append(num)
    else:
        rez="Діапазон введено не коректно!"
    return rez
a = int(input("Введіть початок діапазона (натуральне число більше за 1)= "))
b = int(input("Введіть кінець діапазона (натуральне число більше за початкове значення)= "))
print(prime_list(a,b))
