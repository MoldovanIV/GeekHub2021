#Калькулятор :)
#повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
def calcul(a,oper,b):
    if oper == '+':
        rez=a+b
    elif oper == '-':
        rez=a-b
    elif oper == '*':
        rez=a*b
    elif oper == '/':
        rez=a/b
    else:
        rez=input("Помилка у введенні позначення дії")
    return rez  
x = float(input("Введіть перший аргумент х = "))
znak = input("Введіть позначення дії ( +, -, *, / ) = ")
y = float(input("Введіть другий аргумент y = "))
if (y == 0):
    print("Ділити на 0 не можна!")
else:    
    print(f"{x} {znak} {y} = {calcul(x,znak,y)}")
