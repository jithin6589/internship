def check_palindrome(text):
    
    if text == text[::-1]:
        print(f"the letter {text} is a palindrome")
    else:
        print(f"the letter {text} is not a palindrome")


def main():

    text = input("Enter a string: ")

    result = check_palindrome(text)


main()