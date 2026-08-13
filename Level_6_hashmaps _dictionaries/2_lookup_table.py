def create_square_dictionary():

    squares = {}

    for number in range(1, 11):
        squares[number] = number * number

    return squares


def main():

    result = create_square_dictionary()

    print(result)


main()