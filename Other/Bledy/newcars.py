# 😀
# 🌿
# 🢂🢁🢃🢀

# print("😀", end="")
# print("ala zjadla\nkota")

WIDTH = 5
HEIGHT = 3
x, y, direction = 1, 1, "up"

ARROWS = {"up": "🢁", "right": "🢂", "down": "🢃", "left": "🢀"}
    
while True:
    dx, dy = 0, 0
    command = input("> ").strip().lower()
    match command:
        case "turn right":
            match direction:
                case "up": direction = "right"
                case "right": direction = "down"
                case "down": direction = "left"
                case "left": direction = "up"              
        case "turn left": 
            match direction:
                case "up": direction = "left"
                case "left": direction = "down"
                case "down": direction = "right" 
                case "right" : direction = "up"
        case "forward":
            if direction == "right": dx = 1
            if direction == "left": dx = -1
            if direction == "up": dy = -1
            if direction == "down": dy = 1
        case "backward":
            if direction == "right": dx = -1
            if direction == "left": dx = 1
            if direction == "up": dy = 1
            if direction == "down": dy = -1
        case "strafe right":
            if direction == "right": dy = 1
            if direction == "left": dy = -1
            if direction == "up": dx = 1
            if direction == "down": dx = -1   
        case "strafe left":
            if direction == "right": dy = -1
            if direction == "left": dy = 1
            if direction == "up": dx = -1
            if direction == "down": dx = 1         

        case other:
            # W tym segmencie obslugiwane sa komendy niezwiazane z ruchem  
            match command:
                case "quit": break
                case "position":
                    print(f"({x},{y})")
                    # for row in range(1, HEIGHT + 1):
                    #     for col in range(1, WIDTH + 1):
                    #         if row == y and col == x:
                    #             print("😀", end="")
                    #         else:print("🌿", end="") 
                    #     print()
                    for row in range(1, HEIGHT + 1):
                        for col in range(1, WIDTH + 1):
                            print(ARROWS[direction] if row == y and col == x else "🌿", end= "\n" if col == WIDTH else "")
        

                case other: print("Nie rozpoznano komendy")
            # Wykonanie komendy zostalo zakonczone wiec wroc na poczatek petli.
            continue

    # W tym segmencie wykonywana jest komenda ruchu. 
    new_x, new_y = x + dx, y + dy
    if new_x < 1 or new_y < 1 or new_x > WIDTH or new_y > HEIGHT:
        print(f"Nie moge wykonac tego ruchu, bo wyszedlbym poza plansze. Pozostaje na pozycji ({x},{y})")
        continue

    x, y = new_x, new_y
    print(f"Przeszedlem na pozycje ({new_x},{new_y})")