def sanitize_string(sentence, what, use):

    result = sentence.replace(what, use)

    return result


def main():

    sentence = input("Enter a sentence: ")
    what = input("Enter the substring to replace: ")
    use = input("Enter the substring to replace with: ")

    result = sanitize_string(sentence,what,use)

    print("Sanitized string:", result)


main()