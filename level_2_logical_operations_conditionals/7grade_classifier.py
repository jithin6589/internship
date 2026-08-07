def grade_finder(score):

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    else:
        return "F"


def main():

    score = int(input("Enter your score: "))

    grade = grade_finder(score)

    print("Your Grade is:", grade)


main()