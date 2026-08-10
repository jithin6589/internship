def str_reversal(string):
    for i in range(len(string)):
            print(f"index {i}: {string[i]}")
    result=string[::-1]
    print()
    for j in range(len(result)):
            print(f"index {j}: {result[j]}")
    return result
def main():
    string=input("enter the sring to reverse:")
    result=str_reversal(string)
    print()
    print("before reversal the string is:",string)
    print(f"Reversed string: {result}")
main()