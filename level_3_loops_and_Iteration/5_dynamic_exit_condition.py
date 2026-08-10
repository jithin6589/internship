def count_steps(number):

    steps = 0

    while number != 1:

        if number % 2 == 0:
            number = number // 2
            print(steps)
        else:
            number = number * 3 + 1
            print(steps)
        steps = steps + 1
    print(steps)
    return steps
    
def main():

    number = int(input("Enter a the number: "))

    result = count_steps(number)

    print(f"{result} steps")


main()