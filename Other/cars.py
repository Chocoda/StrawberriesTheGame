# course = "Python for Beginners"
# print(len(course))
# is_car_started = False
# while True:
#     command = input().lower()
#     match command:
#         case "help": print("Type 'start' to start the car, 'stop' to stop it and 'quit' to end the game."  )
#         case "start": 
#             if is_car_started:
#                 print("car already started")
#             else: 
#                 print("car started")
#                 is_car_started = True
#         case "stop": 
#             if not is_car_started:
#                 print("car already stopped")
#             else: 
#                 print("car stopped")
#                 is_car_started = False
#         case "quit":
#             print("End of game")
#             break
#         case other:
#             print("I dont understand. ")
position = [1,1]
while True:
    command = input().lower()
    match command:
        case "postion": 
            print(f"Jestes na pozycji {position}")
        case "right": 
            if position[0] == 3:
                print(f"Nie ma miejsca zeby wykonac ten ruch. Pozostajesz na pozycji {position}")
            else: 
                position[0] += 1
                print(f"Przesowasz sie w prawo, jestes na pozycji {position}. ")
        case "left": 
            if position[0] == 1:
                print(f"Nie ma miejsca zeby wykonac ten ruch. Pozostajesz na pozycji {position}")
            else: 
                position[0] -= 1
                print(f"Przesowasz sie w lewo, jestes na pozycji {position}. ")
        case "up": 
            if position[1] >1  :
                position[1] -= 1
                print(f"Przesowasz sie w gore, jestes na pozycji {position}. ")
            else: 
                print(f"Nie ma miejsca zeby wykonac ten ruch. Pozostajesz na pozycji {position}")
        case "down": 
            if position[1] <3 :
                position[1] += 1
                print(f"Przesowasz sie w dol, jestes na pozycji {position}. ")
            else: 
                print(f"Nie ma miejsca zeby wykonac ten ruch. Pozostajesz na pozycji {position}")
        case "position":
            print(f"Your position is {position}")
        case "quit":
            print("End of game")
            break
        case other:
            print("I dont understand. ")