import glob
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



map_files = sorted(glob.glob("map_*.txt"))

# 😀
# 🌿
# 🌳
# 🌊
# 🢂🢁🢃🢀
def load_map (txt):
    file = open(txt, 'r')
    lines= file.readlines()
    WIDTH= int(lines[0])
    HEIGHT = len(lines) - 1
    file.close()
    return {"width": WIDTH,"height": HEIGHT, "map": list("".join( lines[1:]).replace("\n",""))}

current_map_idx = 0
loaded_map = load_map(map_files[current_map_idx])
MAP = loaded_map["map"]
WIDTH = loaded_map["width"]
HEIGHT = loaded_map["height"]

"""
    linijki_oprocz_pierwszej = lines[1:]
    linijki_polaczone_w_jeden_lancuch = "".join(linijki_oprocz_pierwszej)
    lancuch_bez_znakow_nowej_linii = linijki_polaczone_w_jeden_lancuch.replace("\n", "")
 
   lancuch_zamieniony_na_liste_charakterow = list(lancuch_bez_znakow_nowej_linii)
"""

# MAP = list("".join(lines[1:]).replace("\n", ""))



SYMBOLS = {
    ".": "🌿",
    "t": "🌳",
 
    "w": "🌊",
    "f": "🍓",
    "c": "🌵"
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
        print(end = "\n") 


direction = "up"
x, y = 0, 0
punkty = 0
number_of_times = 0
serduszka = 3
print("""Witamy w grze wideo! 
Zeby zakkonczyc gre: nacisnij "q" 
UWAGA: Masz 3 zycia: zeby ich nie stracic nie wchodz na kaktusy!
Dobrej zabawy!
Nacisnij "s" zeby zaczac gre!
 """)

keyboard.wait("s")
time.sleep(1)
while True:
    os.system("cls")
 
    # for x in range (serduszka):
    #     print("❤️ ",end="")
    # print("")
    print(f"Punkty: {punkty}")
    print("❤️ "* serduszka )
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
                # serduszka -= 1
                # print("Oh nie! zgubiles serduszko!")
                continue
            if MAP[newx+newy*WIDTH] in ("w", "t"):
                continue

            if MAP[newx+newy*WIDTH] =="c":
                serduszka -= 1
            elif serduszka == 0:
                print("GAME OVER")
                break

            x, y = newx, newy
            number_of_times += 1
            if MAP[x + y*WIDTH] == "f":
                MAP[x + y*WIDTH] = "."
                punkty += 1
            if "f" not in MAP:
                os.system("cls")
           
                print(f"Skonczyles poziom {current_map_idx + 1}!")
                current_map_idx += 1
                if current_map_idx < len(map_files):
                    loaded_map = load_map(map_files[current_map_idx])
                    MAP = loaded_map["map"]
                    WIDTH = loaded_map["width"]
                    HEIGHT = loaded_map["height"]
                    x, y = 0, 0
                    print("Nacisnij ENTER aby przejsc do nastepnego poziomu")
                    keyboard.wait("enter")
                    continue
                break # Nie ma juz map do zaladowania => Koniec gry

            
        case "q": break

        case other: print("Nie rozpoznano komedy.")
    time.sleep(.2)
    
print(f"koniec gry! Zrobiles {number_of_times} poruszen. ") 
    
       

