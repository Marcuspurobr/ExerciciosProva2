def somadigitos(x):
    if x<10:
        return x
    return somadigitos(x//10)+x%10
def div3(x):
    if x<10:
        if x==3 or x==6 or x==9:
            return True
        else:
            return False
    return div3(somadigitos(x))
print(div3(192))