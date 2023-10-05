import math 

def solve_triangle_angle_side():

    
    ask_for_side = input("Which side do you have?: ").lower()
  
    given_side = float(input(f"Please input side {ask_for_side}: "))

    ask_for_angle = input("Which angle do you have?: ").lower()
  
    given_angle = float(input(f"Please input angle {ask_for_angle}: "))
   
    if given_angle == "a":
      if given_side == "a":
        side_a = given_side
        side_b = (given_side / math.tan(math.radians(given_angle)))
        side_c = (given_side / math.sin(math.radians(given_angle)))
  
      elif given_side == "a":
        side_a = (given_side * math.tan(math.radians(given_angle)))
        side_b = given_side
        side_c = (given_side / math.cos(math.radians(given_angle)))
  
      else:
        side_a = (given_side * math.sin(math.radians(given_angle)))
        side_b = (given_side * math.cos(math.radians(given_angle)))
        side_c = given_side
  
      angle_B = (90 - given_angle)
  
      print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle_A: {given_angle} \nAngle B: {angle_B}")

solve_triangle_angle_side()
    





  

    