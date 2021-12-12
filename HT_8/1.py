#Програма-банкомат
import json
import csv

VISITOR = ''

def login_password():
    global VISITOR
    attempt = 3
    while attempt:
        print(f'Ви маєте {attempt} спроби\n')
        login, password = map(str, input('Введіть логін та пароль (використовуючи пробіл): ').split())
        with open('users.csv') as f:
            reader = csv.reader(f)
            reader = next(reader)
            for row in reader:
                if login == row[0] and password == row[1]:
                    visitor = login
                    return True
        attempt -= 1
        return '3 спроби використано'
#працює
def menu():
    print('Вітаємо!\n')
    print('Переглянути баланс, натисніть 1\n')
    print('Поповнити баланс, ннатисніть 2\n')
    print('Зняти готівку, натисніть 3\n')
    print('Для виходу, натисніть 4\n')
    user_action = int(input())
    return user_action

#не працює файл
def view_balance():
    with open(VISITOR+'_balance.csv') as balance:
        print(f'Ваш баланс: {balance.read()}')
    print('--------------')

#не працює файл, та сама помилка з visitor
def ad_balance():
    add_balance = int(input('Введіть суму поповнення: '))
    if add_balance < 0:
      return 'Помилка! Введено від\'ємну суму!'
    with open(VISITOR+'_balance.csv') as balance:
        b = balance.read()
    with open(VISITOR+'_balance.csv', 'w') as balance:
        balance.write(str(add_balance + int(b)))
    with open(VISITOR+'_balance.csv') as balance, open(VISITOR+'_transactions.csv', 'a') as transactions:
        b = balance.read()
        transactions.write(json.dumps(b))
        transactions.write('\n')
    print('--------------')

#не працює файл, та сама помилка з visitor
def subt_balance():
    subtract_balance = int(input('\nВведіть суму, яку бажаєте зняти: '))
    with open(f'{VISITOR}_balance.csv') as balance:
        b = balance.read()
    if subtract_balance < 0:
      return 'Введено від\'ємну суму'
    if int(b) >= subtract_balance:
        with open(VISITOR+'_balance.csv', 'w') as balance:
            balance.write(str(int(b) - subtract_balance))
        with open(VISITOR+'_balance.csv') as balance, open(VISITOR+'_transactions.csv', 'a') as transactions:
            b = balance.read()
            transactions.write(json.dumps(b))
            transactions.write('\n')
        print('Операція успішна!')
    else:
        print('Недостатньо коштів...')
    print('--------------')

#працює
def start():
    if login_password():
        while True:
            result = menu()
            if result == 1:
                view_balance()
            if result == 2:
                ad_balance()
            if result == 3:
                subt_balance()
            if result == 4:
                return 'До побачення!'
    return 'До побачення!'

start()
