n=int(input("Введіть кількість рядків N="))
if n>0:
    print("Введіть 1 рядок: ")
    conc_s=input()
    i=2
    while i<=n:
        print("Введіть ",i," рядок: ")
        s=input()
        conc_s=conc_s+s
        i=i+1
    print(conc_s)
else:
    print("Ви ввели некоректну кількість рядків")
