def state_tracking():

    previous = 0

    for now in range(10):

        total = now + previous

        print(f"Current {now} Previous {previous} Sum {total}")

        previous = now


def main():

    state_tracking()


main()