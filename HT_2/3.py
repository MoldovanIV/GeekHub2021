mylist=[(),(),('',),('a', 'b'),{},('a','b','c'),('d'),'',[]]
print(mylist)
i=0
while i < len(mylist):
    if mylist[i]==() or mylist[i]=='' or mylist[i]==[] or mylist[i]=={}:
        del mylist[i]
    else:
        i+=1
print(mylist)
