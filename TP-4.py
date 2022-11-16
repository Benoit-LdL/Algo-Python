
"""

print("______________________________________________________________________")
print("Ex 1. min, max et moyenne de liste")
# FUNCTION
def Ex1(liste):
    mini    = liste[0]
    avrg    = 0
    maxi    = liste[0]
    for item in liste:
        if item > maxi:
            maxi = item
        if item < mini:
            mini = item
        avrg += item
    avrg /= len(liste)
    return mini,avrg,maxi
    
# MAIN
liste = [1,2,3,4,5,6,7,8,9,6,8,7,5,2,4,1,2,3,6,8,7,5,4,8,7,9,5,8,7,5,4,6,2,3,1,5,7,5,8,7,6,8,8]
mini,avrg,maxi = Ex1(liste)

print("Minimum: " + str(mini) + "\t| Maximum: " + str(maxi) + "\t| Average: " + str(round(avrg,2)))


print("______________________________________________________________________")
print("Ex 2. milieu de coordonees 2D et 3D")
# FUNCTION
def Milieu_2d(coord1,coord2):  
    return (coord2[0]+coord1[0])/2, (coord2[1]-coord1[1])/2, (coord2[1]-coord1[1])/2
    
def Milieu_3d(coord1,coord2):
    return (coord2[0]-coord1[0])/2, (coord2[1]-coord1[1])/2, (coord2[2]-coord1[2])/2
    
# MAIN
coord_2d_1 = (2,5)
coord_2d_2 = (7,9)

coord_3d_1 = (1,2,3)
coord_3d_2 = (4,5,6)

print("milieu de coord 1 et 2:\t" + str(Milieu_2d(coord_2d_1, coord_2d_2)))
print("milieu de coord 1, 2 et 3:\t" + str(Milieu_3d(coord_3d_1,coord_3d_2)))


print("______________________________________________________________________")
print("Ex 3. Isobarycentre et Barycentre")
# FUNCTION
def Isobarycentre_2d(liste):
    total_x = 0
    total_y = 0
    
    for i in liste:
        total_x += i[0]
        total_y += i[1]
    
    return round(total_x / len(liste),2), round(total_y / len(liste),2)

def Isobarycentre_2d_coef(liste):
    total_coef, total_x, total_y = 0, 0, 0
    
    for x in liste:
        total_coef  += x[0]
        total_x     += x[1][0]
        total_y     += x[1][1]
    
    avrg_coef   = round(total_coef  / len(liste),2)
    avrg_x      = round(total_x     / len(liste),2)
    avrg_y      = round(total_y     / len(liste),2)
    
    
    return  ( avrg_coef , ( avrg_x , avrg_y ) )
        

# MAIN

liste_coord_2d          = [(4,7),(6,7),(4,5),(8,4)]
lsite_coord_coef_2d     = [(1,(4,7)),(2,(6,7)),(3,(4,5)),(1,(8,4))]

print("Isobarycentre de liste:                  " + str(Isobarycentre_2d(liste_coord_2d)))
print("Isobarycentre de liste coord avec coef:  " + str(Isobarycentre_2d_coef(lsite_coord_coef_2d)))

print("______________________________________________________________________")
print("Ex 4. Tester les ensembles")
# MAIN

ensemble1 = {1,5,8,7,4}
ensemble2 = {7,3,5,4,6}
ensemble3 = set(['jean','marie',205,(1,2,3)])

print(ensemble1 <=  ensemble2)
print(ensemble1 <   ensemble2)
print(ensemble1 |   ensemble2)
print(ensemble1 &   ensemble2)
print(ensemble1 -   ensemble2)


print("______________________________________________________________________")
print("Ex 5. ")
# MAIN

dictionnary = { chr(x):0 for x in range(65,91)  }

f = open("TP-4_ex-5.txt",'r')
#f = open("long_text.txt",'r')

for line in f:
    for letter in line:
        if letter.upper() in dictionnary:
            dictionnary[letter.upper()] += 1

for i in range(65,91):
    if  dictionnary[chr(i)] != 0 :
        print(chr(i) + ":" + str(dictionnary[chr(i)]))



"""

print("______________________________________________________________________")
print("Ex 6. ")
# FUNCTION

def Partie1(nom_fichier):
    f = open(nom_fichier,'r',encoding='utf8')
    dico = {}
    for lineID, line in enumerate(f):
        if lineID > 0 :
            if line.split(';')[1] not in dico:
                splitLine = line.split(';')
                dico[ splitLine[1] ] = [ ( splitLine[0] , splitLine[2] , splitLine[3][:-1] ) ]
            
            else:
                splitLine = line.split(';')
                dico[ splitLine[1] ] += [( splitLine[0] , splitLine[2] , splitLine[3][:-1] )]

    return dico   
   
def Partie2(dico_nom,nom):
    print("Partie 2: affiche pour un nom chaque annéé la frequence du nom")
    if dico_nom.get(nom) != None:
        print(len(dico_nom.get(nom)))
        for x in range(len(dico_nom.get(nom))):
            print(dico_nom.get(nom)[x][1] + " : " + dico_nom.get(nom)[x][2])
        
def Partie3(dico_nom,nom,annee):
    print("Partie 3: donne les frequence d'un nom et une anéé specifié")
    if dico_nom.get(nom) != None:
        for x in range(len(dico_nom.get(nom))):
            if dico_nom.get(nom)[x][1] == annee:
                print(dico_nom.get(nom)[x][1] + " : " + dico_nom.get(nom)[x][2])
    
def Partie4(nom_fichier):
    print("Partie 4: dict dans dict dans dict")
    f = open(nom_fichier,'r',encoding='utf8')
    dico = {}
    for lineID, line in enumerate(f):
        if lineID > 0:
            splitLine = line.split(';')

            if splitLine[1] not in dico:
                dico[ splitLine[1] ] = { int(splitLine[0]) : { splitLine[2] : splitLine[3][:-1] } }

            else:
                if splitLine[0] not in dico[splitLine[1]]:
                    #print("name exist but sex doesn't")
                    dico[ splitLine[1] ] = { int(splitLine[0]) : { splitLine[2] : splitLine[3][:-1] } }

                else:
                    dico[ splitLine[1] ][splitLine[0]][splitLine[2]] = splitLine[3][:-1]

    return dico 

def Partie5(dico,sex_input):
    f = open("TP-4_ex6-5.txt",'w')
    
    for key in dico.keys():
        print(key)
        for sex in dico[key].keys():
            print(sex)
            if sex == sex_input:
                f.write(str( dico[key].get(sex_input) ))
    f.close()

# MAIN

nom     = "CAMILLE"
annee   = "1999"
fichier = "nat2021.csv"

#dico    = Partie1(fichier)

#Partie2(dico,nom)

#Partie3(dico, nom, annee)

dico_new = Partie4(fichier)
print(dico_new)
liste_nom = Partie5(dico_new,1)


#print(dico_new)


