""" Faça uma função calculadora que os números e as operações serão feitas pelo usuário. O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:
1: Soma
2: Subtração
3: Multiplicação
4: Divisão
0: Sair

Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”, o sistema irá parar. 

É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado."""

import calculadora
import os
import time
num1 = 0.0
num2 = 0.0
teste = 5
while(teste != 0):
    os.system("cls")
    teste = int(input("Escolha uma opção: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n0 - Sair\n"))
    if( teste >= 1 and teste <= 4):
        num1 = float(input("Informe o primeiro número: "))
        num2 = float(input("Informe o segundo número: "))
        print("Resultado: ", calculadora.calculadora(num1, num2, teste))
        time.sleep(3)
    elif(teste == 0):
        print("Encerrando programa!!!")
    else:
        print("Opção inválida, escolha uma opção valida na próxima!")
        time.sleep(3)