# Author: Jason Turney jnt5211@psu.edu
# Collaborator:
# Collaborator:
# Collaborator:
# Section: 1
# Breakout: 

def getLetterGrade(grade):
  if grade >= 93.0:
    grade = "A"
  elif grade >= 90.0:
    grade = "A-"
  elif grade >= 87.0:
    grade = "B+"
  elif grade >= 83.0:
    grade = "B"
  elif grade >= 80.0:
    grade = "B-"
  elif grade >= 77.0:
    grade = "C+"
  elif grade >= 70.0:
    grade = "C"
  elif grade >= 70.0:
    grade = "D"
  else:
    grade = "F"
  return grade

def run():
  grade = float(input("Enter your CMPSC 131 grade: "))
  print(getLetterGrade(grade))

if __name__ == "__main__":
  run()