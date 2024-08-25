#Um número perfeito é um número natural para o qual a soma de todos os seus divisores naturais próprios (excluindo ele mesmo) é igual ao próprio número.
def perfeito(x):

    #Primeiro chamei a soma de 0, porque ainda não somei nada
    s=0

    #Vou pegar todos os números de 1 até todos menos ele mesmo
    #ex: se x for 10, vou pegar todos os números de 1 a 9
    for d in range(1,x):

        #se eu achar algum divisor
        if x%d==0:

            #vou somar ele, por causa da definição de numero perfeiro
            s+=d
            
    #agora vou ver se ele é perfeito, vou comparar a soma dos seus divisores, com o próprio número
    if s==x:

        #se for igual, retorna verdadeiro
        return True
    #se não for igual, retorna falso
    return False
print(perfeito(496))

