def fibb_iter(n):
    if n== 0 : return 0
    if n== 1: return 1
    value1 = 0
    value2 = 1
    for x in range(n-1):
        newvbalue = value2
        value2 += value1
        value1 = newvbalue
    return value2
print([fibb_iter(x) for x in range (10)])

mozliwe_odp = ["a", "b", "c", "d"]
def abcd_questions(pytanie, opcje, prawidlowa_odp):
    while True:
        print(pytanie)
        print(opcje)
        odp = input().lower
        if odp in mozliwe_odp:
            if odp == prawidlowa_odp.lower():
                return 1
            else: return 0
pytania=[
    ["Wloch?", ["Istambu", "Ateny", "Rzym", "Brugia"], "c"],
    ["Stanow?", ["Boston", "Washington", "New York", "California"], "b"],
    ["Libanu?", ["Beyrouth", "Abudabi", "Ankara", "Tibilisi"], "a"]
]
score = 0
for x in pytania:
    score+= abcd_questions(*x)
print(f"{score} / {len(pytania)}")
print(f"Prawidlowy prozent{score*100 / len(pytania)} %")
