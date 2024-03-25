def MergeTwoLists(l1,l2):

    #primeiro vou precisar fazer uma terceira lista, que vai ser a resposta do que o enunciado pede
    l3=[]

    #agora vou precisar de comparar os números de cada lista, sempre começando pelos primeiros de cada uma
    #aqui dei valores as posições dos números de cada lista, como a primeira posição é zero, dei o valor de zero as variáveis
    p1=0
    p2=0

    #Eu quero ficar adicionando vários numeros na minha terceira lista, até que chegue no limite da lista1 e lista2, ou seja,
    #quando o número de elementos de cada lista, não chega ao último número, quero que se repita
    #ex: na lista [2,4,6], quero testar os numeros nas posições, (0,1,2), quando a posição chega no limite (3), eu quero que ela pare
    #porém tenho que continuar executando até que eu teste todas as posições das lista 1 e lista 2
    #logo, vou ficar testando (enquanto eu NÃO chegar no limite da Lista1 OU NÃO chegar no limite da Lista2)
    #e essa parte entre parênteses que é o codigo na linha de baixo
    while p1!=len(l1) or p2!=len(l2):

        #agora se eu cheguei no limite da linha lista 1, porém não no limite da lista 2
        if p1==len(l1):
            #vou adicionar o número restante da lista 2
            l3.append(l2[p2])
            #vai pra próxima posição da lista 2
            p2+=1
        
        #Caso agora se eu tiver chegado no limite da lista 2, mas não no limite da lista 1
        elif p2==len(l2):
            #vou adicionar o número restante da lista 1
            l3.append(l1[p1])
            #vai pra próxima posição da lista 1
            p1+=1

        #Esses de cima foram os casos das listas CASO alguma delas ja tivesse colocado todos os números dela,
        #Caso falte colocar número das duas listas, vamos ter que comparar pra ver qual deles é o menor, e colocar
        #Porque no exercício ele pede em ordem crescente
            
        #Esse primeiro é caso o número da primeira lista seja o menor
        elif l1[p1]<=l2[p2]:
            #então adiciona esse menor número da lista 1.
            l3.append(l1[p1])
            #vai pra próxima posição da lista 1
            p1+=1

        #Esse primeiro é caso o número da segunda lista seja o menor
        elif l2[p2]<l1[p1]:
            #então adiciona esse menor número da lista 2
            l3.append(l2[p2])
            #vai pra próxima posição da lista 2
            p2+=1
            
    #quando todo esse looping acabar, e eu ter uma lista 3 com todos os números das lista1 e lista2, quero que retorne essa nova lista
    return l3
l1 = [0,2,5,8]
l2 = [1,2,3,4,5,6,7]
print(MergeTwoLists(l1,l2))