while True:
    print("Welcome to the Pattern Generator and Number Analyser!")
    print("Select an Option: ")
    print("1. Right-angled Triangle")
    print("2. Pyramid")
    print("3. Left-angled Triangle")
    print("4. Analyze a Range of Numbers")
    print('Please enter q to exit the program')
    choice = input("Enter your choice: ")
    if choice == "1":
        for i in range(1, 6):
            for j in range(1, i+1):
                print("*", end=" ")
            print("")
    elif choice == "2":
        for i in range(1, 5 + 1):
            print(" " * (5 - i), end=" ")
            print("* " * (2 * i - 1))
    elif choice == "3":
        for i in range(1, 5 + 1):
            print(" " * (5 - i), end=" ")
            print("* " * i)
    elif choice == "4":
        s_range = int(input("Enter your starting range: "))
        e_range = int(input("Enter your ending range: "))
        for i in range(s_range, e_range+1):
            total = 0
            if ((i % 2) != 0):
                print(f"Number {i} is Odd")
            elif ((i % 2) == 0):
                print(f"Number {i} is Even")

        total = (s_range + e_range)/2
        print(int(total))
    elif choice == "q":
        print("Program Dismissed!")
        break
    else:
        print("Invalid input!!")
        break
