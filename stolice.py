# Zadajezsz 10 pytan o stolice, gdzie zawsze mozliwe sa 4 odpoziedwi
# np
# Jaka jest stolica Polski? a. Paryz b. Krakow c. Warszawa d. Gdansk
# Prawidlowe odpowiedzi to a, b, c, d:
# Na koniec podajesz liczbe punktow na 10 oraz procent prawidlowo popdanych odpowiedzi

print("""TEST NA STOLICE PANSTW EUROPEJSKICH
prawidlowe odpowiedzi (a, b, c, d)
Jaka jest stolica:""")
score = 0
dostepnosc = ["a", "b", "c", "d"]
while True :
    odp = input("Niemiec a. Zurych / b. Wilno / c. Berlin / d. Hamburg " ).lower()
    if odp in dostepnosc:
        if odp == "c":
            score += 1
        break

# while True:
#     pytanie2 = input("Norwegi a. Beyriouth / b. Oslo / c. Odessa / d. Boulogne " ).lower()
#     if pytanie2 in dostepnosc:
#         if pytanie2 == "c":
#             score += 1
#             break
#     else:
#         break
# while True:
#     pytanie3 = input("Turcji a. Instambul / b. Rio de Janeiro / c. Sevilla / d. Ankara " ).lower()
#     if pytanie3 in dostepnosc:
#         if pytanie3 == "c":
#             score += 1
#             break
#     else:
#         break
# while True:
#     pytanie4 = input("Albanii a. Uan Bator / b. Lille / c. Tirana / d. Talin " ).lower()
#     if pytanie4 in dostepnosc:
#         if pytanie4 == "c":
#             score += 1
#             break
#     else:
#         break
#     pytanie5 = input("Grecji a. Atheny / b. Tibilisi / c. Bukareszt / d. Brugia " ).lower()
#     if pytanie5 in dostepnosc:
#         if pytanie5 == "c":
#             score += 1
#             break
#     else:
#         break
#     pytanie6 = input("Hiszpani a. Santa Cruz / b. Madryd / c. Sewilla / d. Milano ").lower()
#     if pytanie6 in dostepnosc:
#         if pytanie6 == "c":
#             score += 1
#             break
#     else:
#         break
#     pytanie7 = input("Austri a. Berno / b. Gdansk / c. Ryga / d. Wieden ").lower()
#     if pytanie7 in dostepnosc:
#         if pytanie7 == "c":
#             score += 1
#             break
#     else:
#         break
#     pytanie8 = input("Wloch a. Rzym / b. San Torini / c. Krakow / d. Sycylia ").lower()
#     if pytanie8 in dostepnosc:
#         if pytanie8 == "c":
#             score += 1
#             break
#     else:
#         break
#     pytanie9 = input("Kanady a. Wilno / b. Kopenhaga / c. Ottawa / d. Wenecja ").lower()
#     if pytanie9 in dostepnosc:
#         if pytanie9 == "c":
#             score += 1
#             break
#     else:
#         break
#     pytanie10 = input("Argentyna a. Paryz / b. Antananariwo  / c. Monte Wideo / d. Buenos Aires ").lower()
#     if pytanie10 in dostepnosc:
#         if pytanie10 == "c":
#             score += 1
#             break
#     else:
#         break

print (f"Masz {score}/10 punktow")
procent = score* 10
print (f" Udalo ci sie {procent}%!")


"""
while True:
    print("Czy lubisz kapuste?")
    response = input(f"Dostepne odpowiedzi : {positive} lub tez {negative}: ")
    if response.lower() in positive:
        print("Ok. Dostaniesz bigos!")
        break
    elif response.lower() in negative:
        print("Nod dobra, nie dostaniesz bigosu!")
        break

"""















