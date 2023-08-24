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
  print("Choose what you want to solve for eg. missing side / missing angle.")
  print("Input whatever is the numbers that you have.")
  print("Solve.")
  print("Type 3 or History in the menu to view calculation history.")
  print("Type 4 or quit on the menu to quit solving.")

menu()
