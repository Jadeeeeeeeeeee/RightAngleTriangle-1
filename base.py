import math

#List of response for questions
response_choices = ["yes", "no",]
side_choices = ["a", "b", "c"]
angle_choices = ["a", "b"]
menu_choices = ["1", "2", "3"]

def string_checker(question, num_response, valid_response):

  if num_response == "3":
        error = "Please choose {}, {} or {}".format(valid_response[0],valid_response[1],valid_response[2])

  else:
    error = "Please choose {} or {}".format(valid_response[0],valid_response[1])

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

  want_instructions = string_checker("\nWould you like to the view instructions? (yes/no):", 2, response_choices)

  if want_instructions == "yes":
    instructions()

  print("")


  while True:
    print("\n------------\n|-_-Menu-_-|\n------------\n1. Solve Triangle(you have 2 sides)\n2. Solve Triangle(you have a side and an angle)\n3. Quit\nWhat would you like to do?(1/2):")
    

    choice = input().lower()

    if choice == "1":
      solve_triangle_2_sides()

    elif choice == "2":
      solve_triangle_angle_side()

    elif choice == "3":
      print("Thanks for using right angle triangle solver")
      break
      
    else:
      print("Please pick a valid option, 1, 2 or 3")


#Instructions for the user to use
#Main routine
def instructions():
  print("\n------------------------\n|-_-_-Instructions-_-_-|\n------------------------\n•Choose what you are given e.g. two sides / side and angle.\n•Input the given sides or given side and angle then solve.\n•Type quit in the menu to end the session and view calculation history.")

def solve_triangle_two_sides():

  missing_side = input("What side are you missing(a/b/c)?").lower()
  
  if missing_side == "a":

    side_b = float(input("side b:"))
    side_c = float(input("side c:"))
 
    side_a = (math.sqrt(side_c**2 - side_b**2))
    angle_A = math.degrees(math.asin(side_b / side_c))

    Angle_B = (90 - angle_A)

    print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle_A: {angle_A} \nAngle B: {Angle_B}")

  elif missing_side == "b":

    side_a = float(input("side a:"))
    side_c = float(input("side c:"))

    side_b = (math.sqrt(side_c**2 - side_a**2))
    Angle_A = math.degrees(math.acos(side_a / side_c))

    Angle_B = (90 - Angle_A)

    print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle_A: {angle_A} \nAngle B: {Angle_B}")

  else:
    side_a = float(input("side a:"))
    side_b = float(input("side c:"))

    side_c = (math.sqrt(side_b**2 - side_a**2))
    Angle_A = math.degrees(math.atan(side_a / side_b))

    Angle_B = (90 - Angle_A)

    print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle_A: {angle_A} \nAngle B: {Angle_B}")
  
def solve_triangle_angle_side():    
    ask_for_side = string_checker("Which side do you have?: ", 3, side_choices )
    given_side = float(input(f"Please input side {ask_for_side}: "))

    ask_for_angle = input("Which angle do you have?: ").lower()
    given_angle = float(input(f"Please input angle {ask_for_angle}: "))
   
    if ask_for_angle == "a":
        if ask_for_side == "a":
            side_a = given_side
            side_b = side_a / math.tan(math.radians(given_angle))
            side_c = side_a / math.sin(math.radians(given_angle))   
        elif ask_for_side == "b":
            side_a = side_b * math.tan(math.radians(given_angle))
            side_b = given_side
            side_c = side_b / math.cos(math.radians(given_angle)) 
        else:
            side_a = side_c * math.sin(math.radians(given_angle))
            side_b = side_c * math.cos(math.radians(given_angle))
            side_c = given_side
    else:
        if ask_for_side == "a":
          side_a = given_side
          side_b = side_a * math.tan(math.radians(given_angle))
          side_c = side_a / math.cos(math.radians(given_angle))

        elif ask_for_side == "b":
          side_a = side_b / math.tan(math.radians(given_angle))
          side_b = given_side
          side_c = side_b / math.sin(math.radians(given_angle))

        else:
          side_a = side_c * math.cos(math.radians(given_angle))
          side_b = side_c * math.sin(math.radians(given_angle))
          side_c = given_side

    angle_B = (90 - given_angle)
      
    print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle_A: {given_angle} \nAngle B: {angle_B}")

menu()
    
    
