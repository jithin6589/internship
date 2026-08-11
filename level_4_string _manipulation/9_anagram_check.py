def check_anagram(word1, word2):

    word1 = word1.lower()
    word2 = word2.lower()

    if sorted(word1) == sorted(word2):
        return True
    else:
        return False


def main():

    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")

    result = check_anagram(word1, word2)

    print("Anagram:", result)


main()