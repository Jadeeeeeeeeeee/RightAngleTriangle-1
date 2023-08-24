import math

def menu():

  print("******************************************\n**Welcome to rignt angle triangle solver**\n******************************************")

  want_instructions = string_checker("\nDo you want to read the instructions (yes/no):",1 ,response_choices)

  if want_instructions == "yes":
    instructions()

  else:
     print("")
     pass

  while True:
    print("\nMenu:\n1. Solve for missing side(you have 2 sides)\n2. Quit\nWhat would you like to do?:")
    

    response = input().lower()

    if response == "1" or response == "Solve Triangle":
      calculate_missing_side()

    elif response == "2" or response == "Quit":
      print("\nThanks for using right angle triangle solver")
      break

    else:
      print("Please pick a valid option, either the number or the word")


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
#Instructions for the user to use
#Main routine


def instructions():
  print("Instructions:")
  print("Choose what you want to solve for eg. missing side / missing angle.")
  print("Input whatever is the numbers that you have.")
  print("Solve.")
  print("Type 3 or History in the menu to view calculation history.")
  print("Type 4 or quit on the menu to quit solving.")

def calculate_missing_side():

  missing_side = input("\nWhat side are you missing(a/b/c)?").lower()

  
  if missing_side == "a":

    side_b = float(input("side b:"))
    side_c = float(input("side c:"))
 
    side_a = (math.sqrt(side_c**2 - side_b**2))
    angle_A = math.degrees(math.asin(side_b / side_c))

    Angle_B = (90 - angle_A)

    print(f"\nResults:\nside a: {side_a}\nangle_A: {angle_A} \nAngle B: {Angle_B}")

  elif missing_side == "b":

    side_a = float(input("side a:"))
    side_c = float(input("side c:"))

    side_b = (math.sqrt(side_c**2 - side_a**2))
    Angle_A = math.degrees(math.asin(side_a / side_c))

    Angle_B = (90 - Angle_A)

    print(f"\nResults:\nside a: {side_b}\nAngle A:{Angle_A} \nAngle B: {Angle_B}")

  else:
    side_a = float(input("side a:"))
    side_b = float(input("side c:"))

    side_c = (math.sqrt(side_a**2 - side_b**2))
    Angle_A = math.degrees(math.asin(side_a / side_b))

    Angle_B = (90 - Angle_A)

    print(f"\nResults:\nside a: {side_b}\n{Angle_A} \nAngle B: {Angle_B}")
  

response_choices = ["yes", "no"]

menu()
    
    
