#Написати функцію < bank >, яка працює за наступною логікою:
#користувач робить вклад у розмірі < a > одиниць строком на < years > років
#під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
#ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки).
#Параметр < percents > є необов'язковим і має значення по замовчуванню < 10 > (10%).
#Функція повинна принтануть і вернуть суму, яка буде на рахунку.
import math
def bank(a,years):
    cash = a*pow(1.1,years)
    return cash
first_cash = float(input("Введіть величину початкового вкладу:\n"))
cust_years = float(input("Введіть термін вкладу (роки/натуральне число):\n"))
print(f"Зробивши вклад {first_cash} під 10% річних через {cust_years} роки/років\nсума на рахунку = {bank(first_cash,cust_years)}")