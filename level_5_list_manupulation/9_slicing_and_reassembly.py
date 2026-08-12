def rotate_left(numbers, n):

    result = numbers[n:] + numbers[:n]

    return result


def main():

    numbers = [1, 2, 3, 4, 5]
    n = 2

    result = rotate_left(numbers, n)

    print("Rotated list:", result)


main()