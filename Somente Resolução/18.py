def twosum(l,r):
    lr=[]
    for d in l:
        for q in range(len(l)):
            if d+l[q]==r and l.index(d)!=q:
                return [l.index(d),q]
    return ('nenhum')
l=[2,4,5]
print(twosum(l,7))