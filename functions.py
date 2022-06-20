#Bibliotecas usadas
from tabulate import tabulate
import time

#matriz dos produtos, id, produto, preço e quantidade em estoque
matrix=[[1,"Coke",3.75,2],
        [2,"Pepsi",3.67,5],
        [3,"Monster",9.96,1],
        [4,"Coffe",1.25,100],
        [5,"Redbull",13.99,2]]

#função para pedir o produto de escolha e o dinheiro
def askProduct():
    print("\n      ---Vending Machine---    \n")

    #imprime a matriz usando biblioteca de tabulação para deixar a visualização mais apresentável
    print(tabulate(matrix, headers=["Id", "Product", "Price", "Stock"]))

    #escolha do usuário
    choice = int(input("\n--------------------------------------\nType your choice's ID -> "))

    #caso de número inválido
    while choice > 5 or choice < 1:
        print("\nID Error, choose again.")
        choice = int(input("\n--------------------------------------\nType your choice's ID -> "))
    
    #caso de escolha sem estoque
    while matrix[choice - 1][3] == 0:
        print("\nProduct out of stock.")
        choice = int(input("\n--------------------------------------\nType your choice's ID -> "))
    print("--------------------------------------")
    
    #Usuário coloca o dinheiro
    insert = float(input("Price: " + str(matrix[choice - 1][2]) + "\n--------------------------------------\nInsert money-> "))
    price = matrix[choice - 1][2]

    #caso de dinheiro insuficiente (maquina devolve e pede para colocar um valor maior que o preço)
    while insert < price:
        print("\nThe value is insuficient, please, try again.\n")
        insert = float(input("Price: " + str(matrix[choice - 1][2]) + "\n--------------------------------------\nInsert money-> "))

    #Informa o valor do troco
    change = insert - matrix[choice - 1][2]  
    print("Your change is:",change)
    
    return change, choice

#função para calcular e devolver o troco
def change(change):
    coins=[200,100,50,20,10,5,2,1,0.25,0.5,0.1]

    #calcula a menor quantidade possível de notas e moedas para dar o troco com base na lista 'coins'
    for i in range(len(coins)):
        if change >= coins[i]:
            number = change/coins[i]
            n = int(number)*coins[i]
            change -= n
            if coins[i]>1:
                bills="bill(s)"        
            else:
                bills="coin(s)"
    
    #Informa quantas notas e moedas de cada valor o usuário recebeu de troco
            print("You received",int(number),": ", coins[i], "Reais", bills)
    print("--------------------------------------\n")
    time.sleep(5)