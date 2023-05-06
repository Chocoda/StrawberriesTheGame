mozliwe_odpowiedzi = ["a", "b", "c", "d"]

"""
wejscie:
 - pytanie: tresc pytania - str
 - opcje: mozliwe odpowiedzi - list
 - praw_odp: literka prawidlowej odpowiedzi - str
wyjscie:
    liczba punktow za pytanie (0 albo 1) - int
"""
def abcd_question(pytanie, opcje, praw_odp):
    while True:
        # Wyswietl tresc pytania
        print(pytanie)
        # Wyswietl mozliwe opcje odpowiedzi
        for i, v in enumerate(opcje):
            print(f"\t{mozliwe_odpowiedzi[i]}. {v}") # \t w stringu to znak tabulacji
        # Odczytaj odpowiedz uzytkownika z klawiatury
        odp = input().lower()

        # Sptrawdz czy odpowiedz jest literka a, b, c lub d
        if odp in mozliwe_odpowiedzi:
            # Skoro wiem, ze odpowiedz ma poprawny format to sprawdz czy to byla dobra odpowiedz
            if odp == praw_odp.lower():
                # Jezeli odpowiedz byla prawidlowa to zwroc 1 pkt
                return 1
            else:
                # Jezeli odpowiedz byla nieprawidlowa to zwroc 0 pkt
                return 0

        # Jezeli odpowiedz nie jest literka a, b, c, d to petla rozpocznie nowa iteracje, gdzie znowu zada pytanie


""""
Lista pytan:
    Kazdy element listy jest lista, ktora zawiera na poszczegolnych elementach:
        0: tresc pytania
        1: mozliwe opcje opdowiedzi
        2: literka prawidlowej odpowiedzi
    ZAUWAZ ZE: Powyzse elementy sa takie same jak argumenty, ktore nalezy przekazac do funkcji abcd_question

"""
pytania = [
    ["Stolica Polski?", ["Krakow", "Warszawa", "Poznan", "Gdansk"], "b"],
    ["Stolica Francji?", ["Paryz", "Gdynia", "Poznan", "Gdansk"], "a"],
    ["Stolica Hiszpanii?", ["Krakow", "Warszawa", "Poznan", "Madryt"], "d"],
    ["Stolica Wloch?", ["Krakow", "Warszawa", "Rzym", "Gdansk"], "c"]
]

# Inicjalizuje zmienna z wyniukiem na 0
score = 0

# Iteruje przez kazde pytanie z listy pytan
for lista_z_pytaniem in pytania:
    # Przekazuje kazdy element z listy reprezentujacej pojedyncze pytanie jako kolejny argument do funkcji abcd_question
    # lista_z_pytaniem[0] - tresc pytania
    # lista_z_pytaniem[1] - lista opcjiiodpowiedzi
    # lista_z_pytaniem[2] - literka prawidlowej odpowiedzi
    # score += abcd_question(lista_z_pytaniem[0], lista_z_pytaniem[1], lista_z_pytaniem[2])
    score += abcd_question(*lista_z_pytaniem) # Skrocony zapis powyzszj linijki

# Wyswietl liczbe punktow
print(f"Prawidlowe odpowiedzi: {score}/{len(pytania)}")
# Wyswietlam wynik procentowy
print(f"Procent prawidlowych odpowiedzi: {100*score/len(pytania)}%")