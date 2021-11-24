#Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
#   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
#-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
#-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
#-  якщо довжина бульше 50 - > ваша фантазiя

cust_s = str(input("Введіть випадковий рядок який містить лише символи алфавіту та цифри:\n"))
def magic (s):
    n_symb = len(s)
    if n_symb > 30 and n_symb < 50:
        n_l = sum(map(str.isalpha, s))
        n_n = sum(map(str.isnumeric, s))
        rez = str(print(f"Cимволів = {n_symb}, букв = {n_l}, цифр = {n_n}"))
    elif n_symb < 30:
        suma = 0
        for symb in s:
            if symb.isdigit():
                suma += int(symb)
        rez1 = str(print(f"Сума цифр = {suma}"))
        b_list = ''
        for symb in s:
            if symb.isalpha():
                b_list.append(symb)
        rez2 = str(print(f"Лише букви: {b_list}"))
        rez = rez1 + rez2
    else:
        rez = 'Вам пора відпочити!'
    return    
magic(cust_s)

