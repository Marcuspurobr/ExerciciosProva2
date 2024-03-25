#Esse é um exercício básico de repercussão
#Vou dar um exemplo do raciocínio utilizado:
#exemplo: somadigitos(356)
#somadigitos(356) = somadigitos (35) + 6
#somadigitos(35)= somadigitos (3) + 5
#somadigitos(3)= somadigitos 3
#ou seja, somadigitos(356)= 3+5+6, que é igual a 14
def somadigitos(x):
    
    #Se o caso base for menor que 10
    if x<10:

        #só retorna ele mesmo
        return x
    
    #A repercussão, pega o último número da direita e soma com o somadigitos do resto
    return somadigitos(x//10)+x%10
print(somadigitos(1567))