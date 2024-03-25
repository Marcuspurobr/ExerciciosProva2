def contemDUP(l):
    for d in l:
        for q in range(len(l)):
            if d==l[q] and l.index(d)!=q:
                return True
    return False
l=[1,2,3,4,5,1]
l2=[1,3,2,4]
print(contemDUP(l))
print(contemDUP(l2))