#Отримати максимальне і мінімальне значення із словника. Дані захардкодити.
d = {0: -100, 1: 10, 2: 30, 3: 50, 4: 70, 5: 90}
print("Словник:\n",d)
key_max = max(d, key=d.get)
key_min = min(d, key=d.get)
print('Max: ',d[key_max])
print('Min: ',d[key_min])