#print("""TEST NA STOLICE PANSTW EUROPEJSKICH
#prawidlowe odpowiedzi (a, b, c, d)
#Jaka jest stolica:""")
"""
dostepnosc = ["a", "b", "c", "d"]
score = 0
while True :
    response = input("Niemiec a. Zurych / b. Wilno / c. Berlin / d. Hamburg " ).lower()
    if response in dostepnosc:
        if response == "c":
            score += 1
    else :
        print (response)
    response = input("Norwegi a. Beyriouth / b. Oslo / c. Odessa / d. Boulogne " ).lower()
    if response in dostepnosc:
        if response == "b":
            score += 1
    else :
        print (response)
    response = input("Turcji a. Instambul / b. Rio de Janeiro / c. Sevilla / d. Ankara " ).lower()
    if response in dostepnosc:
        if response == "d":
            score += 1
    else :
        print (response)
    response= input("Albanii a. Uan Bator / b. Lille / c. Tirana / d. Talin " ).lower()
    if response in dostepnosc:
        if response == "c":
         score += 1
    else :
        print (response)
    response = input("Grecji a. Atheny / b. Tibilisi / c. Bukareszt / d. Brugia " ).lower()
    if response in dostepnosc:
        if response == "a":
            score += 1
    else :
        print (response)
    response = input("Hiszpani a. Santa Cruz / b. Madryd / c. Sewilla / d. Milano ").lower()
    if response in dostepnosc:
        if response == "b":
            score += 1
    else :
        print (response)
    response = input("Austri a. Berno / b. Gdansk / c. Ryga / d. Wieden ").lower()
    if response in dostepnosc:
        if response == "d":
            score += 1
    else :
        print (response)
    response = input("Wloch a. Rzym / b. San Torini / c. Krakow / d. Sycylia ").lower()
    if response in dostepnosc:
        if response == "a":
            score += 1
    response = input("Kanady a. Wilno / b. Kopenhaga / c. Ottawa / d. Wenecja ").lower()
    if response in dostepnosc:
        if response == "c":
            score += 1
    else :
        print (response)
    response = input("Argentyna a. Paryz / b. Antananariwo  / c. Monte Wideo / d. Buenos Aires ").lower()
    if response in dostepnosc:
        if response == "c":
            score += 1
    else :
        print (response)
    break
print (f"Masz {score}/10 punktow")
procent = score* 10
print (f" Udalo ci sie {procent}%!")

"""
"""
while True:
    print("Czy lubisz kapuste?")
    response = input(f"Dostepne odpowiedzi : {positive} lub tez {negative}: ")
    if response.lower() in positive:
        print("Ok. Dostaniesz bigos!")
        break
    elif response.lower() in negative:
        print("Nod dobra, nie dostaniesz bigosu!")
        break
"""
"""
while True :
    response = input("Niemiec a. Zurych / b. Wilno / c. Berlin / d. Hamburg " ).lower()
    if response == "c":
            score += 1
    response = input("Norwegi a. Beyriouth / b. Oslo / c. Odessa / d. Boulogne " ).lower()
    if response == "b":
        
        score += 1
    response = input("Turcji a. Instambul / b. Rio de Janeiro / c. Sevilla / d. Ankara " ).lower()
    if response == "d":
        score += 1
    response= input("Albanii a. Uan Bator / b. Lille / c. Tirana / d. Talin " ).lower()
    if response == "c":
        score += 1
    response = input("Grecji a. Atheny / b. Tibilisi / c. Bukareszt / d. Brugia " ).lower()
    if response == "a":
        score += 1
    response = input("Hiszpani a. Santa Cruz / b. Madryd / c. Sewilla / d. Milano ").lower()
    if response == "b":
         score += 1
    response = input("Austri a. Berno / b. Gdansk / c. Ryga / d. Wieden ").lower()
    if response == "d":
        score += 1
    response = input("Wloch a. Rzym / b. San Torini / c. Krakow / d. Sycylia ").lower()
    if response == "a":
        score += 1
    response = input("Kanady a. Wilno / b. Kopenhaga / c. Ottawa / d. Wenecja ").lower()
    if response == "c":
        score += 1
    response = input("Argentyna a. Paryz / b. Antananariwo  / c. Monte Wideo / d. Buenos Aires ").lower()
    if response == "c":
        score += 1
    break
print (f"Masz {score}/10 punktow")
procent = score* 10
print (f" Udalo ci sie {procent}%!")
"""

