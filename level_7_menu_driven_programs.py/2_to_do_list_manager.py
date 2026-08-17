def todo_manager():

    elements = []

    while True:

        print("\n1. Add")
        print("2. Remove")
        print("3. View")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:

                element = input("Enter the element to add : ")

                elements.append(element)

                print("element added successfully.")

            elif choice == 2:

                for index in range(len(elements)):
                    print(index, ":", elements[index])

                index = int(input("Enter the index number to remove: "))

                if index >= 0:
                    removed_element = elements.pop(index)
                    print("Element removed successfully:", removed_element)
                else:
                    print("Invalid index.")
            elif choice == 3:

                if len(element) == 0:
                    print("No element available.")
                else:
                    print("\nYour elementes are:")

                    for element in elements:
                        print("-", element)

            elif choice == 4:

                print("To-do list exited.")
                break

            else:
                print("Invalid choice. Please enter 1 to 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():

    todo_manager()


main()