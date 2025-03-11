def get_scores():
    return [float(input(f"Enter {c} score: ")) for c in ["Assignments", "Quizzes", "Midterm", "Final Exam"]]

def calculate_grade(scores):
    weights = [0.3, 0.2, 0.2, 0.3]
    return sum(s * w for s, w in zip(scores, weights))

def letter_grade(grade):
    return "A" if grade >= 90 else "B" if grade >= 80 else "C" if grade >= 70 else "D" if grade >= 60 else "F"

scores = get_scores()
final_grade = calculate_grade(scores)
print(f"Final Grade: {final_grade:.2f} ({letter_grade(final_grade)})")
