def CountGoodString(n):
    if n%2==0:
        return 5**(n//2) * (4**(n//2)) % (10**9 + 7)
    return (5**(n//2)) * (4**(n//2)) * (5) % (10**9 + 7)
print(CountGoodString(50))