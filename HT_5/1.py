#створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
#Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).

class LoginException(Exception):
    pass
def check_login(login, parol, silent=False):
    baza = [('Kravec','1234'), ('Popov','567'), ('Tkach', '999'), ('Filshyn','888'), ('Holder','111')]
    logins = [user[0] for user in baza]
    passwords = [user[1] for user in baza]
    if login in logins:
        index = logins.index(login)
        if parol == passwords[index]:
            return True
        else:
            if silent == False:
                raise LoginException("Неправильний пароль!")
            else:
                return False
    else:
        raise LoginException("Даний логін не знайдено!")
cust_login = input("Введіть логін: ")
cust_parol = input("Введіть пароль: ")
print(check_login(cust_login, cust_parol, True))
print(check_login(cust_login, cust_parol))
