#Já foi explicado essa função no exercício anterior
def somadigitos(x):
    if x<10:
        return x
    return somadigitos(x//10)+x%10

#Divisibiladade por 3 é dada por:
#Soma todos os digitos de 3 e ve se ele é divisivel por 3
#entao o que essa função faz: fica somando e somando os digitos até que de um número menor que 10
#e aí vamos ver se esse número é 3, 6 ou 9, porque todos eles são divisíveis por 3
#e também porque não da mais pra fazer o soma digito desses digitos, então esse é o caso base
#Resumidamente, é uma repercussão DENOVO

def div3(x):

    #O caso base, porque não vai dar pra somar mais, que é quando o x é menor que 10
    if x<10:

        #Se esse número for 3,6,9
        if x==3 or x==6 or x==9:
            
            #Retorna verdade, porque é divisivel sim por 3
            return True
        #caso nao for 3,6 e nem 9
        else:

            #retorna falso, porque não é divisivel por 3
            return False
    
    #Caso não seja menor que 10, vou ficar fazendo ele somar esses digitos até dar um número menor que 10
    return div3(somadigitos(x))

print(div3(192))