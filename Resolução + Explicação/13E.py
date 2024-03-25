#Isso aqui não precisa saber fazer, pra fazer a prova, porque ele vai deixar escrever só 'Primo' na hora, e não precisa escrever a função

def primo(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

#Agora a função de ver se TODOS elementos da lista são primos
#por incrivel que pareça, não vamos usar mais repercussão (AMÉM)

def apenasprimos(l):

    #Primeiro vamos olhar cada um dos elementos da lista
    for d in l:
        
        #Se algum desses elementos não for primo
        if primo(d)==False:

            #Retorna falso, porque na lista tem um número que não é primo
            return False
    
    #Caso não retorne falso nenhuma vez, então todos elementos da lista são primos, então retorna verdade
    return True

l1=[2,3,5,7]
l2=[2,3,5,14]
print(apenasprimos(l1))
print(apenasprimos(l2))