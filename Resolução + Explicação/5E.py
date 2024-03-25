#função pra descobrir se todos os clientes tem troco
#lembrando que cada limonada custa 5 conto
#e que começamos sem nota nenhuma
def lemonade(x):

    #lista das notas que temos
    notas=[]

    #vamos testar todas as notas dos clientes
    for d in x:

        #para cada nota que o cliente entrega, vamos colocar na lista
        notas.append(d)

        #se a nota for de 10 conto
        if d==10:

            #vamos ver se temos 5 conto na lista, se não tiver
            if 5 not in notas:

                #vamos retornar 'False' porque nao temos troco pra todo mundo
                return False
            
            #Mas se tivermos uma nota de 5, vamos remover ela
            #(porque damos de troco e perdemos ela)
            notas.remove(5)
        
        #se a nota do cliente for de 20
        if d==20:
            #vamos ver se temos as notas 5 e 10, mas se não tivermos uma das duas
            if (5 or 10) not in notas:

                #vamos retornar 'False' porque nao temos troco pra todo mundo
                return False
            
            #Mas se tivermos essas duas notas, vamos remove-las
            #(porque damos de troco e perdemos elas)
            notas.remove(5)
            notas.remove(10)
    
    #caso não dê nenhum problema com o troco, deu certo
    return True
r=[5,5,5,10,20]
print(lemonade(r))