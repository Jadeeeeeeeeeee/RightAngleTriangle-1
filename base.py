import math

def menu():

  print("******************************************\n**Welcome to rignt angle triangle solver**\n******************************************")

  while True:
    print("\nMenu:\n1. Solve Triangle\n2. Quit\nWhat would you like to do?:")
    

    response = input().lower()

    if response == "1" or response == "Solve Triangle":
      calculate_missing_side()

    elif response == "2" or response == "Quit":
      print("\nThanks for using right angle triangle solver")
      break

    else:
      print("Please pick a valid option, either the number or the word")

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
  

menu()
    
    
