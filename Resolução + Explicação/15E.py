# O raciocinio que usei pra criar essa função foi:
#Verifico se um elemento da lista 1 também existe na lista 2
#se sim, vou adicionar esse elemento na lista nova
#e depois vou remover esse elemento da lista dois
#eu preciso remover esse elemento para que eu não fique adicionando o mesmo numero varias vezes
def intersec(l1,l2):

    #A lista nova, que é a lista de interseção
    ln=[]

    #vou analisar cada número da lista 1
    for d in l1:

        #Se ele estiver na lista 2
        if d in l2:

            #Vou adicionar ele na lista de interseção
            ln.append(d)

            #E removelo da lista 2
            l2.remove(d)

    #e no final retornar a lista interseção
    return ln
l1=[1,5,7,8,1]
l2=[5,7,1,1]
print(intersec(l1,l2))