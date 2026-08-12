def find_values(numbers):

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number
            print("Largest:", largest)
        if number < smallest:
            smallest = number
            print("Smallest:", smallest)

def main():

    numbers = [45, 2, 89, 12, 7]

    find_values(numbers)
    


main()