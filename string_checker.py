def string_checker(question, num_letters, valid_response):

  error = "Please choose {} or {}".format(valid_response[0],valid_response[1])

  if num_letters == 1:
    short_version = 1

  else:
    short_version = 2
  

  while True:
    response = input(question).lower()

    for item in valid_response:
      if valid_response == item[short_version] or response == item:
        return item


    print(error)

def instructions():
  print("Instructions")
#Main routine
response_choices = ["yes", "no"]

want_instructions = string_checker("Do you want to view the instructions(y/n)?:", 1,response_choices)

if want_instructions == "yes" or want_instructions == "y":
  instructions()