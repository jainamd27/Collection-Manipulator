while True:
    print("Welcome to the Bill Splitter App!")
    t_billAm = float(input("Enter total bill amount: "))
    n_ofPeople = int(input("Enter the number of people: "))
    tip_per = int(input("Enter tip percentage (0/5/10/15/20): "))
    tipAm = (t_billAm*tip_per)/100
    print("Tip Amount: ", tipAm)
    t_BillWithTip = t_billAm + tipAm
    print("Total Bill (with Tip): ", t_BillWithTip)
    splitAm = t_BillWithTip / n_ofPeople
    print("Each person should pay: ", splitAm)

    res = input("Would you like to calculate another bill? (y/n): ")
    if res == "y":
        continue
    elif res == "n":
        break
    else:
        print("Invalid input!!")
        break