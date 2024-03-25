#Raciocínio que usei pra fazer essa função:
#Primeiramente vou fazer igual a 16, vou pegar um número da lista e vou comparar com o resto dos números
#se eu achar um número que somado com outro (que não seja ele mesmo) de a resposta (que chamei de "r")
#retorna a posição do número e a posição do outro número que somou (lembrando que ele não quer saber quais números somaram, mas sim suas posições)
def twosum(l,r):

    #vou olhar cada número da lista (d)
    for d in l:

        #Peguei cada posição da lista, para que eu possa analisar o resto dos números
        for q in range(len(l)):
            
            #Se a soma de um número da lista(n) somado com outro número da lista na posição [q] da lista der o resultado "r"
            #e esse número não pode ser ele mesmo
            if d+l[q]==r and l.index(d)!=q:
                
                #retorna a posição do número d, e o "q", que já é a posição do segundo número
                return [l.index(d),q]
            
    #mas se não achar nenhum número que a soma da "r", então retorna 'nenhum'
    return ('nenhum')
l=[2,4,5]
print(twosum(l,7))