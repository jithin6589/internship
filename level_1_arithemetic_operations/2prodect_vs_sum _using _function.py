# ""num1=int(input("enter the first no"))
# num2=int(input("enter the second no"))
# def product_sum(num1,num2):
#     if num1*num2<=1000:
#         return num1*num2
#     else:
#       return num1+num2
# result=product_sum(num1,num2)
# print("the result is :",result)
def sum_of_two(var1,var2):
    return(var1+var2)
def product_of_two(var1,var2):
    return(var1*var2)

def main():
    var1=int(input("enter the first no :"))
    var2=int(input("enter the second no:"))

    product_result=(product_of_two(var1,var2))
    if product_result<=1000:
        print(f"the product of{var1} * {var2} ={product_result}")
    else:
        sum_result=(sum_of_two(var1,var2))
        print(f"the sum of{var1} + {var2} ={sum_result}")
main()