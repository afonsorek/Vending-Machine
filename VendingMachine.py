#importa o arquivo das funções para facilitar o loop
import functions

cont = 0
#loop da máquina funcionando eternamente chamando as funções
while cont == 0:
    x, y = functions.askProduct()
    functions.change(x)
    
    #Subtrai item do estoque
    functions.matrix[y - 1][3] -= 1