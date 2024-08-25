#Definindo a função
def soma1(l):

    #primeiro vou transformar essa lista em um número
    l=digitos(l)

    #faço a soma
    r=l+1

    #depois eu pego esse número e faço uma lista com ele, e retorno
    return lista(r)

#Essa função aqui que usei pra transformar a lista em número
def digitos(l):
    #se a lista está vazia, vale 0, mas aí vai somando de acordo com os números da lista
    n=0

    #Para cada valor na lista
    for d in l:

        #o novo valor vai ser o anterior vezes 10, mais o atual
        #exemplo: a lista [2,4,6]
        #n=(0*10)+2
        #n=(2*10)+4
        #n=(24*10)+6
        #n=246
        n= (n*10)+d
    
    #retorna o valor do número
    return n

#a explicação dessa função está no exercício 2 que eu postei no github
def lista(x):
    if x<10:
        return [x]
    return lista(x//10)+[(x%10)]
print(soma1([9,9,9]))
