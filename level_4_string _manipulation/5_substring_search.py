def count_substring(sentence, word):

    count = sentence.count(word)

    return count


def main():

    sentence = input("Enter a sentence: ")
    word = input("Enter the word to search: ")

    result = count_substring(sentence, word)

    print("The word appears", result, "times")


main()