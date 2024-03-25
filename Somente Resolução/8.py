def perfeito(x):
    s=0
    for d in range(1,x):
        if x%d==0:
            s+=d
    if s==x:
        return True
    return False
print(perfeito(496))

