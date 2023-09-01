import math

def string_checker(question, num_letters, valid_response):

  error = "Please choose {} or {}".format(valid_response[0],valid_response[1])

  if num_letters == 1:
    short_version = 1

  else:
    short_version = 2
  

  while True:
    response = input(question).lower()

    for item in valid_response:
      if valid_response == item[:short_version] or response == item:
        return item


    print(error)

def num_check(question):

  while True:

    try:
      response = float(input(question))
      return response

    except ValueError:
      print("Please enter a number")


def menu():

  print("******************************************\n**Welcome to rignt angle triangle solver**\n******************************************")

  want_instructions = string_checker("\nWould you like to the view instructions? (yes/no):",1 ,response_choices)

  if want_instructions == "yes" or want_instructions == "y":
    instructions()

  else:
     print("")
     pass

  while True:
    print("\n------------\n|-_-Menu-_-|\n------------\n1. Solve for missing side(you have 2 sides)\n2. Quit\nWhat would you like to do?(1/2):")
    

    response = input().lower()

    if response == "1" or response == "Solve for missing side":
      calculate_missing_side()

    elif response == "2" or response == "Quit":
      print("\nThanks for using right angle triangle solver")
      break

    else:
      print("Please pick a valid option, either the number or the word")


#Instructions for the user to use
#Main routine
def instructions():
  print("\n------------------------\n|-_-_-Instructions-_-_-|\n------------------------")
  print("\n•Choose what you want to solve for eg. missing side / missing angle.")
  print("•Input whatever is the numbers that you have.")
  print("•Solve.")
  print("•Type 3 or History in the menu to view calculation history.")
  print("•Type 4 or quit on the menu to quit solving.\n")

def calculate_missing_side():

  missing_side = input("\nWhat side are you missing(a/b/c)?").lower()

  
  if missing_side == "a":

    side_b = num_check("side b:")
    side_c = num_check("side c:")
 
    side_a = (math.sqrt(side_c**2 - side_b**2))
    angle_A = math.degrees(math.asin(side_b / side_c))

    Angle_B = (90 - angle_A)

    print(f"\nResults:\nside a: {side_a}\nangle_A: {angle_A} \nAngle B: {Angle_B}")

  elif missing_side == "b":

    side_a = num_check("side a:")
    side_c = num_check("side c:")

    side_b = (math.sqrt(side_c**2 - side_a**2))
    Angle_A = math.degrees(math.acos(side_a / side_c))

    Angle_B = (90 - Angle_A)

    print(f"\nResults:\nside a: {side_b}\nAngle A:{Angle_A} \nAngle B: {Angle_B}")

  else:
    side_a = num_check("side a:")
    side_b = num_check("side c:")

    side_c = (math.sqrt(side_b**2 - side_a**2))
    Angle_A = math.degrees(math.atan(side_a / side_b))

    Angle_B = (90 - Angle_A)

    print(f"\nResults:\nside a: {side_b}\n{Angle_A} \nAngle B: {Angle_B}")
  

response_choices = ["yes", "no", "n","y" ]

menu()
    
    
