element=input('Введіть новий елемент x=')
old=[(10, 20, 40), (40, 50, 60,70), (80, 90),(1000,)]
new=[]
for i in range(len(old)):
    prom=list(old[i])
    prom[-1]=element
    prom=tuple(prom)
    new.append(prom)
print('Старий список:\n',old)
print('Новий список:\n',new)
