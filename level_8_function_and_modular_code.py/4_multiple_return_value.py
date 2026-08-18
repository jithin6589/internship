def calculate(numbers):

    total = sum(numbers)

    average = total / len(numbers)

    return total, average


def main():

    numbers = (input("enter the number seperated by space "))

    numbers=numbers.split()

    numbers=list(map(int,numbers))

    total, average = calculate(numbers)

    print("Sum:", total)
    print("Average:", average)


main()