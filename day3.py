pin = int(input("Please enter your pin: "))
ammount = 26000

if pin == 1545:
    mode = input("Enter your banking mode: ")
    if mode == "deposite":
        am = int(input("Enter the amount to deposite: "))
        print("Your amount has been debited successfully!!")
        ammount = ammount + am
        print("Your new amount is: ", ammount)
    elif mode == "withdraw":
        am = int(input("Enter the amount to withdraw: "))
        if am <= ammount:
            print("Your amount has been credited successfully!!")
            ammount = ammount - am
            print("Your new amount is: ", ammount)
        else:
            print("You can't withdraw more than your bank balance")
    else:
        print("Invalid mode")
else:
    print("Incorrect pin")
