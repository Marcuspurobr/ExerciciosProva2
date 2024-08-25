def desapareceu(l):
    #lista que vou dar a resposta
    ls=[]

    #quantidade de números
    n=len(l)

    #o exercício diz que é pra procurar no intervalo de [1,n]
    #visto que o intervalo é fechado, precisa incluir o n
    #como no 'range'do pyhton ele para antes
    #temos que adicionar +1 no 'n' para que o python pare no 'n'
    for d in range(1,n+1):
        
        #se o número tiver desaparecido
        if d not in l:

            #coloque na lista de desaparecidos
            ls.append(d)
    
    #retorna essa lista
    return ls
l=[1,1]
print(desapareceu(l))
