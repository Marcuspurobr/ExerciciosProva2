#Isso é só a função de primo, não precisa saber
def primo(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#Essa função aqui é pra transformar o número 'x' em uma lista
#temos que usar isso porque na função 'goodstring' temos que comparar cada digito
#então, uma maneira de comparar cada digito, é colocando cada algarismo como se fosse um elemento de uma lista
def lista(x):
    #Caso base da recursão, que é no caso 1 digito só
    #caso queira saber o que é caso base, pesquisa na net aí o que é recursão no python, que é bem mais fácil
    #do que eu digitar aqui
    if x<10:
        return [x]
    
    #tendo o caso base, vou querer que pra cada vez que ele fizer a recursão,
    #quero que ele coloque na lista o último número, e pegue o restante e faça a recursão
    return lista(x//10)+[(x%10)]

#exemplo: lista(234)
#vai retornar: lista(23)+[4]
#e lista(23) vai retornar lista(2)+[3]
#e lista(2) vai retornar [2]
#então ficaria tipo: [2]+[3]+[4], que vai dar [2,3,4]


#agora definir se um número é uma ''goodstring''
#o que é uma 'goodstring'?
#Pega cada digito de um número:
#se o número tiver na posição par, então ele deve ser par
#se o número tiver na posição ímpar, então ele deve ser PRIMO
#OBS: lembre-se que posição começa-se contando com 0
#EX: 2582 é uma goodstring, pois nas posições pares (posição 0 e 2), possuem os números (2,8) e ambos são pares
#e nas posições ímpares (posição 1,3), possuem os números (5,2) e ambos são primos

def goodstring(x):

    #primeiro vou transformar esse número em uma lista, pra facilitar acessar cada algarismo
    x=lista(x)

    #agora vou ver o tamanho do número usando o len(x)
    #e vou querer pegar a posição (p), de cada número
    #a posição 0 é o primeiro número, posição 1 é o segundo, posição 2 o terceiro...
    for p in range (len(x)):

        #se a posição for par
        if p%2==0:

            #e o número naquela posição não for par
            if int(x[p])%2!=0:

                #retorna que o número não é uma 'goodstring'
                return False
            
        #se ele não for par, então só pode ser ímpar
        #e se esse número na posição ímpar NÃO for primo
        elif primo(int(x[p]))==False:

            #retorna que o número não é uma 'goodstring'
            return False
    
    #mas caso nenhum desses casos tenha acontecido, então ele é uma goodstring
    return True
print(goodstring(2582))
print(goodstring(3245))
