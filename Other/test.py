liczba1 = float(input("Podaj liczbe: "))
liczba2 = float(input("Podaj druga liczbe: "))
znak = input("Podaj opoerator (+, -, *, /): ")

if znak == "+":
    print(liczba1 + liczba2)
elif znak == "-":
    print(liczba1 - liczba2)
elif znak == "*":
    print(liczba1 * liczba2)
elif znak == "/":
    print(liczba1 / liczba2)
else:
    print("Nieznany operator")