def primo(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def lista(x):
    if x<10:
        return [x]
    return lista(x//10)+[(x%10)]
def goodstring(x):
    x=lista(x)
    for p in range (len(x)):
        if p%2==0:
            if int(x[p])%2!=0:
                return False
        elif primo(int(x[p]))==False:
            return False
    return True
print(goodstring(2582))
print(goodstring(3245))