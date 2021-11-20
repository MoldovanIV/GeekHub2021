d = {0: -100, 1: 10, 2: 30, 3: 50, 4: 70, 5: 90}
print("Словник:\n",d)
key_max = max(d.keys(), key=(lambda k: d[k]))
key_min = min(d.keys(), key=(lambda k: d[k]))
print('Max: ',d[key_max])
print('Min: ',d[key_min])
