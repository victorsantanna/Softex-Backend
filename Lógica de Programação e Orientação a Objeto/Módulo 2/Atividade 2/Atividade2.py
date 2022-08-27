# Desenvolva um código que utilize as seguintes características de um veículo:
#- Quantidade de rodas;
#- Peso bruto em quilogramas;
#- Quantidade de pessoas no veículo.
#Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
#A: Veículos com duas ou três rodas;
#B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
#C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
#D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas;
#E: Veículos com quatro rodas ou mais e com mais de 6000 kg.*/

#python

qtdRodas = int(input("Informe a quantidade de Rodas do veículo: "))
peso = float(input("Informe o peso bruto em quilogramas do veículo: "))
qtdPessoas = int(input("Informe a quantidade máxima de pessoas transportadas no veículo: "))

if qtdRodas == 2 or qtdRodas == 3 :
    print("O veiculo é da categoria A")
elif qtdRodas == 4 and qtdPessoas <= 8 and peso <= 3500 :
    print("O veiculo é da categoria B")
elif qtdRodas >= 4 and qtdPessoas <= 8 and peso > 3500 and peso <= 6000 :
    print("O veiculo é da categoria C")
elif qtdRodas >= 4 and qtdPessoas > 8 and peso <= 6000 :
    print("O veiculo é da categoria D")
elif qtdRodas >= 4 and peso > 6000 :
    print("O veiculo é da categoria E")
else:
    print("O veiculo não se enquadra em nenhuma categoria de habilitação!")