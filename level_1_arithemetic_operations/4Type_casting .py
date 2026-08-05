# a=input("enter the first no:")
# b=input("enter the second no:5)
# c=int(a)
# d=int(b)
# result1=a+b
# result2=c+d
# print("the first result is:",result1)
# print("the second result is:",result2)

def add_as_string(value1, value2):
    return value1 + value2


def add_as_integer(value1, value2):
    return value1 + value2


def main():
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")

    string_result = add_as_string(first_number, second_number)

    number1 = int(first_number)
    number2 = int(second_number)

    integer_result = add_as_integer(number1, number2)

    print(f"\nString Addition  : {first_number} + {second_number} = {string_result}")
    print(f"Integer Addition : {number1} + {number2} = {integer_result}")


main()