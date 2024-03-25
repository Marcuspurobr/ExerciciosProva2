def rainhaataca(l1,c1,l2,c2):
    if l1==l2 or c1==c2:
        return True
    if (l2-l1)==(c2-c1):
        return True
    if (l2-l1)==-(c2-c1):
        return True
    return False
print(rainhaataca(6,6,3,4))
