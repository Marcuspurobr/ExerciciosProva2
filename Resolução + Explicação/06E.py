#Esse exercício está meia simplificada a explicação porque o prof ja explicou na aula
#Definição que conta os bits (1) de um número binário
#lembrando que, usaremos a base 2, por isso vou ficar dividindo por 2
def ContaBit(n):
    
    #Caso base
    #Se o valor for 0, então tem 0
    if n==0:
        return 0
    
    #se o valor for 1, então tem 1
    if n==1:

        #retorna 1
        return 1
    
    #repercussão
    return ContaBit(n//2)+n%2

print(ContaBit(11))
