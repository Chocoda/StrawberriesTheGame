print("TO JEST TEST NA DATY")
print("KIEDY bylo:")
mozliwe_odp = ["a", "b", "c", "d"]
def questions (pytanie, opcje, prawodp):
    while True:
        print(pytanie)
        print(opcje)
        print(mozliwe_odp)
        odp = input().lower()

        if odp in mozliwe_odp:
            if odp == prawodp:
                return 1
            else : 
                return 0
question  = [
    ["Poczatek bitwy pod Waterloo?", ["1815", "1872", "1899", "1799"], "a"],
    ["Poczatek drugiej wojny swiatowej?", ["2017", "1914", "1939", "1895"], "c"],
    ["Wojna na Ukrainie", ["1203", "2013", "2023", "2022"], "d"],
    ["Narodziny Jezusa?", ["2019", "0", "100", "-1"], "b"],
    ["Smierc Krolowej Elzbiety II?", ["1275", "1899", "2022", "2021"], "c"],
    ["Poczatek Rewolucji Francuzkiej?", ["1789", "1723", "1748", "1255"], "a"],
    ["Odrycie Ameryki przez Krzysztofa Kolumba?", ["1214", "1492", "1652", "1388"], "b"],
    ["Noc św. Bartłomieja?", ["1721", "1479", "1572", "2011"], "c"],
    ["Rewolucji Rosyjskej?", ["1821", "1892", "1954", "1917"], "d"],
    ["Bomba Hiroshimy?", ["1945", "1280", "1963", "1984"], "a"]
]  
score = 0
for x in question:
    score += questions(*x)
print(f"score = {score}/{len(question)}")

