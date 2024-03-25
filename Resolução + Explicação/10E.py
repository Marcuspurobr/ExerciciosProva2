#Nesse exercício é só aplicar o que ta escrito no enunciado
#Talvez vocês possam errar por conta dos vários parenteses que tem no meio da conta
#Então tomem cuidado com eles
def Fibonacci(n):

    #aqui é o caso base do fibonacci, caso não tenha entendido olha la os slides, que la explica a definição
    if n==1 or n==2:
        return 1
    
    #Essa parte aqui eu só copiei o que ta escrito no exercício
    #Nessa parte aqui é a parte que ta escrito ''F 2n''
    if n%2==0:
        return 2*Fibonacci((n//2)+1)*Fibonacci(n//2)-Fibonacci(n//2)**2
    
    #E essa parte é a que está escrito ''F 2n+1''
    return (Fibonacci((n//2)+1))**2+(Fibonacci(n//2))**2

#Só mandei printar vários Fibonacci pra testar se está certo
for d in range(1,20):
    print(Fibonacci(d))