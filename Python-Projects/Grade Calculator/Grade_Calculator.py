################################################################################
# Python challenge: Grade calculator
#
# Name: Matej Haas
# Matriculation number: 00872249
################################################################################

# Add your code below
CHALLENGE_POINTS = 0
ASSIGNMENT_POINTS = 0
ASSIGNMENT_REVIEW_POINTS = 0
POINTS_TOTAL = 0
GRADES = {1: "Sehr Gut (1)",
          2: "Gut (2)",
          3: "Befriedigend (3)",
          4: "Genügend (4)", 
          5: "Nicht Genügend (5)"}


def get_challenge_points():
  global CHALLENGE_POINTS
  points = input("Enter your achieved points for the challenge: ")

  while True:    
    if not points.isnumeric():
      print("Input Error. Please enter a valid integer between 0 and 20") 
      points = input("Enter your achieved points for the challenge: ") 
    
    elif not (20 >= int(points) >= 0):
      print("Input Error. Please enter a valid integer between 0 and 20")
      points = input("Enter your achieved points for the challenge: ")
    
    else:
      CHALLENGE_POINTS = int(points)
      break


def get_assignment_points():
  global ASSIGNMENT_POINTS
  points = input("Enter your achieved points for the assignment: ")

  while True:    
    if not points.isnumeric():
      print("Input Error. Please enter a valid integer between 0 and 70") 
      points = input("Enter your achieved points for the assignment: ") 
    
    elif not (70 >= int(points) >= 0):
      print("Input Error. Please enter a valid integer between 0 and 70")
      points = input("Enter your achieved points for the assignment: ")
    
    else:
      ASSIGNMENT_POINTS = int(points)
      break


def check_att_review():
  global ATTENDED_ASSIGNMENT_REVIEW
  review = input("Did you attend the assignment review? ")
  
  while True:
    if not review.lower() in ("yes", "no"):
      print("Input Error. Please enter either 'yes' or 'no'")
      review = input("Did you attend the assignment review? ")
    
    elif review.lower() == "no":
      print("The assignment review is MANDATORY!")
      review = input("Did you attend the assignment review? ")
    
    else:
      break


def get_review_points():
  global ASSIGNMENT_REVIEW_POINTS
  points = input("Enter your achieved points for the assignment review: ")
  
  while True:
    if not points.isnumeric():
      print("Input Error. Please enter a valid integer between 0 and 10") 
      points = input("Enter your achieved points for the assignment review: ") 
    
    elif not (10 >= int(points) >= 0):
      print("Input Error. Please enter a valid integer between 0 and 10")
      points = input("Enter your achieved points for the assignment review: ")
    
    else:
      ASSIGNMENT_REVIEW_POINTS = int(points)
      break


def calculate_points_total():
  global POINTS_TOTAL
  
  if ASSIGNMENT_REVIEW_POINTS > 0:
    POINTS_TOTAL = CHALLENGE_POINTS + ASSIGNMENT_POINTS + ASSIGNMENT_REVIEW_POINTS
  
  else:
    POINTS_TOTAL = 0


def print_grade():
  if ASSIGNMENT_REVIEW_POINTS == 0:
    print("You need more than 0 points on the assignment review to pass this course.")
    grade = 5
  
  else:
    if POINTS_TOTAL < 50:
      grade = 5
    
    elif POINTS_TOTAL < 63:
      grade = 4
    
    elif POINTS_TOTAL < 78:
      grade = 3
    
    elif POINTS_TOTAL < 90:
      grade = 2
    
    else:
      grade = 1
    
  print(f"Based on your input your grade will be: {GRADES[grade]}")


def main():
  get_challenge_points()
  get_assignment_points()
  check_att_review()
  get_review_points()
  calculate_points_total()
  print_grade()


if __name__ == "__main__":
  main()
