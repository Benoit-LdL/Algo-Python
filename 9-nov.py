""" Chapitre 1 : Compréhension  Exercice 1


entiers     = [1,2,3,4,5,6,7,8,9]
chars       = ['a','z','e','r','t','y']
mix         = ['abc','12','5','toto','3']   
# 1. FUNCTION
def carre(l):
    return [x*x for x in l]

# 1. MAIN
print("Multiplication des nombres: " + str(carre(entiers)))



# 2. FUNCTION
def demi_pair(l):
    return [x/2 for x in l if x % 2 == 0 and x != 0]

# 2. MAIN
print("Division des nombres pairs: " + str(demi_pair(entiers)))



# 3. FUNCTION
def carre_str1(c):
    return [ord(x)*ord(x) for x in c]

def carre_str2(m):
    return [int(x)*int(x) for x in m if x.isdigit() == True ]
    

# 3. MAIN
print("Carré des chars en int: " + str(carre_str1(chars)))
print("Carré des ints dans liste de string: " + str(carre_str2(mix)))

"""
###############################################################################
""" Chapitre 2 : Fichiers Exercice 2

# 2 FUNCTION

def ex2_1_4(l):
    counter = 1
    
    total_words = 0
    total_chars = 0
    
    for line in this_file:
        
        # 2.3
        word_counter = 1
        if len(line) > 1:
            for i in range(len(line)-1):
                #print(str(line[i]))
                if (line[i] != " " and line[i+1] == " "):
                    word_counter += 1
        else:
            word_counter = 0
            
        # 2.1 & 2.2 (+ visualisation 2.3)
        print("Line number " + str(counter) + " : " + " | # chars : " + str(len(line)-1) + " |  words : " + str(word_counter) + " ::" + line)

        total_words += word_counter
        total_chars += len(line)-1
                
        counter +=1

    print("# lines : " + str(counter))
    print("# Words : " + str(total_words))
    print("# chars : " + str(total_chars))
            
            
# 1. MAIN
this_file   = open("9-nov.py",'r')

# 2.1, 2.2, 2.3, 2.4
# ex2_1_4(this_file)

# 2.5
#for line in this_file:
#    if line[0] == '#':
#        print(line)


# 2.6
line_counter = 0
fichier_pair    = open("9-nov_pairs.py",'w')
fichier_impair  = open("9-nov_impairs.py",'w')

for line in this_file:
    line_counter += 1
    if line_counter % 2 == 0:
        fichier_pair.write(line)
    else:
        fichier_impair.write(line)


fichier_pair.close()
fichier_impair.close()

this_file.close()

print("Done!")

"""
###############################################################################
"""Exercice 3
"""
# 3. FUNCTION

def Check_file(name,charList):
    f = open(name,'r')
    charList_counter = 0
    for line in f:
        for i in range(len(line)):
            charlist_found = False
            
            if line[i] == charList[0]:
                for j in range(len(charList)):
                    if line[i+j] == charList[j]:
                        charlist_found = True
                    else:
                        charlist_found = False
            if charlist_found:
                charList_counter += 1
    f.close()
    print("Nombre d'apparitions de la chaine : " + str(charList_counter))   
    
# 3. MAIN

Check_file("testfile.txt", "appel")