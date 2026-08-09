def countdown(number):

    while number >= 0:
        print(number)
        number = number - 1

    print("Blast off!")


def main():

    number = int(input("Enter a number: "))

    countdown(number)


main()