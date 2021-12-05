#Програма-світлофор
import time
print("Кольори світлофора:\nДля авто   Для пішохода")
while True:
    for i in range(4):
        time.sleep(1)
        print("   Red        Green")
    print("\nУвага! Зміна кольору!\n")
    for i in range(2):
        time.sleep(1)
        print("  Yellow      Green")
    print("\nУвага! Зміна кольору!\n")   
    for i in range(4):
        time.sleep(1)
        print("   Green       Red")
    print("\nУвага! Зміна кольору!\n")
    for i in range(2):
        time.sleep(1)
        print("   Yellow      Red")
    print("\nУвага! Зміна кольору!\n")
