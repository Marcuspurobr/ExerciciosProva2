#O raciocínio que usei pra criar essa função foi:
#Primeiro vou criar uma lista nova (como sempre né)
#Aí, vou olhar cada elemento da lista, e vou adicionar ele, se ele não estiver na lista nova
#exemplo: l= [1,2,2,4]
#primeiro eu adiciono o 1 na lista nova: ln=[1]
#depois eu adiciono o 2 na lista nova: ln=[1,2]
#mas aí eu vejo que na lista nova já tem o 2, então não adiciono
#depois eu adiciono o 4 na lista nova: ln=[1,2,4]
#aí eu retornaria a lista nova


def removerDUP(l):

    #criei a lista nova
    ln=[]

    #olhando para cada número da lista
    for d in l:

        #se esse número não tem na lista nova
        if d not in ln:

            #adiciona na lista nova
            ln.append(d)

    #e no final retorna a lista nova
    return ln

l=[2,4,5,2,4]
print(removerDUP(l))
