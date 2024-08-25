#O professor pediu pra fazer uma versão mais rápida em sala de aula, que seria conforme o exemplo:
#Se pede (5^20), tu deve fazer (5^10)^2
#E do (5^10), tu faz (5^5)^2, então meio que no final fica ((5^5)^2)^2, e vamos fazer isso varias e varias vezes até o caso base ficar bem pequeno
#Também conhecido como repercussão

#Sendo que eu chamei o número X o numero da base e o Y o expoente
def pot(x,y):

    #Caso base da repercussão, porque uma hora vai chegar no número elevado a 1
    if y==1:
        
        #retorna ele mesmo, porque um número elevado a 1, é igual a ele mesmo
        return x
    
    #Agora caso o Y nao for um, eu faço esse número com o expoente pela metade, vezes ele mesmo
    #exemplo: (5^20) passa a ser (5^10)*(5^10)
    if y%2==0:
        return pot(x,y//2)*pot(x,y//2)
    
    #Mas isso pode complicar caso o número do expoente for ímpar,
    #então nesse caso, vamos dividir por 2 mesmo, normalmente e pegar a parte inteira
    #Porem como vamos só pegar a parte inteira, vai ficar sobrando o 1
    #então no final coloco o número elevado 1 (que da a ele mesmo)
    #exemplo: (5^7) passa a ser (5^3)*(5^3)*(5^1)
    #o que não deixa de ser uma verdade, então está certo
    if y%2==1:
        return pot(x,y//2)*pot(x,y//2)*pot(x,1)
print(pot(25,2))
