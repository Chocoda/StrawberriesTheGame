# 😀
# 🌿
# 🌳
# 🌊
# 🢂🢁🢃🢀

MAP = """\
...ww\
....w\
.....\
..t..\
....t\
"""
WIDTH = 5
HEIGHT = 5
SYMBOLS = {
    ".": "🌿",
    "t": "🌳",
    "w": "🌊"
}

newx, newy = 1,1
DIRECTIONS = {"up":("🢁"), "right":("🢂"), "down": ("🢃"), "left": ("🢀")}
MOVEMENTS = ["turn right", "turn left", "forward", "backward"]
direction = "up"
while True:
    x,y= newx, newy
    dx, dy = 0,0
    command =input("> "  ).lower()
    if command in MOVEMENTS:
        match command:
            case "turn right":
                if direction == "up": direction = "right"
                elif direction == "right": direction = "down"
                elif direction == "down": direction = "left"
                else: direction = "up"
                print(f"Skreciles w prawo. Jestes w kierunku {direction}")

            case "turn left":
                if direction == "up": direction = "left"
                elif direction == "right": direction = "up"
                elif direction == "down": direction = "right"
                else : direction = "down"
                print(f"Skreciles w lewo. Jestes w kierunku {direction}")

            case "forward":
                if direction == "up": dy-=1
                elif direction == "right": dx += 1
                elif direction == "down": dy+= 1
                else: dx-=1
                newx, newy = x+dx, y+dy
                if newx < 1 or newy < 1 or newx > WIDTH or newy > HEIGHT: 
                    print(f"Nie moge wykonac tego ruchu bo wyszedlbym poza pole gry. Pozostajesz na pozycji {x}, {y}")
                    newx, newy = newx - dx, newy - dy
                else: 
                    print(f"Posunales sie . Jestes na pozycji {newx},{newy}")

        
            case "backward":
                if direction == "up": dy+=1
                elif direction == "right": dx -= 1
                elif direction == "down": dy-= 1
                else: dx+=1   
                newx, newy = x+dx, y+dy
                if newx < 1 or newy < 1 or newx > WIDTH or newy > HEIGHT: 
                    print(f"Nie moge wykonac tego ruchu bo wyszedlbym poza pole gry. Pozostajesz na pozycji {x}, {y}")
                    newx, newy = x-dx, y-dy
                else: 
                    print(f"Posunales sie . Jestes na pozycji {newx},{newy}")
        

    else:
        match command:          
            case "quit": break
            case  "position":
                for row in range (1,HEIGHT+1):
                    for col in range (1,WIDTH+1):
                        if col+row*WIDTH == (newx)+(newy)* WIDTH :
                                print(DIRECTIONS[direction], end="")
                        else:
                            ascii_symbol = MAP[(col-1) + WIDTH*(row-1)]
                            emoji_symbol = SYMBOLS[ascii_symbol]
                            print(emoji_symbol, end = "")
                    print("") 
                print(f"{newx},{newy}")
            case other: print("Nie rozpoznano komedy.")

    
       

