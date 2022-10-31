'''Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).
Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.'''

import funcaoidade
nome = input("Digite seu nome completo: ")
while (True):
    try:
        anoNasc = int(input("Digite o ano que você nasceu: "))
        print(nome, ", você tem", funcaoidade.idade(anoNasc), "anos.")
        break
    except ValueError:
        print("Erro: Você digitou um valor diferente de um inteiro de 4 digítos!")
    except Exception as erro:
        print(erro)