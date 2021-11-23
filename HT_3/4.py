#Створiть 3 рiзних функцiї (на ваш вибiр).
#Кожна з цих функцiй повинна повертати якийсь результат.
#Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi,
#обробляє повернутий ними результат та також повертає результат.
#Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3

def summa(a,b):
    s=a*a+2*b
    return s
def rizn(a,b):
    r=a-b
    return r
def dob(a,b):
    d=a*b
    return d
def vyraz(a,b):
    v=summa(a,b)+rizn(a,b)+dob(a,b)
    return v
print("Обчислення значення виразу \n (x^2+2x)+(x-y)+xy ")
x=float(input("Введіть значення x = "))
y=float(input("Введіть значення y = "))
#print(f"Сума = {summa(x,y)}")
#print(f"Різниця = {rizn(x,y)}")
#print(f"Добуток = {dob(x,y)}")
print(f"Значення виразу = {vyraz(x,y)}")
