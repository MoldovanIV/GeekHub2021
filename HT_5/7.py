#Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
def iterate(sequence):
    while True:
        for elem in sequence:
            yield elem

for elem in iterate("ДеМояВідпустка?!.."):
    print(elem)
