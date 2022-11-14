import math

""" EX 1. E

def Factoriel_iter(valeur):
    total = 1
    
    for i in range(1,valeur+1):
        total*=i

    return total

def Approx_e_iter(iterations):
    e_float = 1

    for i in range(1,iterations):
        e_float += 1/Factoriel_iter(i)
        #print("temp e",str(e_float))
    
    return e_float

def Iterations_to_e(p):
    
    counter = 1
    delta = Approx_e_iter(counter+1) - Approx_e_iter((counter))
    print(str(Approx_e_iter(counter+1)), " | ", str(delta))
    counter += 1
    

    while (p < delta):
        delta = Approx_e_iter(counter+1) - Approx_e_iter((counter))
        print(str(Approx_e_iter(counter+1)), " | ", str(delta))
        counter += 1

    return Approx_e_iter(counter),delta,counter-1

#MAIN
value = 10
print("Factoriel: ",str(Factoriel_iter(value)))
    
print("approx: ",str(Approx_e_iter(value)))

print("----",Iterations_to_e(0.005))

"""


""" EX 2. PI
"""





""" EX 3. FIBONACCI

def fibo(n):
    
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)


#n = 12
#print("fibo de ",str(n)," est: ",fibo(n))

"""



""" EX 4. nombre d'or

def OR(n):
    return fibo(n+1)/fibo(n)

print(OR(25))
"""



""" EX 5. Eratosthène
"""

def Eratos(val):
    premiers = []
    for i in range(val):
        print(i+1)
        if
        
        

Eratos(120)