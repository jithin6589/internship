def cross_list_filter(list1, list2):

    result = []

    for number in list1:
        if number % 2 != 0:
            result.append(number)

    for number in list2:
        if number % 2 == 0:
            result.append(number)

    return result


def main():

    list1 = [10, 20, 25, 30, 35]
    list2 = [40, 45, 60, 75, 90]

    result = cross_list_filter(list1, list2)

    print("Result:", result)


main()