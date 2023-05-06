WIDTH = 3
HEIGHT = 3
x, y = 1, 1
while True:
    dx, dy = 0, 0
    command = input("> ").lower()
    match command:
        case "quit": break
        case "up": dy = -1
        case "down": dy = 1
        case "left": dx = -1
        case "right": dx = 1
        case "position":
            print(f"({x},{y})")
            continue
        case other:
            print("Nie rozpoznano komendy")
            continue

    new_x, new_y = x + dx, y + dy
    if new_x < 1 or new_y < 1 or new_x > WIDTH or new_y > HEIGHT:
        print(f"Nie moge wykonac tego ruchu, bo wyszedlbym poza plansze. Pozostaje na pozycji ({x},{y})")
        continue

    x, y = new_x, new_y
    print(f"Przeszedlem na pozycje ({x},{y})")