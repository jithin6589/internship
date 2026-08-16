def inventory_system():

    inventory = {}

    while True:

        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Inventory")
        print("4. Exit")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:

                item = input("Enter item name: ")
                quantity = int(input("Enter quantity to add: "))

                if item in inventory:
                    inventory[item] = inventory[item] + quantity
                else:
                    inventory[item] = quantity

                print("Stock added successfully.")

            elif choice == 2:

                item = input("Enter item name: ")
                quantity = int(input("Enter quantity to remove: "))

                if item not in inventory:
                    print("Item not found.")

                elif quantity > inventory[item]:
                    print("Not enough stock.")

                else:
                    inventory[item] = inventory[item] - quantity
                    print("Stock removed successfully.")

            elif choice == 3:

                if len(inventory) == 0:
                    print("Inventory is empty.")

                else:
                    print("\nInventory:")

                    for item in inventory:
                        print(item, ":", inventory[item])

            elif choice == 4:

                print("Inventory system exited.")
                break

            else:

                print("Invalid choice. Please enter 1 to 4.")

        except ValueError:

            print("Invalid input. Please enter a number.")


def main():

    inventory_system()


main()