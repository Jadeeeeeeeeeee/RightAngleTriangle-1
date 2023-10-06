import math 

def solve_triangle_angle_side():    
    ask_for_side = input("Which side do you have?: ").lower()
    given_side = float(input(f"Please input side {ask_for_side}: "))

    ask_for_angle = input("Which angle do you have?: ").lower()
    given_angle = float(input(f"Please input angle {ask_for_angle}: "))
   
    if ask_for_angle == "a":
        if ask_for_side == "a":
            side_a = given_side
            side_b = side_a / math.tan(math.radians(given_angle))
            side_c = side_a / math.sin(math.radians(given_angle))   
        elif ask_for_side == "b":
            side_a = side_b * math.tan(math.radians(given_angle))
            side_b = given_side
            side_c = side_b / math.cos(math.radians(given_angle)) 
        else:
            side_a = side_c * math.sin(math.radians(given_angle))
            side_b = side_c * math.cos(math.radians(given_angle))
            side_c = given_side
    else:
        if ask_for_side == "a":
          side_a = given_side
          side_b = side_a * math.tan(math.radians(given_angle))
          side_c = side_a / math.cos(math.radians(given_angle))

        elif ask_for_side == "b":
          side_a = side_b / math.tan(math.radians(given_angle))
          side_b = given_side
          side_c = side_b / math.sin(math.radians(given_angle))

        else:
          side_a = side_c * math.cos(math.radians(given_angle))
          side_b = side_c * math.sin(math.radians(given_angle))
          side_c = given_side

    angle_B = (90 - given_angle)
      
    print(f"\nResults:\nside a: {side_a}\nside b: {side_b}\nside c: {side_c}\nangle_A: {given_angle} \nAngle B: {angle_B}")

solve_triangle_angle_side()
    





  

    