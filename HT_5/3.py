#На основі попередньої функції створити наступний кусок кода:
#   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
#   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення,

import re
pattern = r'[A-Z]{2}'
class LoginException(Exception):
    pass
def validate(login, password):
    contains_digit = False
    for character in password:
        if character.isdigit():
            contains_digit = True
    has_2capital_letters = re.search(pattern, password)
    if 3 <= len(login) <= 50 and len(password) >= 8 and contains_digit == True and has_2capital_letters is not None:
        return "Вітаємо, Ви авторизовані!"
    elif contains_digit == False:
        raise LoginException("Пароль не відповідає вимогам! Ваш пароль має містити цифри!")
    elif has_2capital_letters is None:
        raise LoginException("Пароль не відповідає вимогам! Ваш пароль має містити хоча б дві великі літери!")
    else:
        raise LoginException("Проблема авторизації!")
    
authorization = {'Kravec':'1234_QWERTY', 'Holder':'111_QWErty',  'Popov':'qwerty567', 'Tkach':'qwerty', 'Filshyn':'123456'}
for auth in authorization.keys():
    try:
        print(f"Логін: {auth}, пароль: {authorization[auth]}")
        print(validate(auth, authorization[auth]))
    except LoginException as exp:
        print(exp)



    
