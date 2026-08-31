import pandas as pd

# 1. Read the CSV file
df = pd.read_csv(r"C:\Users\ASUS\Desktop\JITHIN\internship\pandas_problems\students.csv")

print("Original DataFrame:")
print(df)


# 2. Add grade column based on marks
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "D"


df["grade"] = df["marks"].apply(calculate_grade)

print("\nDataFrame with Grade:")
print(df)


# 3. Filter students who live in Delhi
#    AND have marks greater than 75

filtered_students = df[
    (df["city"] == "Delhi") & 
    (df["marks"] > 75)
]

print("\nStudents from Delhi with marks greater than 75:")
print(filtered_students)


# 4. Statistical summary of marks
print("\nStatistical Summary of Marks:")
print(df["marks"].describe())


# 5. Count students in each grade
print("\nCount of Students in Each Grade:")
print(df["grade"].value_counts())