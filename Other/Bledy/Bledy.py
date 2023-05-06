"""
Print noie wywoluje funkci.
Jezeli mam w funkcji print to moge wywolac fukcje bez printa.
W przeciwnym wypadku daje else.
Zeby string stal sie intigerem daj INT na poczatku
extend robi konkatynacje list."""
# i= 1
# while i<= 5:
#     print( "*"*i)
#     i+=1
# print("Done")
# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:
#     guess = int(input("guess: "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won!")
#         break
# else: print("Sorry, you failed.")


# import random
# secret_number = random.randint(1, 100)
# print("The result is between 0 and 100")
# guess_number = 1
# guess = int(input("Guess: "))
# while guess != secret_number:
#     if guess < secret_number: print("Upper!")
#     if guess > secret_number: print("lower!")
#     guess = int(input("Guess: "))
#     guess_number += 1
# print(f"Guessed it! The result was {guess} and you found in {guess_number} attempts.")


# times = 5
# i = 0
# while i < times:
#     print(i)
#     i += 1

# print()

# i = times - 1
# while i >= 0:
#     print(i)
#     i -= 1


# to_guess = int(input("Pick a number from 0 to 100: "))
# number_guess = 50
# upper_number = 100
# lower_number = 0
# print(number_guess)

# while number_guess != to_guess :
#     print(number_guess)      
#     if number_guess < to_guess:
#         lower_number = number_guess
#     else:
#         upper_number = number_guess
#     number_guess = (lower_number+upper_number)//2
# print("Found")


# liczba_zjedzonych_psow = 1000
# def wyswietl_liczba_zjedzonych_sow():
#     print(500)

# print(liczba_zjedzonych_psow)

import random
NumberOfTimes = 0
poprawne = 0
bledne = 0
while True :
    number1 = random.randint(0, 12)
    number2 = random.randint(0, 12)
    losowany_znak = random.randint(1, 3)
    # dodawanie = 1
    # odejmowanie = 2
    # mnozenie = 3
    if losowany_znak == 1:
        znak = "+"
        answer = str(number1 + number2)
        NumberOfTimes += 1
    if losowany_znak == 2:
        znak = "-"
        answer = str(number1 - number2)
        NumberOfTimes += 1
    if losowany_znak == 3:
        znak = "*"
        answer = str(number1 * number2)
        NumberOfTimes += 1
    answer_given = str(input(f"{number1} {znak} {number2} = "))
    if answer_given == "q":
        break
    if answer_given == answer:
        print("Dobrze.")
        poprawne += 1
    else:
        print(f"Masz blad. {number1} {znak} {number2} = {answer}")
        bledne += 1
print(f"""Udzieliles/as odpowiedzi na {NumberOfTimes - 1} odpowiedzi. Poprawne odpowiedzi: {poprawne} Bledne odpowiedzi: {bledne}. 
Skutecznosc: {(poprawne  / (NumberOfTimes-1)) * 100 } %""")