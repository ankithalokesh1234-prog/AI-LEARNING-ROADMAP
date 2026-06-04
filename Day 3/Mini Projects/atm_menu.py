balance = 5000

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid Choice")
