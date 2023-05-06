import keyboard
import os
import time

def key_to_en(key):
    match key:
        case "haut": return "up"
        case "droite": return "right"
        case "bas": return "down"
        case "gauche": return "left"
        case other: return key


# 😀
# 🌿
# 🌳
# 🌊
# 🢂🢁🢃🢀

MAP = list("""\
...ww\
....w\
f....\
..t..\
.f..t\
""")

WIDTH = 5
HEIGHT = 5
SYMBOLS = {
    ".": "🌿",
    "t": "🌳",
    "w": "🌊",
    "f": "🍓"
}

newx, newy = 1,1
DIRECTIONS = {"up":("🢁"), "right":("🢂"), "down": ("🢃"), "left": ("🢀")}
DIR_NAMES = ["up", "right", "down", "left"]
MOVEMENTS = ["turn right", "turn left", "forward", "backward"]


def print_map(mtx, width, prow, pcol, pdir):
    height = len(mtx) // width

    for row in range (height):
        for col in range (width):
            if row == prow and col == pcol :
                print(DIRECTIONS[direction], end="")

            else:
                ascii_symbol = mtx[col + width*row]
                emoji_symbol = SYMBOLS[ascii_symbol]
                print(emoji_symbol, end = "")
        print("") 


direction = "up"
x, y = 0, 0
punkty = 0
while True:
    os.system("cls")

    print(f"Punkty: {punkty}")
    print_map(MAP, WIDTH, y, x, direction)
    dx, dy = 0,0
    command = key_to_en(keyboard.read_key())
    match command:
        case "right" | "left":
            dir_idx = DIR_NAMES.index(direction)
            didx = 1 if command == "right" else -1
            new_dir_idx = (dir_idx + didx) % 4
            direction = DIR_NAMES[new_dir_idx]

        case "up" | "down":
            match direction:
                case "up": dy =-1
                case "right": dx = 1
                case "down": dy = 1
                case "left": dx = -1

            if command == "down":
                dx *= -1
                dy *= -1
            newx, newy = x+dx, y+dy


            if newx < 0 or newy < 0 or newx >= WIDTH or newy >= HEIGHT: 
                continue
            if MAP[newx+newy*WIDTH] in ("w", "t"):
                continue

            x, y = newx, newy

            if MAP[x + y*WIDTH] == "f":
                MAP[x + y*WIDTH] = "."
                punkty += 1
            
        case "q": break

        case other: print("Nie rozpoznano komedy.")


    
    time.sleep(.2)
    
       

