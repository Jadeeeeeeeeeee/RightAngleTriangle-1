
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
  print("==============\n=Instructions=\n==============\n• Choose what you are solving for (missing side/missing angle)\n• Input the given sides/angles\n• Solve  ")

response_choices = ["yes", "no"]

want_instructions = string_checker("Do you want to read the instructions (yes/no):",1 ,response_choices)

if want_instructions == "yes":
  instructions()
