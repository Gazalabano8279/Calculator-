while True:
    num1 = int(input("Enter the number"))
    num2 = int(input("Enter the number"))

    print("1. Add")
    print("2. Multiply")
    print("3. Subtraction")
    print("4. Division")
    print("5. Find Remainder")
    print("6. Find the powers")
    choice = int(input("Enter your choice"))
    if choice == 1:
        print(num1+num2)
    elif choice == 2:
        print(num1*num2)
    elif choice == 3:
        print(num1-num2)
    elif choice == 4:
        if num2 != 0:
            print(num1/num2)
        else:
            print("Error: Denominator cannot be 0")
    elif choice == 5:
        print(num1%num2)
    elif choice == 6:
        print(num1**num2)
    else:
        print("Invalid Choice")
    again = input("Do you want to continue?")
    if again.lower() != "yes":
        break
