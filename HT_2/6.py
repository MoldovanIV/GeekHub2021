dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
print(dic1)
print(dic2)
print(dic3)
dic1.update(dic2)
dic1.update(dic3)
print("Об'єднуємо словники в один:\n",dic1)
print("Перевірка початкових словників:")
print(dic1)
print(dic2)
print(dic3)


