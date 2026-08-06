# multi tire branching mans to study multiple portions multiple decesions
# like , if elif else
def tax_calculator(income):
    if income<=10000:
        return 0
    elif income<=20000:
        return (income-10000)*10/100
    else:
        return 1000+(income-20000)*20/100
def main():
    income=int(input("enter the incume to calculate thetax:"))
    tax=tax_calculator(income)
    print(f"the tax of {income} is{tax}")
main()