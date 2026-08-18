def greet(name, greeting="Hello"):

    return greeting + ", " + name


def main():

    result1 = greet("Sam")

    print(result1)

    result2 = greet("Sam", greeting="Hi")

    print(result2)


main()