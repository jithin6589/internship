def calculate_factorial(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial

def main():
    number = int(input("Enter a number: "))
    result = calculate_factorial(number)
    print(f"The factorial of {number} is {result}")


main()