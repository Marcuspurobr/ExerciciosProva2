#Essa função eu ja fiz nos exercícios 2 e 3


def lista(x):
    if x<10:
        return [x]
    return lista(x//10)+[(x%10)]

#Essa função tem o seguinte raciocínio:
#Primeiro pegamos um número, e para cada algarismo dele, precisamos somar o quadrado de cada algarismo
#e se o resultado for 1, então ele é um ''happy number''
#se não for, repete o processo 'infinitamente'
#e precisamos descobrir se um número é um happy number ou nao
#Exemplo: 86
#pegamos a cada algarismos -> 8 e 6
#fazemos ao quadrado-> 64 e 36
#e soma -> 100
#fazemos de novo -> 1 + 0 + 0
# da o resultado 1, então 86 é um happy number

def HappyNumber(x):

    #Primeiro vou criar uma lista, mas dessa vez é para tentar evitar o looping infinito
    #como eu disse no inicio, se um numero entra em um looping infinito, ele não é um 'happy number'
    #mas para que isso se torne um algoritmo, não podemos entrar em um looping, o que nos complica
    #porém há um jeito de resolver isso
    l=[]

    #O jeito que utilizei foi esse, o unico jeito de um happy number se repetir infinitamente, é se caso ele faça aquela soma la varias vezes
    #uma hora ele vai repetir algum número
    #então eu criei uma lista, e toda vez que fizermos alguma soma dos números, vou anotar o resultado nessa lista
    #enquanto a lista não houver números repetidos, vou executar o algoritmo
    #se por acaso repetir algum número, eu sei que isso vai resultar em um looping infinito
    #então eu retorno Falso
    
    #Então, enquanto não há repetição:
    while x not in l:

        #Primeiro vejo se o número é 1, por que se for, é a resposta correta
        if x==1:
            return True
        
        #Se não for, colocamos esse número na lista de números que ja foi
        l.append(x)

        #E vou transfomar esse número em uma lista, mas isso é mais pra eu somar cada algarismo
        y=lista(x)

        #Vou chamar o novo número de 0 só por enquanto, e depois vou colocar que ele é a soma dos seus digitos ao quadrado
        x=0

        #Para cada algarismo na lista:
        for d in range(len(y)):

            #Vou somar cada algarismo ao quadrado na variavel X, e voltar ao looping
            x=x+int(y[d])**2
    
    #o algoritmo vai resultar em looping, então retorno falso
    return False
print(HappyNumber(2))
print(HappyNumber(19))
print(HappyNumber(68))