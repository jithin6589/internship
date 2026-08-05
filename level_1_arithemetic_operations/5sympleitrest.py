# P = float(input("Enter the principal amount: "))
# R = float(input("Enter the rate of interest: "))
# T = float(input("Enter the time (in years): "))
# result=(P*R*T)/100
# print("The simple interest is:", result)

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (%): "))
    time = float(input("Enter the time (in years): "))

    simple_interest = simple_interest(principal, rate, time)

    print("\n----- Simple Interest Calculator -----")
    print(f"Principal Amount : {principal}")
    print(f"Rate of Interest : {rate}%")
    print(f"Time             : {time} years")
    print(f"Simple Interest  : {simple_interest}")


main()