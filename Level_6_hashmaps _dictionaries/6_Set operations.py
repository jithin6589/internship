def find_common(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    common = set1 & set2

    return common


def main():

    list1 = set(map(int, input("Enter numbers: ").split()))
    list2 = set(map(int, input("Enter numbers: ").split()))

    result = find_common(list1, list2)

    print("Common elements:", result)


main()