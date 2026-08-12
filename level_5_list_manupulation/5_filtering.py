def filter_numbers(numbers):

    for number in numbers:

        if number % 5 == 0:
            print(number)


def main():

    numbers = input("Enter numbers: ")

    numbers = [int(number) for number in numbers.split()]

    print(numbers)

    filter_numbers(numbers)


main()