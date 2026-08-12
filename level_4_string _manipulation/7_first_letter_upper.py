example="hello welcome to python"
example=example.split()
result=""
for word in example:
    temp=word[0].upper() + word[1:]
    print(temp)
    result += temp + " "
print(result)