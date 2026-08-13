def count_words(sentence):

    words = sentence.split()

    count = {}

    for word in words:

        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

    return count


def main():

    sentence = input("Enter a sentence: ")

    result = count_words(sentence)

    print(result)


main()