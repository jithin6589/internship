def compare_numbers(num1, num2):
    if num1 > num2:
        return "greater"
    elif num1 < num2:
        return "less"
    else:
        return "equal"


def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = compare_numbers(num1, num2)

    if result == "greater":
        print(f"{num1} is greater than {num2}")
    elif result == "less":
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is equal to {num2}")


main()