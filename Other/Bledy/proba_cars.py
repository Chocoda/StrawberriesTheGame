x,y, direction = 1,1, "up"
HEIGHT = 5
WIDTH = 5
# 😀
# 🌿
# 🌳
# 🢂🢁🢃🢀

MAP = """\
.....\
.....\
.....\
..t..\
....t\
"""

ARROWS = {"up": "🢁", "down": "🢃", "right": "🢂", "left": "🢀" }
while True:
    dx, dy = 0, 0
    command = input("> ").strip().lower()
    match command:
        case "turn right": 
            match direction:
                case "up": direction = "right"
                case "down": direction = "left"
                case "right": direction = "down"
                case "left": direction = "up"
        case "turn left":
            match direction:
                case "up": direction = "left"
                case "down": direction = "right"
                case "right": direction = "up"
                case "left": direction = "down"
        case "forward":
            match direction:
                case "up": dy = -1
                case "down": dy = 1
                case "right": dx = 1
                case "left": dx = -1
        case "backward":
            match direction:
                case "up": dy = 1
                case "down": dy = -1
                case "right": dx = -1
                case "left": dx = 1
        case "strafe right":
            match direction:
                case "up": dx = 1
                case "down": dx = -1
                case "right": dy = 1
                case "left": dy = -1
        case "strafe left":
            match direction:
                case "up": dx = -1
                case "down": dx = 1
                case "right": dy = -1
                case "left": dy = 1   
        case other:
            match command:
                case "quit": break
                case "position":
                    print(f"({x},{y})")
                    for row in range (1, HEIGHT +1):
                        for col in range (1, WIDTH +1):
                            #print(ARROWS[direction] if row == y and col == x else "🌿", end= "\n" if col == WIDTH else "" )     
                            i = row - 1
                            j = col - 1
                            if row == y and col == x:
                                print (ARROWS[direction], end="")
                    
                            else:
                                if MAP[i*WIDTH+j] == ".":
                                    print("🌿", end="")
        
                                if MAP[i*WIDTH+j] == "t":
                                    print("🌳",end= "")
                            if col == WIDTH: print("")

                case other:
                    print("Nie rozpoznano komedy.")

    new_x, new_y = x+dx, y+dy
    new_i = new_y - 1
    new_j = new_x - 1
    at_new_position = MAP[new_i*WIDTH + new_j]
    if new_x <1 or new_y <1 or new_x > WIDTH or new_y > HEIGHT or at_new_position == "t":
        print("Nie moge wykonac tego ruchu bo wyszedlbym poza pole ruchu.")
        continue
    x, y = new_x, new_y
    print(f"Jestes na pozycji {new_x} , {new_y}")



