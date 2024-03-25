def filtrarPAR(l):
    ln=[]
    for d in l:
        if d%2==0:
            ln.append(d)
    return ln
l=[2,5,7,9,12]
print(filtrarPAR(l))