def string_remover(string,num):
    result=string[num:]
    return result
def main():
    string=input("Enter a string: ")
    num=int(input("Enter the index of the character to remove: "))
    result=string_remover(string,num)
    print("befores slicing the string is:",string)
    print(f"String after removing character at index {num}: {result}")
main()