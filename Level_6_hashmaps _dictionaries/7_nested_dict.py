def print_report(students, student_name):

    subjects = students[student_name]

    print("\nReport Card")
    print("Student:", student_name)

    for subject in subjects:
        print(subject, ":", subjects[subject])


def main():

    students = {
        "Alice": {
            "Math": 90,
            "Science": 85
        },
        "Bob": {
            "Math": 80,
            "Science": 90
        }
    }

    print("Available Students:")

    for name in students:
        print(name)

    student_name = input("Enter student name: ")

    print_report(students, student_name)


main()