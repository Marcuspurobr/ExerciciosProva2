def lemonade(x):
    notas=[]
    for d in x:
        notas.append(d)
        if d==10:
            if 5 not in notas:
                return False
            notas.remove(5)
        if d==20:
            if (5 or 10) not in notas:
                return False
            notas.remove(5)
            notas.remove(10)
    return True
r=[5,5,10,20,20]
print(lemonade(r))