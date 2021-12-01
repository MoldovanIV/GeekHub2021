#Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
#   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
#   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
#  - щось своє :)
#   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.
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
    else:
        raise LoginException("Проблема авторизації!")
print(validate('Newlogin','MYpassword2021'))


