# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

''' EX 1 : Prise en main
############
total = 0
number = int(input("donnez un chiffre:"))

while number != 0:
    total += number
    number = int(input("donnez un autre chiffre [" + str(total) + "] (0 pour arreter) : "))

print("le total est " + str(total))
'''

''' EX 2  : Entrées_sorties
############

from random import randint
x = randint(0,100)


value_in = int(input("devinez un chiffre entre 0 et 100:"))

while value_in != x:
    if value_in > x:
        value_in = int(input("la valeur recherchée est plus petite:"))
    elif value_in < x:
        value_in = int(input("la valeur recherchée est plus grande:"))

print("Bravo, la valeur recherchée est bien " + str(x))
'''

''' EX 3 : Les chaines
############

voyelles = ['a','e','i','o','u','y']
nombre_voyelles, nombre_consonnes = 0,0
out = ""
counter = 0

x = []
x = input("donnez un chaine de char:")

liste_occurences = []
premier_element = [x[0],1]
liste_occurences.append(premier_element)


for i in range(0,len(x)):

#### 1.
    if x[i] == 'l':
        print("trouvé 'l' sur la place " + str(i))
        counter += 1

#### 3.      
    if x[i] == 'a':
        out += 'o'
    else:
        out += x[i]

#### 4.
    for j in voyelles:
        if x[i] == j:
            nombre_voyelles += 1

#### 2.
if counter == 0:
    print("Il n'y a pas de 'l'")
    
nombre_consonnes = len(x)-nombre_voyelles

#### 4.
for k in range(1,len(x)):
    in_list = False
    
    for l in range(0,len(liste_occurences)):     
        if liste_occurences[l][0] == x[k]:
            liste_occurences[l][1] += 1
            in_list = True
    
    if in_list == False:
        nouvel_element = [x[k],1]
        liste_occurences.append(nouvel_element)

### 5.
length = len(x)
half = length // 2

not_palidrome = True
for i in range(0,half):
    if (x[i] != x[(length-1)-i]):
        not_palidrome = False

# OUTPUT #


print("Nouveau mot: " + out)
print("Nombre de voyelles: " + str(nombre_voyelles))
print("Nombre de voyelles: " + str(nombre_consonnes))
print("Liste d'occurences: " + str(liste_occurences))
print("Palindrome: " + str(not_palidrome))
'''

''' EX 4 : Les listes
############
'''
