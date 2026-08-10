def voels_count(string):
    voels = "aeiouAEIOU"
    count=0
    for i in range (len(string)):
        print(string[i])
        if string[i] in voels:
            count=count+1
    return count
def main():
    string=input("Enter a string: ")
    result=voels_count(string)
    print(f"The number of vowels in the string is: {result}")
main()