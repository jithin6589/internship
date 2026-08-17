def calculator():

    while True:

        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            number1 = float(input("Enter first number: "))
            number2 = float(input("Enter second number: "))
            if choice == 5:
                print("Calculator exited.")
                break

            elif choice == 1:

                print("Result:", number1 + number2)

            elif choice == 2:

                print("Result:", number1 - number2)

            elif choice == 3:

                print("Result:", number1 * number2)

            elif choice == 4:

                if number2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Result:", number1 / number2)

            else:
                print("Invalid choice. Please enter 1 to 5.")

        except ValueError:
            print("Invalid input. Please enter a valid number ")


def main():

    calculator()


main()