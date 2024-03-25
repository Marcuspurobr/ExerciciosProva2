def maior2(l):
    m=0
    m2=0
    for d in l:
        if d>m:
            m2=m
            m=d
        elif d>m2:
            m2=d
    return m2
l=[2,5,8,9,11,7,12]
print(maior2(l))