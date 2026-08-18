def append_file():

    file = open("notes.txt", "a")

    text = input("Enter the content to store: ")

    file.write(text + "\n")

    file.close()

    print("Content added successfully.")


def read_file():

    file = open("notes.txt", "r")

    content = file.read()

    print("\nFile contents:")
    print(content)

    file.close()


def overwrite_file():

    file = open("notes.txt", "w")

    text = input("Enter the new content to remove and over write the file: ")

    file.write(text + "\n")

    file.close()

    print("File overwritten successfully.")


def main():

    while True:

        print("\n1. Append")
        print("2. Read")
        print("3. Overwrite")
        print("4. Exit")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:
                append_file()

            elif choice == 2:
                read_file()

            elif choice == 3:
                overwrite_file()

            elif choice == 4:
                print("Program exited.")
                break

            else:
                print("Invalid choice. Please enter 1 to 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


main()