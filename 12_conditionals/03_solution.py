# 3. Grade Calculator

# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter your score : "))

if score > 100:
    print("Please varify your grade again 🥺")
    exit()

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "A"
elif score >= 60:
    grade = "A"
else:
    grade = "A"

print("grade :",grade)