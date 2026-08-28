import numpy as np

temps = np.array([28, 30, 29, 31, 33, 32, 30, 29, 27, 26, 28, 31, 34, 33])

first_week = temps[:7]
print("First week temperatures:", first_week)

second_week = temps[7:]
print("Second week temperatures:", second_week)


alternate_days = temps[::2]
print("Every alternate day temperatures:", alternate_days)


fahrenheit = (temps * 9 / 5) + 32
print("Fahrenheit temperatures:", fahrenheit)


highest = np.max(temps)
lowest = np.min(temps)
average = np.mean(temps)

print("Highest temperature:", highest, "°C")
print("Lowest temperature:", lowest, "°C")
print("Average temperature:", average, "°C")

# 5. Count days above the average