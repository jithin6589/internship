# Why is this called Nested Conditional?

# A Nested Conditional means an if statement inside another if statement.

# Instead of checking everything at the same level, we first check one condition. If it is true, we then check another condition inside it.

# Example:

# if side1 == side2:
#     if side2 == side3:
#         print("Equilateral")

def triangle_finder(side1,side2,side3):
    if side1==side2:
        if side2==side3:
            return("Equilateral")
        else:
            return("Isosceles")
    else:
        if side2==side3:
            return("Isosceles")
        else:
            if side1==side3:
                return("Isosceles")
            else:
                return("Scalene")
def main():
    side1=int(input("Enter the side 1: "))
    side2=int(input("Enter the side 2: "))
    side3=int(input("Enter the side 3: "))
    reslt=triangle_finder(side1,side2,side3)
    print(f"The triangle is {reslt}")
main()