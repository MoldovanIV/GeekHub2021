import json

base = {"Ivanov" : "12345", "Bobov" : "808bo", "Hrek" : "yyy111"}

#Створення текстового файла з даними користувачів (логін/пароль)

try:
    with open("users.txt","w") as file:
        for login,parol in base.items():
            file.write("{}:{}".format(login,parol))
except FileNotFoundError:
    print("Неможливо відкрити файл")
finally:
    print(file.closed)

#Фукнція start()
    
def start(user_login,user_parol,base):
    if user_login in base.keys() and user_parol == base[user_login]:
        operation = int(input("Яку дію бажаєте виконати?\n-------------------------------\nПереглянути баланс - Натисніть 1\nПоповнити баланс - Натисніть 2\nЗняти готівку - Натисніть 3\nВихід - Натисніть 4\n"))
        if operation == 1:
            print("Ваш баланс становить: ")
        elif operation == 2:
            print("Введіть суму поповнення: ")
        elif operation == 3:
            print("Введіть суму, яку бажаєте зняти: ")
        else:
            print ("Вже йдете? Так швидко? :( Приходьте ще!\nГарного Вам дня!")
    else:
        print("Упс... Дані введено не вірно. Спробуйте ще.")

#   def balance
#def balance(user_login):
    
#   def transactions
def transactions(user_login):
    tran = []
    base_tran = "tran.json"
    with open(base_tran,"w") as tr:
        json.dump(tran,tr)

print("Доброго дня!")

us_l = input("Введіть Ваш логін: ")
us_p = input("Введіть Ваш пароль: ")

start(us_l,us_p,base)
transactions(us_l)
