from LetterGrade import LetterGrade

user_interested = True
while(user_interested):
    letter_grade = LetterGrade(input("Enter a letter grade: "))
    print(letter_grade.to_points())
    user_interested = False if input("Do you want to continue? [y/n]") == "n" else True