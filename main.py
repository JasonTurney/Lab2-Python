# Author: Jason Turney jnt5211@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 

grade = float(input("Enter your CMPSC 131 grade: "))
def getLetterGrade(grade):
  if grade >= 93.0:
    print("Your letter grade for CMPSC 131 is A.") 
  if grade >= 90.0 and grade < 93.0:
    print("Your letter grade for CMPSC 131 is A-.")
  if grade >= 87.0 and grade < 90.0:
    print("Your letter grade for CMPSC 131 is B+.")
  if grade >= 83.0 and grade < 87.0:
    print("Your letter grade for CMPSC 131 is B.")
  if grade >= 80.0 and grade < 83.0:
    print("Your letter grade for CMPSC 131 is B-.")
  if grade >= 77.0 and grade < 80.0:
    print("Your letter grade for CMPSC 131 is C+.")
  if grade >= 70.0 and grade < 77.0:
    print("Your letter grade for CMPSC 131 is C.")
  if grade >= 70.0 and grade < 60.0:
    print("Your letter grade for CMPSC 131 is D.")
  if grade < 60:
    print("Your letter grade for CMPSC 131 is F.")
getLetterGrade(grade)