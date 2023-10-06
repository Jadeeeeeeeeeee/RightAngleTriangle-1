import math 


def solve_triangle_two_sides():

  missing_side = input("What side are you missing(a/b/c)?:").lower()

  
  if missing_side == "a":

    side_b = float(input("side b:"))
    side_c = float(input("side c:"))

    while side_c <= side_b:
      print("\nPlease make sure that side c is larger than side b")
      side_c = float(input("side c:"))
 
    side_a = (math.sqrt(side_c**2 - side_b**2))
    Angle_A = math.degrees(math.asin(side_b / side_c))

    Angle_B = (90 - Angle_A)
    

  elif missing_side == "b":

    side_a = float(input("side a:"))
    side_c = float(input("side c:"))

    while side_c <= side_b:
      print("\nPlease make sure that side c is larger than side a")
      side_c = float(input("side c:")) 

    side_b = (math.sqrt(side_c**2 - side_a**2))
    Angle_A = math.degrees(math.acos(side_a / side_c))

    Angle_B = (90 - Angle_A)

  else:
    side_a = float(input("side a:"))
    side_b = float(input("side b:"))

    side_c = (math.sqrt(side_b**2 - side_a**2))
    Angle_A = math.degrees(math.atan(side_a / side_b))

    Angle_B = (90 - Angle_A)

  print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle A: {Angle_A} \nAngle B: {Angle_B}")
  

solve_triangle_two_sides()
    
    
    

    

  
    




