def primzahl(x):
    a=0
    for i in range(2,x-1,1):
        if x%i==0:
            a=a+1
            print(i)
    if a>0:
        return("Keine Primzahl")
    elif x==2:
        return("Primzahl")
    else:
        return("Primzahl")