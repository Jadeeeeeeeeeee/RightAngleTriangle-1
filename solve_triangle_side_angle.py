import math

def solve_missing_side_w_angle_side():
    while True:
        missing_side = input("What side do you have?(a/b/c):").lower()
       
        if missing_side not in ['a', 'b', 'c']:
            print("Invalid side. Please pick 'a' or 'b' or 'c'")
            continue
             
        known_side = float(input(f"Side {missing_side}: "))
        known_angle = float(input(f"Angle {missing_side:}:"))
      
        if missing_side == "a":
            side_b = known_side
            angle_A = math.radians(known_angle)
            side_a = side_b / math.tan(angle_A)
      
        elif missing_side == "b":
          side_a = known_side
          angle_A = math.radians(known_angle)
          side_b = side_a / math.tan(angle_A)
        else:
          angle_B = math.radians(known_angle)
          side_c = known_side
          side_a = side_c * math.cos(angle_A)
          side_b = side_c * math.cos(angle_A)
      
        angle_B = (90 - known_angle)
      
        print(f"Side a{side_a}:\nSide b{side_b}:\nangleB{angle_B}")
        print(f"Side c:{math.sqrt(side_a**2 + side_b**2)}\n")
         

solve_missing_side_w_angle_side()


  

 
