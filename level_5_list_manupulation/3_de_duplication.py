def remove_duplicates(numbers):

    unique_numbers = []

    for number in numbers:

        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


def main():

    numbers = input("Enter numbers separated by spaces: ")

    numbers = numbers.split()
    print(numbers)
    result = remove_duplicates(numbers)

    print("Unique elements:", result)


main()