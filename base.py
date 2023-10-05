import math

#List of response for questions
response_choices = ["yes", "no", "n","y" ]
side_choices = ["a", "b", "c"]
angle_choices = ["a", "b"]
menu_choices = ["1", "2"]

def string_checker(question, num_response, valid_response):

  if num_response == "2":
   error = "Please choose {} or {}".format(valid_response[0],valid_response[1])

  else:
    error = "Please choose {}, {} or {}".format(valid_response[0],valid_response[1],valid_response[2])

  if num_response == 1:
    short_version = 1

  else:
    short_version = 2
  

  while True:
    response = input(question).lower()

    for item in valid_response:
      if item[:short_version] == valid_response or response == item:
        return item


    print(error)

def num_check(question):

  while True:

    try:
      response = float(input(question))
      return response

    except ValueError:
      print("\nPlease enter a number")


def menu():

  print("******************************************\n**Welcome to rignt angle triangle solver**\n******************************************")

  want_instructions = string_checker("\nWould you like to the view instructions? (yes/no):",1 ,response_choices)

  if want_instructions == "yes" or want_instructions == "y":
    instructions()

  else:
     print("")
     pass

  while True:
    print("\n------------\n|-_-Menu-_-|\n------------\n1. Solve triangle(you have 2 sides)\n2. Quit\nWhat would you like to do?(1/2):")
    

    choice = input().lower()

    if choice == "1" or choice == "Solve for missing side":
      calculate_missing_side()

    elif choice == "2" or choice == "Quit":
      print("\nThanks for using right angle triangle solver")
      break

    else:
      print("Please pick a valid option, either the number or the word")


#Instructions for the user to use
#Main routine
def instructions():
  print("\n------------------------\n|-_-_-Instructions-_-_-|\n------------------------\n•Choose what you are given e.g. two sides / side and angle.\n•Input the given sides or given side and angle then solve.\n•Type quit in the menu to end the session and view calculation history.")

def calculate_missing_side():

  missing_side = string_checker("\nWhat side are you missing?",3 ,side_choices).lower()

  
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
    side_b = num_check("side b:")

    side_c = (math.sqrt(side_b**2 - side_a**2))
    Angle_A = math.degrees(math.atan(side_a / side_b))

    Angle_B = (90 - Angle_A)

    print(f"\nResults:\nside a: {side_b}\n{Angle_A} \nAngle B: {Angle_B}")






menu()
    
    
