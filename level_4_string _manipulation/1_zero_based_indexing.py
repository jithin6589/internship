def even_index(text):
    for i in range(len(text)):
        if i % 2 == 0:
            print(f"index {i}: {text[i]}")
def main():
    text=input("Enter a string: ")
    result=even_index(text)
main()