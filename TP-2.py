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

def Approx_pi(p):
    counter = 0
    out = 0

    # for i in range(100):
    #     out += (pow(-1,i)/((2*i)+1))
    #     print(out*4)
    
    while out*4 != p:
        out += (pow(-1,counter)/((2*counter)+1))
        counter+=1
        print("---")
        print(p)
        print(out*4)

    
    
Approx_pi(3.1415)


""" EX 3. FIBONACCI

def fibo(n):
    
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)


#n = 12
#print("fibo de ",str(n)," est: ",fibo(n))
"""