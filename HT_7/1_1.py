import json
base = {"Ivanov" : "123", "Bobov" : "808bo", "Hrek" : "yyy111"}
#Створення текстового файла з даними користувачів (логін/пароль)
try:
    with open("users.txt","w") as file:
        for login,parol in base.items():
            file.write("{}:{}".format(login,parol))
except FileNotFoundError:
    print("Неможливо відкрити файл")
finally:
    print(file.closed) 

#   def balance
def balance(user_login):
    b = open (user_login+".txt","r")
    rb = b.readline())
    print(rb)
    b.close()
#   def transactions
def transactions(user_login,suma):
    filename = user_login+".json"
    with open(filename,"w") as t:
        json.dump(suma,t)

    filename = user_login+".json"
    with open(filename) as t:
        suma = json.load(t)
    print(suma)   
print("Доброго дня!")
user_login = input("Введіть Ваш логін: ")
user_parol = input("Введіть Ваш пароль: ")

if user_login in base.keys() and user_parol == base[user_login]:
    operation = int(input("Яку дію бажаєте виконати?\n-------------------------------\nПереглянути баланс - Натисніть 1\nПоповнити баланс - Натисніть 2\nЗняти готівку - Натисніть 3\nВихід - Натисніть 4\n"))
    name = user_login
    if operation == 1:
        print("Ваш баланс становить: ")
        balance(user_login)
    elif operation == 2:
        suma = float(input("Введіть суму поповнення: "))
        transactions(user_login,suma)
        balance(user_login)
    elif operation == 3:
        suma = float(input("Введіть суму, яку бажаєте зняти: "))
        transactions(user_login,-suma)
    else:
        print ("Вже йдете? Так швидко? :( Приходьте ще!\nГарного Вам дня!")
else:
    print("Упс... Дані введено не вірно. Спробуйте ще.")


