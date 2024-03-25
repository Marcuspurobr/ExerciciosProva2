def pot(x,y):
    if y==1:
        return x
    if y%2==0:
        return pot(x,y//2)*pot(x,y//2)
    if y%2==1:
        return pot(x,y//2)*pot(x,y//2)*pot(x,1)
print(pot(25,2))
