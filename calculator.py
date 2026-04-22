def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\n1.Add  2.Subtract  3.Multiply  4.Divide")
        choice = input("Enter choice: ")

        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Cannot divide by zero")
        else:
            print("Invalid choice")

        again = input("Do you want to continue? (yes/no): ")
        if again.lower() != 'yes':
            print("Program Stopped!!!")
            break


calculator()