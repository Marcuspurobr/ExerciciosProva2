def primo(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
def apenasprimos(l):
    for d in l:
        if primo(d)==False:
            return False
    return True
l1=[2,3,5,7]
l2=[2,3,5,14]
print(apenasprimos(l1))
print(apenasprimos(l2))