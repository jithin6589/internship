file = open("notes.txt", "r")

text = file.read()

words = text.split()

count = len(words)

print("Total number of words:", count)

file.close()