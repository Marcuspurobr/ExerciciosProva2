def intersec(l1,l2):
    ln=[]
    for d in l1:
        if d in l2:
            ln.append(d)
            l2.remove(d)
    return ln
l1=[1,5,7,8,1]
l2=[5,7,1,1]
print(intersec(l1,l2))