#O raciocínio que usei pra fazer:
#Primeiro vou ter 2 variaveis, o maior (m) número da lista e o segundo maior (m2)
#vou olhar cada número da lista
#se esse elemento da lista for maior que o (m), então vou chamar ele de M, e o antigo maior, vai ser chamado de (m2), que é o segundo maior
#mas caso esse elemento da lista não for maior que o (m), vamos analisar se ele é maior que o (m2), se sim, esse novo número será o (m2)
def maior2(l):

    #primeiro vou chamar o maior e o segundo maior de 0
    m=0
    m2=0

    #para cada numero na lista
    for n in l:

        #se o número for maior que o antigo maior(m),
        if n>m:

            #então o segundo maior, vai ser esse antigo maior
            m2=m

            #e o maior vai ser esse número que vimos na lista
            m=n

        #caso o número n for maior que o antigo maior(m), porém, maior que o segundo maior(m2)
        elif n>m2:

            #o segundo maior(m2) vai ser esse número n
            m2=n
    return m2
l=[2,5,8,9,11,7,12]
print(maior2(l))