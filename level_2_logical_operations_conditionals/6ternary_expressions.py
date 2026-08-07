def even_odd(number):

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")


def main():

    number = int(input("Enter a number: "))

    result = even_odd(number)

    print(result)


main()