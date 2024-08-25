#Essa função tem como base uma rainha de xadrez
def rainhaataca(l1,c1,l2,c2):

    #Se a rainha estiver na mesma coluna ou linha que a peça
    if l1==l2 or c1==c2:

        #então ela ataca
        return True
    
    #Se a rainha estivar na mesma diagonal 1 que a peça
    if (l2-l1)==(c2-c1):

        #então ela ataca
        return True
    
    #Se a rainha estivar na mesma diagonal 2 que a peça
    if (l2-l1)==-(c2-c1):

        #então ela ataca
        return True
    
    #se nenhuma das condições anteriores cumprirem, então ela não ataca
    return False
print(rainhaataca(6,6,3,4))
