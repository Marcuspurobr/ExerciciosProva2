def lista(x):
    if x<10:
        return [x]
    return lista(x//10)+[(x%10)]
def HappyNumber(x):
    l=[]
    while x not in l:
        if x==1:
            return True
        l.append(x)
        y=lista(x)
        x=0
        for d in range(len(y)):
            x=x+int(y[d])**2
    return False
print(HappyNumber(2))
print(HappyNumber(19))
print(HappyNumber(68))
