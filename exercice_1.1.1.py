import random

print("Devinez un nombre entre 1 et 100")
n = int(random.uniform(0,100))
#print(n)

while 0 == 0 :
    print("Entrez un nombre : ")
    b = input()
    a=int(b)
    if a == n :
        print("Exact !")
        break
    else :
        if a < n :
            if n - a <= 5 :
                print("C'est un tout petit peu plus")
            elif n - a > 5 and n - a <=10 :
                print("C'est beaucoup plus")
            else :
                print("C'est tres plus")
        else :    
            if a - n <= 5 :
                print("C'est un tout petit peu moins")
            elif a - n > 5 and a - n <=10 :
                print("C'est beaucoup moins")
            else :
                print("C'est tres moins")
            