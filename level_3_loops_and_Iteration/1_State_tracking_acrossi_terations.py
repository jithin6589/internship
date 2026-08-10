def state_tracking(number):

    previous = 0

    for i in range(number):

        total = i + previous

        print(f"Current {i} Previous {previous} Sum {total}")

        previous = i


def main():
    number = int(input("Enter a number: "))
    state_tracking(number)
    


# def state_tracking(number):

#     previous = 0

#     for now in range(number):

#         total = now + previous

#         print(f"Current {now} Previous {previous} Sum {total}")

#         previous = now


# def main():

#     number = int(input("Enter a number: "))

#     state_tracking(number)


# main()