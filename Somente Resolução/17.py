def removerDUP(l):
    ln=[]
    for d in l:
        if d not in ln:
            ln.append(d)
    return ln
l=[2,4,5,2,4]
print(removerDUP(l))
