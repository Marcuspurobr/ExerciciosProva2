def ContaBit(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return ContaBit(n//2)+n%2
print(ContaBit(11))