

def occ_en_liste(liste):
    if liste == []:
        return 0
    elif liste[0] == 'e':
        return 1 + occ_en_liste(liste[1:])
    else:
        return occ_en_liste(liste[1:])

liste = ['a','i','o','e','u','e']

print(occ_en_liste(liste))

##################

def somme_rec(liste):
    if liste == []:
        return 0
    return liste[0] + somme_rec(liste[1:])
    
liste2 = [1,2,3,4,5,6,7,8,9]
print(somme_rec(liste2))


def inverse_liste_rec(L) -> list :
    if L == []:
        return []
    else:
            return inverse_liste_rec(L[1:]) + [L[0]]

print(inverse_liste_rec(liste2))

def palindrome_rec(mot):
    if mot == '' or len(mot) == 1:
        return True
    if mot[0] != mot[-1]:
        return False
    else:
        return palindrome_rec(mot[1:-1])


print(palindrome_rec("kayak"))