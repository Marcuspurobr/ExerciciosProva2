def somadigitos(x):
    if x<10:
        return x
    return somadigitos(x//10)+x%10
print(somadigitos(1567))