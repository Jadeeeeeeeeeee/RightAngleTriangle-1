def num_check(question):

  while True:

    try:
      response = float(input(question))
      return response

    except ValueError:
      print("Please enter a number")



side_a = num_check("Side a:")

print(f"side a:{side_a}")
