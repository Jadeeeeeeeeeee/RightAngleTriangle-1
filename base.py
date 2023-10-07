import math

#List of response for questions
response_choices = ["yes", "no",]
side_choices = ["a", "b", "c"]
angle_choices = ["a", "b"]

#List to store calculation history
history = []

#Functions
#Stringchekcer that checks whether the user has entered a valid respone or not
def string_checker(question, num_response, valid_response):
    if num_response == 2:
        error = "Please choose {} or {}".format(valid_response[0], valid_response[1])
    elif num_response == 3:
        error = "Please choose {}, {}, or {}\n".format(valid_response[0], valid_response[1], valid_response[2])

    while True:
        response = input(question).lower()

        if response in valid_response:
            return response

        print(error)



#This function checks whether the user has entered a number or not
def num_check(question):

  while True:

    try:
      response = float(input(question))
      return response

    except ValueError:
      print("\nPlease enter a number")

#The instructions on how to use the program
def instructions():
  print("\n------------------------\n|-_-_-Instructions-_-_-|\n------------------------\n•Choose what you are given e.g. two sides / side and angle.\n•Input the given sides or given side and angle to solve.\n•Type quit in the menu to end the session and view calculation history.")

#A menu for users to use as their main tool to control the program, whether they want to solve triangle or quit using the program.
def menu():

  print("******************************************\n**Welcome to rignt angle triangle solver**\n******************************************")

  want_instructions = string_checker("\nWould you like to the view instructions? (yes/no):", 2, response_choices)

  if want_instructions == "yes":
    instructions()

  print("")


  while True:
    print("\n------------\n|-_-Menu-_-|\n------------\n1. Solve Triangle(you have 2 sides)\n2. Solve Triangle(you have a side and an angle)\n3. Quit\nWhat would you like to do?(1/2/3):")
    

    choice = input().lower()

    if choice == "1":
      solve_triangle_two_sides()

    elif choice == "2":
      solve_triangle_angle_side()

    elif choice == "3":
      print("Thanks for using right angle triangle solver")
      break
      
    else:
      print("Please pick a valid option, 1, 2 or 3")

#This function is for solving right angle triangle when given two sides
def solve_triangle_two_sides():

  #Ask the user what side they are missing to know which sides they have
  missing_side = string_checker("\nWhat side are you missing(a/b/c)?:", 3, side_choices)


#Ask the user about the remaining sides after knowing which one is missing  
  if missing_side == "a":

    side_b = num_check("side b:")
    side_c = num_check("side c:")

    #This makes sure that side c is larger than side a or b becuase in a right angle triangle side c is always larger than side a and be
    while side_c <= side_b:
      print("\nPlease make sure that side c is larger than side b")
      side_c = num_check("side c:")
 
    side_a = (math.sqrt(side_c**2 - side_b**2))
    Angle_A = math.degrees(math.asin(side_b / side_c))

    Angle_B = (90 - Angle_A)
    

  elif missing_side == "b":

    side_a = num_check("side a:")
    side_c = num_check("side c:")

    while side_c <= side_a:
      print("\nPlease make sure that side c is larger than side a")
      side_c = num_check("side c:")

    side_b = (math.sqrt(side_c**2 - side_a**2))
    Angle_A = math.degrees(math.acos(side_a / side_c))

    Angle_B = (90 - Angle_A)

  else:
    side_a = num_check("side a:")
    side_b = num_check("side b:")

    side_c = (math.sqrt(side_b**2 - side_a**2))
    Angle_A = math.degrees(math.atan(side_a / side_b))

    Angle_B = (90 - Angle_A)

  #Print the results of the calculation
  print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle A: {Angle_A} \nAngle B: {Angle_B}")

#This fucntion solves the triangle when given  
def solve_triangle_angle_side():    
    ask_for_side = string_checker("\nWhich side do you have?: ", 3, side_choices )
    given_side = num_check(f"Please input side {ask_for_side}: ")

    ask_for_angle = string_checker("\nWhich angle do you have?(a/b): ", 2, angle_choices)
    given_angle = num_check(f"Please input angle {ask_for_angle}: ")
    
    if ask_for_angle == "a":
        if ask_for_side == "a":
            side_a = given_side
            side_b = side_a / math.tan(math.radians(given_angle))
            side_c = side_a / math.sin(math.radians(given_angle))
          
        elif ask_for_side == "b":
            side_b = given_side
            side_a = side_b * math.tan(math.radians(given_angle))
            side_c = side_b / math.cos(math.radians(given_angle))

        else:
            side_c = given_side
            side_a = side_c * math.sin(math.radians(given_angle))
            side_b = side_c * math.cos(math.radians(given_angle))
            
        Angle_A = given_angle
        Angle_B = (90 - given_angle)
   
    else:
        if ask_for_side == "a":
          side_a = given_side
          side_b = side_a * math.tan(math.radians(given_angle))
          side_c = side_a / math.cos(math.radians(given_angle))
          Angle_B = given_angle
          Angle_A = (90 - given_angle)

        elif ask_for_side == "b":
          side_b = given_side
          side_a = side_b / math.tan(math.radians(given_angle))
          side_c = side_b / math.sin(math.radians(given_angle))
          Angle_B = given_angle
          Angle_A = (90 - given_angle)

        else:
          side_c = given_side
          side_a = side_c * math.cos(math.radians(given_angle))
          side_b = side_c * math.sin(math.radians(given_angle))
          Angle_B = given_angle
          Angle_A = (90 - given_angle)
      
    print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle_A: {Angle_A} \nAngle B: {Angle_B}")

    #store the calculation history
  history.append(f"\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle_A: {Angle_A} \nAngle B: {Angle_B}")


menu()


    
    
