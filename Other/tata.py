import random
liczba_pytan = 0
liczba_prawidlowych = 0

while True:
    liczba_a = random.randint(0, 12)
    liczba_b = random.randint(0, 12)

    indeks_dzialania = random.randint(0, 2)

    match indeks_dzialania:
        case 0:
            wynik_dzialania = liczba_a + liczba_b
        case 1:
            wynik_dzialania = liczba_a - liczba_b
        case 2:
            wynik_dzialania = liczba_a * liczba_b
        case other:
            print("haha")

    znak_dzialania = ("+", "-", "*")[indeks_dzialania]

    tekst_dzialania = f"{liczba_a} {znak_dzialania} {liczba_b} = "

    odpowiedz_uzytkownika = input(tekst_dzialania)
    if odpowiedz_uzytkownika == "q":
        break
    liczba_pytan += 1
    odpowiedz_uzytkownika = int(odpowiedz_uzytkownika)

    if odpowiedz_uzytkownika == wynik_dzialania:
        liczba_prawidlowych += 1
        print("Dobra odpowiedz!")
    else:
        print(f"Zla odpowiedz. {tekst_dzialania}{wynik_dzialania}")

print(f"Odpowiedziales na {liczba_pytan} pytan.")
print(f"Liczba odpowiedzi prawidlowych: {liczba_prawidlowych}.")
print(f"Liczba odpowiedzi blednych: {liczba_pytan - liczba_prawidlowych}.")
print(f"Skutecznosc: {100*liczba_prawidlowych/liczba_pytan}%.")