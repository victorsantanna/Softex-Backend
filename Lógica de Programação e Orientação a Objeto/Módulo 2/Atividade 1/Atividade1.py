#/*Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:
#- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
#- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado;
#- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está #aprovado.
#No sistema, todos os valores devem estar armazenados em variáveis.*/

nomeAluno = ""
nota1 = 0.0
nota2 = 0.0
media = 0.0
qtdFaltas = 0

print("Digite o nome do Aluno: ")
nomeAluno = input()
qtdFaltas = int(input("Digite a quantidade de faltas do Aluno: "))
nota1 = float(input("Digite a primeira nota do Aluno: "))
nota2 = float(input("Digite a segunda nota do Aluno: "))
media = (nota1+nota2)/2
if qtdFaltas > 3:
    print(nomeAluno, "você está reprovado por falta, com", qtdFaltas, "faltas.")
elif media < 7.0:
    print(nomeAluno, "você está reprovado por média, com", media, ".")
else:
    print(nomeAluno, "você está APROVADO por média, com", media, ".")