# Truth ness and short circuiting meaning is the python have an ability to find the true of fale condition we dont hav eto print true==true
# eg:
# name = "Jithin"

# if name:
#     print("Name exists") 
# the out put is true so print the name other wise

#  we have an empty list it will print false or no output 
# eg:
# name = ""

# if name:
#     print("Name exists")
#  the output is false so no output 

def check_password(password):

    failed = []

    if len(password) < 8:
        failed.append("length")

    has_digit = False
    has_upper = False

    for ch in password:
        if ch.isdigit():
            has_digit = True

        if ch.isupper():
            has_upper = True

    if has_digit== False:
        failed.append("digit")

    if has_upper== False:
        failed.append("uppercase")

    if len(failed) == 0:
        print("Password is valid")
    else:
        print(f"the failds are: {failed}")
def main():

    password = input("Enter password: ")

    check_password(password)


main()