def separate_numbers(numbers):

    even_numbers = []
    odd_numbers = []

    for number in numbers:

        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    print("Even:", even_numbers)
    print("Odd:", odd_numbers)


def main():

    numbers = [12, 7, 34, 21, 5, 10, 8, 3, 19, 2]

    separate_numbers(numbers)


main()