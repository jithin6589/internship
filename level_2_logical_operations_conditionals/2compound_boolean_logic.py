# what is Compound Boolean Expression
# (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# This single expression checks all the Leap Year rules.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
def main():
    year = int(input("Enter a year: "))

    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
main()