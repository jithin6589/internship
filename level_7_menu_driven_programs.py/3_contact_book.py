def contact_book():

    contacts = {}

    while True:

        print("\n1. Add")
        print("2. Search")
        print("3. Delete")
        print("4. List All")
        print("5. Exit")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:

                name = input("Enter name: ")
                phone = input("Enter phone number: ")

                contacts[name] = phone

                print("Contact added successfully.")

            elif choice == 2:

                name = input("Enter name to search: ")

                if name in contacts:
                    print("Phone:", contacts[name])
                else:
                    print("Contact not found.")

            elif choice == 3:

                name = input("Enter name to delete: ")

                if name in contacts:
                    del contacts[name]
                    print("Contact deleted successfully.")
                else:
                    print("Contact not found.")

            elif choice == 4:

                if len(contacts) == 0:
                    print("No contacts available.")
                else:

                    print("\nAll Contacts:")

                    for name in contacts:
                        print(name, ":", contacts[name])

            elif choice == 5:

                print("Contact book exited.")
                break

            else:

                print("Invalid choice. Please enter 1 to 5.")

        except ValueError:

            print("Invalid input. Please enter a number.")


def main():

    contact_book()


main()