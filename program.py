mozliwe_odpowiedzi = ["a", "b", "c", "d"]

def abcd_question(pytanie, opcje, praw_odp):
    while True:
        print(pytanie)
        for i, v in enumerate(opcje):
            print(f"\t{mozliwe_odpowiedzi[i]}. {v}")
        odp = input().lower()
        if odp in mozliwe_odpowiedzi:
            if odp == praw_odp.lower():
                return 1
            else:
                return 0

     
pytania = [
    ["Stolica Polski?", ["Krakow", "Warszawa", "Poznan", "Gdansk"], "b"],
    ["Stolica Francji?", ["Paryz", "Gdynia", "Poznan", "Gdansk"], "a"],
    ["Stolica Hiszpanii?", ["Krakow", "Warszawa", "Poznan", "Madryt"], "d"],
    ["Stolica Wloch?", ["Krakow", "Warszawa", "Rzym", "Gdansk"], "c"]
]

score = 0

for lista_z_pytaniem in pytania:
    score += abcd_question(*lista_z_pytaniem) 

print(f"Prawidlowe odpowiedzi: {score}/{len(pytania)}")
print(f"Procent prawidlowych odpowiedzi: {100*score/len(pytania)}%")

prawidlowe_odp = ["a", "b", "c", "d"]
print(f"TEST: za kazdym razem masz do wybory {prawidlowe_odp} pierwsza odp to a , druga b, itd Teraz powiedz mi jaka jest stolica: ")
def questions(pytania, opcje, prawidlowa_odp):
    while True:
        print(pytania)
        print(opcje)
        odp= input().lower()
        if odp in mozliwe_odpowiedzi:
            if odp == prawidlowa_odp.lower():
                return 1
            else: return 0
pytania=[
    ["Wloch?", ["Rzym", "Madryt", "Florencja", "Lisbona"], "a"],
    ["Francji?", ["Wenecja", "Lille", "Lisbona", "Paryz"], "d"],
    ["Wloch?", ["Rzym", "Madryt", "Florencja", "Lisbona"], "a"],
    ["Wloch?", ["Rzym", "Madryt", "Florencja", "Lisbona"], "a"],
    ["Wloch?", ["Rzym", "Madryt", "Florencja", "Lisbona"], "a"],
]
score = 0
for listapyt in pytania:
    score += questions(*listapyt)
print(f"Prawidlowe odp: {score}/{len(pytania)}")
print(f"Prozent {100 * score / len(pytania)} % ")