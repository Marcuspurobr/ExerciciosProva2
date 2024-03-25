def soma1(l):
    l=digitos(l)
    r=l+1
    return lista(r)
def digitos(l):
    n=0
    for d in l:
        n= (n*10)+d
    return n
def lista(x):
    if x<10:
        return [x]
    return lista(x//10)+[(x%10)]
print(soma1([9,9,9]))