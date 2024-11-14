# ✅ Grade Calculator:
# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

score = float(input("enter ur score\n"))

if score >= 90 and score <= 100:
    print("score is", "A")
elif score >= 80 and score <= 89:
    print("score is", "B")
elif 70 <= score <= 79:
    print("score is", "C")
elif 60 <= score <= 69:
    print("score is", "D")
else:
    print("score is", "F")