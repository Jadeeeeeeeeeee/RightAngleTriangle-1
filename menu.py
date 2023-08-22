def menu():

  print("Welcome to rignt angle triangle solver, what would you like to do?")

  while True:
    print("\nOptions:")
    print("1. Instructions")
    print("2. Solve Triangle")
    print("3. History")
    print("4. Quit")

    response = input().lower()

    if response == "1" or response == "Instructions":
      instructions()
     
    elif response == "2" or response == "Solve Triangle":
      print("solve triangle")

    elif response == "3" or response == "History" :
      print("History")

    elif response == "4" or response == "Quit":
      print("Thanks for using right angle triangle solver")
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