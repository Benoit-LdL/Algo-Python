# -*- coding: utf-8 -*-

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
'''
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
print("Nombre de consonnes: " + str(nombre_consonnes))
print("Liste d'occurences: " + str(liste_occurences))
print("Palindrome: " + str(not_palidrome))
#'''

''' EX 4 : Les listes
############

liste_entiers = [1,2,3,4,5,5,6,7,7,8,9]

#### 1.
total = 0
for i in liste_entiers:
    total += i

## OUT 1.
print("total: " + str(total))


#### 2.
def minimum(liste):
    out = liste[0]
    
    for i in liste:
        if i < out:
            out = minimum(i)
    return out

## 2. MAIN
print("minimum: " + str(minimum(liste_entiers)))

#### 3.
def contains(liste,element):
    in_list = False
    for i in liste:
        if i == element:
            in_list = True
            break
  
    if in_list:
        print("letter '" + str(element) + "' is in the list.")
    else:
        print("letter '" + str(element) + "' is not in the list.")

## 3. MAIN  
contains(liste_entiers,4)

#### 4.
def iterations(liste,element):
    counter = 0
    for i in liste:
        if i == element:
            counter += 1
    return counter

## 4. MAIN
element = 5
print("element '" +str(element) + "' se trouve " + str(iterations(liste_entiers,element)) + "x dans la liste.")

#### 5.

def inverse(liste):
    liste_out = []
    
    for i in range(0,len(liste)):
        liste_out.append(liste[(len(liste)-1)-i])
        
    return liste_out
        
## 5. MAIN
print("Inverse: " + str(inverse(liste_entiers)))    

#### 6.

def prefix(main_list,pref_list):
    is_correct = True
    for i in range(0,len(pref_list)):
        if pref_list[i] != main_list[i]:
            is_correct = False
    
    if is_correct:
        print("prefix phrase is in main phrase.")
    else:
        print("prefix phrase is not in main phrase.")

## 6. MAIN
pref_list = [1,2,3,4]
prefix(liste_entiers,pref_list)

#### 7.

def suffix(main_list,suff_list):
    is_correct = True
    for i in range(0,len(pref_list)):
        if suff_list[i] != main_list[i+ ( len(main_list) - len(suff_list) ) ]:
            is_correct = False
    
    if is_correct:
        print("suffix phrase is in main phrase.")
    else:
        print("suffix phrase is not in main phrase.")

## 7. MAIN

suff_list = [7,7,8,9]
suffix(liste_entiers,suff_list)


### 8.

def compare(liste1,liste2):
    is_different = False
    counter = 0
    while counter < len(liste1):
        if liste1[counter] != liste2[counter]:
            is_different = True
            break
        counter += 1
    
    if is_different:
        print("lists are different")
    else:
        print("Lists are equal")

## 8. MAIN

liste2 = [1,2,3,4,5,5,6,7,7,8,9]
compare(liste_entiers,liste2)

#print("DEBUG| " + str(suff_list[i]) + " -- " + str(main_list[i+ ( len(main_list) - len(suff_list) ) ]))
#print("DEBUG| " + str(i))
'''

''' EX 5: EX 4 en Recursif
############
'''
