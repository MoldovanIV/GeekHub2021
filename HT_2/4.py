dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
print(dic1)
print(dic2)
print(dic3)
allinOne = dict(list(dic1.items()) + list(dic2.items())+ list(dic3.items()))
print("Об'єднуємо словники в один:\n",allinOne)
print("Перевірка початкових словників:")
print(dic1)
print(dic2)
print(dic3)
