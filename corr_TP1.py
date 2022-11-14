#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 10:29:55 2022

@author: salvat

Quelques correction du TP1
"""


def cpt_occ(mot):
    """ compte les occurences de chaque lettre présente dans la chaîne mot passée en argument
    renvoie une liste de listes de 2 éléments [lettre, nb occurences de la lettre].
    cpt_occ('papa') renvoie la liste [['p',2],['a',2]] """ 
    l_occ=[]                # initialisation de la liste résultat 
    for lettre in mot:      # on parcourt tous les caractères de mot
        pas_trouve = True   # drapeau pour indiquer si on a déjà vu la lettre
        for couple in l_occ:    # recherche de la lettre dans le résultat 
            if lettre == couple[0]: # si la lettre est présente
                couple[1] +=1       # on incrémente son compteur
                pas_trouve = False  # et on indique que la lettre a été trouvée
        if pas_trouve :             # si la lettre n'a pas encore été traitée
            l_occ.append([lettre,1])    # on ajoute le couple [lettre,1]
    return l_occ                    # au final on renvoie le résultat.


def palindrome(mot):
    """ Teste si la chaîne passée en paramètre est un palidromme.
    Renvoie Vrai si c'est le cas; Faux sinon."""
    l = len(mot)//2             # moitié de la taille du mot (divison entière)
    for i in range(l):
        if mot[i] != mot[-(1+i)]:   # on compare la lettre en position i avec celle en position len(mot)-i
            return False            # 2 lettres différentes => mot n'est pas un palindrome
    return True             # Si on arrive à la fin de la boucle, alors le mot est un palindrome

def palindrome_rec(mot):
    """ Version récursive de la vérification du statut de palindrome d'un mot"""
    if mot == '' or len(mot)==1:    # Condition d'arrêt : mot vide ou une seule lettre
        return True
    if mot[0] != mot[-1]:   # condition de récursion : 1ere et dernière lettre sont identiques
        return False        # en cas de différence : on n'a pas un palidrome
    return palindrome_rec(mot[1:-1])    # sinon, on vérifie le reste du mot (sans le 1er et le dernier caractère)

def inverse_liste(L):
    """ construit et renvoie une liste qui est l'inverse de la liste passée en paramètre"""
    return L[::-1]  # on utilise les slice

def inverse_liste_rec(L) -> list :
    """ construit une liste inverse de la liste passée en paramètre. Fonction récursive."""
    if L == [] :    # Condition d'arrêt : liste vide
        return L
    return inverse_liste_rec(L[1:]) +[L[0]] # sinon, on inverse la liste sans le 1er élément, et on ajoute en fin le 1er élément

def somme_liste(L):
    """ Renvoie la somme des nombres constituant la liste L passée en paramètre."""
    total = 0           # variable pour calculer la somme
    for x in L :        # Pour chaque élément de la liste
        total += x      # On ajoute l'élément à total
    return total        # A la fin, total contient la somme recherchée

def somme_liste_rec(L):
    """ Renvoie la somme des éléments de L. Fonction récursive"""
    if L == []:         # Cas d'arrêt : liste vide -> somme nulle
        return 0        
    return L[0] + somme_liste_rec(L[1:])    # Récursion : 1er élément plus somme de la liste sans le 1er élément 

def cpte_occ_liste(L,e):
    """Renvoie le nombre d'occurences de l'élément e dans la liste L. Fonction récursive"""
    if L == [] :    # cas d'arrêt : liste vide
        return 0
    if L[0] == e :  # Si le 1er élément est celui recherché
        return 1 + cpte_occ_liste(L[1:], e)         # le nb d'occurences sera celui de e dans L sans le 1er élément plus 1
    else :          # si le 1er élément, n'est pas celui recherché
        return cpte_occ_liste(L[1:], e) # le nb d'occu. de e dans L est celui de e dans L sans le 1er élément
    
