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
    
    return round(total_x / len(liste),4), round(total_y / len(liste),4)
    
# MAIN

liste_coord_2d          = [(4,7),(6,7),(4,5),(8,4)]
lsite_coord_coef_2d     = [(1,(4,7)),(1,(6,7)),(1,(4,5)),(1,(8,4))]

print("Isobarycentre de liste: " + str(Isobarycentre_2d(liste_coord_2d)))

print("______________________________________________________________________")
print("Ex 4. ")
# FUNCTION

# MAIN

print("______________________________________________________________________")
print("Ex 5. ")
# FUNCTION

# MAIN

print("______________________________________________________________________")
print("Ex 6. ")
# FUNCTION

# MAIN