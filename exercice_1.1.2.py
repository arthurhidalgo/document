from math import floor
while 0 == 0 :
    print("Entrez un nombre entre 0 et 100 : ")
    b = input()
    a=int(b)
    if 0 <= a and a <= 100 :
        break
    
c = 100
while 0==0 :
    print("Ma proposition: ", c)
    if c == a :
            print("Exact !")
            break
    elif c < a :
        c = c + floor(c/2)
    else :
        c = c - floor(c/2)