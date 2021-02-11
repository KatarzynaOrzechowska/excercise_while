# -*- coding: utf-8 -*-

#Stwórz prostą grę zgadywankę. Komputer losuje wartość z przedziału od 1-30. 
#Poproś użytkownika o zgadnięcie liczby. Program pyta użytkownika 
#o podanie liczby tak długo, dopóki gracz nie zgadnie.
print('Maszyna losujaca wylosowała liczbę z zakresu 1-30. Twoim zadaniem jest ja odgadnac')
import random
wartosc = random.randrange(1,31)
i = True
while i == True:
    liczba = int(input('Twoja liczba to: '))
    if liczba > wartosc:
        print('Liczba jest za duża')
        print('Niestety, nie zgadles, probuj dalej.')
        i = True
    elif liczba < wartosc:
        print('Liczba jest za mała')
        print('Niestety, nie zgadles, probuj dalej.')
        i = True
    else:
        liczba == wartosc
        print(f'Gratulacje! To liczba {wartosc}.') 
        i = False