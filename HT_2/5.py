d={6:10,'Age':20,1:10,'Name': 'Ivan', 'Number':20}
print("Початковий словник\n",d)
result={}
for key, value in d.items():
    if value not in result.values():
        result[key]=value
print("Після видалення дублікатів:\n",result)


