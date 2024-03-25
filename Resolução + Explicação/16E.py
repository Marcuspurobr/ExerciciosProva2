#O raciocinio que usei pra fazer essa função foi:
#primeiramente peguei cada número da lista,
#e para cada um desses números, eu olhei o resto dos números da lista, pra ver se tem um igual a ele

def contemDUP(l):

    #Para cada elemento da lista
    for d in l:

        #Peguei cada posição da lista, para que eu possa analisar o resto dos números
        for q in range(len(l)):

            #Se tiver um número (d) na lista em alguma posição [q], (e que NÃO seja na posição do número D)
            #Explicação do parentese: se eu não colocar essa parte, ele vai sempre comparar com ele mesmo
            #e sempre vai falar que tem duplicado, então tem que deixar claro que não é ele mesmo
            if d==l[q] and l.index(d)!=q:

                #retorna verdade, se tiver duplicado
                return True
            
    #se não, retorna falso
    return False
l1=[1,2,3,4,5,1]
l2=[1,3,2,4]
print(contemDUP(l1))
print(contemDUP(l2))