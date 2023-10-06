def menu():

  print("******************************************\n**Welcome to rignt angle triangle solver**\n******************************************")

  while True:
    print("\nOptions:\n1. Solve Triangle\n2. Quit")

    response = input().lower()

    if response == "1" or response == "Solve Triangle":
      print("solve triangle")

    elif response == "2" or response == "Quit":
      print("\nThanks for using right angle triangle solver")
      break

    else:
      print("Please pick a valid option, either the number or the word")

def instructions():
  print("Instructions:")

def solve_triangle_2_sides():
  print("Solve triangle with two sides")

def solve_triangle_angle_side():
  print("Solve triangle with side and angle")