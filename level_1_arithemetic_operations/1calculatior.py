
def sum_of_two(var1, var2):
    return var1+var2;

def mul_of_two(var1, var2):
    return var1*var2;

def div_of_two(var1, var2):
    return var1/var2;

def floor_of_two(var1, var2):
    return var1//var2;

def modulus_of_two(var1, var2):
    return var1%var2;


def main():
    var1=int(input("Enter first number:"));
    var2=int(input("Enter second number:"));

    print(f"Sum of {var1} + {var2} = {sum_of_two(var1, var2)}")
    print(f"MUl of {var1} * {var2} = {mul_of_two(var1, var2)}")
    print(f"Div of {var1} / {var2} = {div_of_two(var1, var2)}")
    print(f"Floor of {var1} // {var2} = {floor_of_two(var1, var2)}")
    print(f"Modulus of {var1} % {var2} = {modulus_of_two(var1, var2)}")


main()