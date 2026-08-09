def print_pattern( num1, num2):

    for i in range(num1, num2+1):

        for j in range(i):
            print(i, end=" ")

        print()


def main():
    num1=int(input("Enter the starting number: "))
    num2=int(input("Enter the ending number: "))
    print_pattern(num1, num2)


main()