
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
  print("\n------------------------\n|-_-_-Instructions-_-_-|\n------------------------\n•Choose what you are given e.g. two sides / side and angle\n•Input the given sides or given side and angle then solve.\n•Type quit in the menu to end the session and view calculation history")

response_choices = ["yes", "no"]

want_instructions = string_checker("Do you want to read the instructions (yes/no):",1 ,response_choices)

if want_instructions == "yes":
  instructions()
