# Написати функцію < fibonacci >,
#яка приймає один аргумент і виводить всі числа Фібоначчі,
#що не перевищують його.
def fibonacci(n):
    rez=[]
    fib1 = 1
    fib2 = 1
    i = 1
    print(fib1)
    while (i < n):
        fib2, fib1, i = fib2+fib1, fib2, i+1
        print(fib1)
    return 
numb_fib = int(input("Введіть номер елемента ряду Фібоначчі n = "))
fibonacci(numb_fib)


