pin = int(input("Enter your pin: "))

while pin !=1234:
    pin = int(input("Wrong pin! try again: "))
if pin == 1234:
    print("Accepted!")