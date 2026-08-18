def avg(numbers):

    total = sum(numbers)

    average = total / len(numbers)

    return average


def main():

    numbers = input("Enter numbers separated by space: ")

    numbers = numbers.split()

    numbers = list(map(int, numbers))

    result = avg(numbers)

    print("Average:", result)


main()