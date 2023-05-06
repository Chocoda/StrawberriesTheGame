mozliwe_odp = ["a", "b", "c", "d"]
print("Oto quiz na miasta. Bedziesz musial/a powiedziec w jakim kraju jest dane miasto.")
print(f"Bedziesz mial/a do wyboru 4 opcje. Pierwsza to a, druga to b itd.")
print("W jakim kraju jest:")
def abcd_questions(pytanie, opcje, prawidlowa_odp):
    while True:
        print(pytanie)
        print(opcje)
        odp= input().lower()
        if odp in mozliwe_odp:
            if odp == prawidlowa_odp:
                return 1
            else : return 0
pytania = [
    ["Madryt?", ["Wenezuela", "Hiszpania", "Wlochy", "Meksyk"], "b"],
    ["Buenos Aires?", ["Grecja", "Brazylia", "Urugwaj", "Argentyna"], "d"],
    ["Lille?", ["Francja", "Belgia", "Szkocja", "Iralndia"], "a"],
]
score = 0
for lista_z_pytania in pytania:
    score += abcd_questions(*lista_z_pytania)
print(f"MASZ {score}/{len(pytania)}")
print(f"To znaczy masz {score * 100/ len(pytania)}%")
print("Kongratulacje!")