def invert_dictionary(data):

    result = {}

    for key in data:

        value = data[key]

        result[value] = key

    return result


def main():

    data = {"a": 1, "b": 2}

    result = invert_dictionary(data)

    print("Inverted dictionary:", result)


main()