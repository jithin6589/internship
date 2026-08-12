def manage_fruits():
    print("\n")
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    print("the orjinal list is : ",(fruits))
    fruits.append("fig")
    print("\n")
    print("after adding new fruite",(fruits))
    fruits.pop(1)
    print("\n")
    print("after removing the first frutit",(fruits))


def main():

    manage_fruits()
    

main()