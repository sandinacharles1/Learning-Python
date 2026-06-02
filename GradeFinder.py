#FIX INDENTATION

# Variables. We have the dictionary to know which percentage to multipl by, and we have
the lists to later add all the numbers to to perform operational functions with it.
list_percentages = {"Homework": 0.4, "Labs": 0.1, "Quizzes": 0.1, "Exams": 0.4}
lab_grades_list = []
homework_grades_list = []
quiz_grades_list = []
exam_grades_list = []
# Function to get lab grades. We don’t know how many they have so we have it loop until
they say they don’t have anymore. This applied to all getting functions below.
def get_lab_grades():
lab_grades_input = input("Input Lab grades, if there are no more grades, type 'No
More Grades': ")
while lab_grades_input != "No More Grades":
lab_grades_list.append(float(lab_grades_input))
lab_grades_input = input("Input Lab grades (or 'No More Grades'): ")
# Function to get homework grades
def get_homework_grades():
homework_grades_input = input("Input Homework grades, if there are no more grades,
type 'No More Grades': ")
while homework_grades_input != "No More Grades":
homework_grades_list.append(float(homework_grades_input))
homework_grades_input = input("Input Homework grades (or 'No More Grades'): ")
# Function to get quiz grades
def get_quiz_grades():
quiz_grades_input = input("Input Quiz grades, if there are no more grades, type 'No
More Grades': ")
while quiz_grades_input != "No More Grades":
quiz_grades_list.append(float(quiz_grades_input))
quiz_grades_input = input("Input Quiz grades (or 'No More Grades'): ")
# Function to get exam grades
def get_exam_grades():
exam_grades_input = input("Input Exam grades, if there are no more grades, type 'No
More Grades': ")
while exam_grades_input != "No More Grades":
exam_grades_list.append(float(exam_grades_input))
exam_grades_input = input("Input Exam grades (or 'No More Grades'): ")
# Average Grade. We will be averaging a lot, might as well make it it’s own functions.
If ther are no grades then nothing because the denominator would be 0, which is an error.
def average(grades):
return sum(grades) / len(grades) if grades else 0
# Letter Grade. We need to equate a number to a letter grade based on the standard
grading system.
def letter_grade(score):
if score >= 90:
return "A"
elif score >= 87:
return "B+"
elif score >= 80:
return "B"
elif score >= 77:
return "C+"
elif score >= 70:
return "C"
elif score >= 60:
return "D"
else:
return "F"
# Get grades from user using the functions we created above, and have it append
everything into the list. we get these grades to then perform operations with them.
get_homework_grades()
get_lab_grades()
get_quiz_grades()
get_exam_grades()
# Calculate averages using the grades we got in the list.
average_homework = average(homework_grades_list)
average_lab = average(lab_grades_list)
average_quiz = average(quiz_grades_list)
average_exam = average(exam_grades_list)
# Compute final weighted grade. We will use dictionary value since it is assigned, which
is shown in the prompt
final = (average_homework * list_percentages["Homework"] +
average_lab * list_percentages["Labs"] +
average_quiz * list_percentages["Quizzes"] +
average_exam * list_percentages["Exams"])
# Print report
print("\nGRADE REPORT")
print("-" * 75)
print(f"Homework grades\t: {homework_grades_list} = {sum(homework_grades_list)} /
{len(homework_grades_list)} = {average_homework:.1f}")
print(f"Lab grades\t: {lab_grades_list} = {sum(lab_grades_list)} / {len(lab_grades_list)}
= {average_lab:.1f}")
print(f"Quiz grades\t: {quiz_grades_list} = {sum(quiz_grades_list)} /
{len(quiz_grades_list)} = {average_quiz:.1f}")
print(f"Exam grades\t: {exam_grades_list} = {sum(exam_grades_list)} /
{len(exam_grades_list)} = {average_exam:.1f}")
print("-" * 75)
print(f"Homeworks\t: {average_homework:.1f} × {list_percentages['Homework']} =
{average_homework * list_percentages['Homework']:.1f}")
print(f"Labs\t: {average_lab:.1f} × {list_percentages['Labs']} = {average_lab *
list_percentages['Labs']:.1f}")
print(f"Quizzes\t: {average_quiz:.1f} × {list_percentages['Quizzes']} = {average_quiz *
list_percentages['Quizzes']:.1f}")
print(f"Exams\t: {average_exam:.1f} × {list_percentages['Exams']} = {average_exam *
list_percentages['Exams']:.1f}")
print("-" * 30)
print(f"TOTAL\t: {final:.1f}")
print("-" * 30)
print(f"GRADE\t: {letter_grade(final)}")
print("-" * 30)
