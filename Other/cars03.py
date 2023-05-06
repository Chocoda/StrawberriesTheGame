# 😀
# 🌿

# print("😀", end="")
# print("ala zjadla\nkota")

WIDTH = 5
HEIGHT = 3
MOVEMENTS = {"up":(0, -1), "down":(0, 1), "left":(-1, 0), "right":(1, 0) }

x, y = 1, 1

    
while True:
    command = input("> ").strip().lower()

    if command not in MOVEMENTS:
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
                        print("😀" if row == y and col == x else "🌿", end= "\n" if col == WIDTH else "")
     

            case other: print("Nie rozpoznano komendy")
        # Wykonanie komendy zostalo zakonczone wiec wroc na poczatek petli.
        continue


    # W tym segmencie wykonywana jest komenda ruchu. 
    dx, dy = MOVEMENTS[command]
    new_x, new_y = x + dx, y + dy
    if new_x < 1 or new_y < 1 or new_x > WIDTH or new_y > HEIGHT:
        print(f"Nie moge wykonac tego ruchu, bo wyszedlbym poza plansze. Pozostaje na pozycji ({x},{y})")


    x, y = new_x, new_y
    print(f"Przeszedlem na pozycje ({x},{y})")