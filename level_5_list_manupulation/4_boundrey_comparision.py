def check_boundary(numbers):

    if numbers[0] == numbers[-1]:
        print(f"the starting and ending element of the list {numbers} is same ")
    else:
         print(f"the starting and ending element of the list {numbers} is not same ")


def main():

    numbers =input("enter the number for the list , after enter each number add a space:")
    numbers=numbers.split()
    check_boundary(numbers)

    numbers = input("Enter numbers separated by spaces: ")

    numbers = numbers.split()
main()