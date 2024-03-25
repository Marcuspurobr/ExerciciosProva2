#Função para filtrar os números pares, bem parecido com a anterior
#A lógica dessa função que vou usar é, vou criar uma lista nova
#E para cada elemento da lista antiga, se ele for par, vou colocar na lista nova, e imprimir a nova


def filtrarPAR(l):

    #Primeiramente criei a lista nova (ln)
    ln=[]

    #E vou analisar cada elemento da lista antiga
    for d in l:

        #Se algum deles for par
        if d%2==0:

            #vou adicionar na lista nova
            ln.append(d)

    #e no final retorna a lista nova
    return ln
l=[2,5,7,9,12]
print(filtrarPAR(l))