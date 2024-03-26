#Função que deve retornar varias strings em uma lista
#Por exemplo, tem uma string com 10 elementos, e pede substrings de tamnho 2
#temos que retornar 5 substrings de tamanho 2
#exemplo: 'marcusmarcus'
#deve retornar: ´[ma,rc,us,ma,rc,us]
def subsSTR(x,k):

    #Primeiro vou criar a lista que vou devolver as substrings
    ln=[]

    #Depois vou ver qual o tamanho dela
    x=str(x)

    #E vou ver quantas vezes da pra dividir essa lista do tamanho K, porque a pessoa pode escolher na função, qual tamanho quer
    t=len(x)//k

    #E ver se tem algum resto, que não divide certinho, por exemplo
    #se uma string tem tamanho 11, e queremos substrings de 2
    #no final temos que devolver uma substring de tamanho 1
    r=len(x)%k

    #Para cada possível parte da substring q da pra dividir
    #por exemplo, uma string de 10 digitos que quer substrings de tamanho 2, então da pra dividir 5 vezes
    # os valores serão [0,1,2,3,4]
    for d in range(t):

        #então, aqui complica um pouco mas não desespera
        #Primeiramente vamos ter na cabeça os valores do D que podem ser [0,1,2]
        #E que quero, por exemplos substrings de tamanho 2
        #Então o que eu vou querer que adiciona?
        #Primeiro os numeros da posição 0 e a posição 1
        #depois da posição 2 e posição 3
        #depois da posição 4 e posição 5
        #depois da posição 6 e posição 7
        #depois da posição 8 e posição 9
        #Mas como o python sempre para um antes, ficaria assim:
        #[0:2],[2:4],[4:6],[6:8],[8:10],
        #que pode ser escrito como:
        #esse número D * o tamanho que queremos, até esse número mais o tamanho
        #tradução: uma string 'marcusmarcus' com tamanho 2
        #primeiro pegamos 0*2:(0*2)+2
        #entao o primeiro vai ser do 0 até o 2 : [ma]
        #próximo: 1*2:(1*2)+2
        #vai ser do 2 até o 4: [rc]
        #sei que é meio dificil entender, mas não tem um jeito melhor de eu explicar aqui, sorry
        ln.append(x[k*d:(k*d)+k])

    #E esse final aqui é pro resto
    if r!=0:

        #Que vai adicionar o começo do resto, até o final da string
        ln.append(x[(len(x))-r-1:(len(x))-1])

    #e no final retorna a string ja toda repartida
    return ln
print(subsSTR('marcusmarcus',2))
