# łamanie haseł 4 literowych tylko małe litery podaje użytkownik,
# sprawdz czy ma 4 litery to co podal, a nastepnie uzyj biblioteki
# random i losuj 4 literowe ciagi znakow i sprawdzaj
# czy jest takie samo jak haslo podane przez uzytkownika jesli tak zrob break na while

import random

password = input('Podaj hasło 4 litery, tylko male: ').lower()

if len(password) != 4:
    print('Hasło niewłaściwe!')
    exit()

letters = 'abcdefghijklmnopqrstuvwxyz'
try_password = '' #tu bedziemy wpisywac losowane litery

while True:
    for i in range(4):
        letter = random.choice(letters)
        try_password += letter
    if try_password == password:
        print('Twoje hasło zostało złamane!', try_password)
        break #złamanie while True
    else:
        try_password = '' #czyszcze do losowania

