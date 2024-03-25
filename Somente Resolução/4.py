def desapareceu(l):
    ls=[]
    n=len(l)
    for d in range(1,n+1):
        if d not in l:
            ls.append(d)
    return ls
l=[1,1]
print(desapareceu(l))