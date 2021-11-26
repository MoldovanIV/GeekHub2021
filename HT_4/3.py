#Написати функцию < is_prime >, яка прийматиме 1 аргумент - число від 0 до 1000,
#яка вертатиме True, якщо це число просте, False - якщо ні.
def is_prime(num):
    if num >= 2:
        k = 0
        for i in range(2, num // 2+1):
            if (num % i == 0):
                k = k+1
        if (k <= 0):
            answer = 'True'
        else:
            answer = 'False'
    else:
        answer = 'Введене число не є простим.\nПрості числа - це натуральні числа.\nНайменше просте число - це 2.'
    return answer        
cust_input = int(input("Введіть натуральне число від 0 до 1000:\n"))
if cust_input<1001 and cust_input>=0:
    print(f"Число {cust_input} просте?\nВідповідь: {is_prime(cust_input)}")
else:
    print("Введене число не з діапазону [0:1000]")
