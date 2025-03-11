def get_student_info():
    """Get student name and ID"""
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    return name, student_id

def get_scores():
    """Get scores for different grade components"""
    assignments = float(input("Enter assignment score (out of 100): "))
    quizzes = float(input("Enter quiz score (out of 100): "))
    midterm = float(input("Enter midterm exam score (out of 100): "))
    final_exam = float(input("Enter final exam score (out of 100): "))
    return assignments, quizzes, midterm, final_exam

def calculate_final_grade(assignments, quizzes, midterm, final_exam):
    """Calculate the weighted final grade"""
    final_grade = (assignments * 0.3) + (quizzes * 0.2) + (midterm * 0.2) + (final_exam * 0.3)
    return final_grade

def determine_letter_grade(final_grade):
    """Determine letter grade based on final score"""
    if final_grade >= 90:
        return "A"
    elif final_grade >= 80:
        return "B"
    elif final_grade >= 70:
        return "C"
    elif final_grade >= 60:
        return "D"
    else:
        return "F"

def main():
    """Main function to execute the grade calculator"""
    name, student_id = get_student_info()
    assignments, quizzes, midterm, final_exam = get_scores()
    
    final_grade = calculate_final_grade(assignments, quizzes, midterm, final_exam)
    letter_grade = determine_letter_grade(final_grade)
    
    print(f"\nStudent: {name} (ID: {student_id})")
    print(f"Final Grade: {final_grade:.2f}")
    print(f"Letter Grade: {letter_grade}")

if _name_ == "_main_":
    main()
