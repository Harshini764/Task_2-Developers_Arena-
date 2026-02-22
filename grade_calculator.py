name = input("Enter student name: ")
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("  ⚠️  Marks must be between 0 and 100. Try again.")
    except ValueError:
        print("  ⚠️  Invalid input. Please enter a number.")

if marks >= 90:
    grade = "A"
    message = "Excellent! Outstanding performance! 🌟"
elif marks >= 80:
    grade = "B"
    message = "Very Good! Keep it up! 👍"
elif marks >= 70:
    grade = "C"
    message = "Good! Room for improvement. 😊"
elif marks >= 60:
    grade = "D"
    message = "Satisfactory. Study harder! 📚"
else:
    grade = "F"
    message = "Failed. Don't give up! 💪"

print()
print(f"📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
