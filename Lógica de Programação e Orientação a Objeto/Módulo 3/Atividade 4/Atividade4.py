#Crie um tipo abstrato de dado (TAD) para manipular números complexos na linguagem Python.
#O método deve:

#- calcular três números complexos;
#- realizar todas as operações básicas;
#- e imprimir as propriedades real e img do números. 

class Complexos:
    
    def calcular_complexos(a, b, c):
        N1 = complex(a)
        N2 = complex(b, c)
        N3 = complex(c, a)

        print("Qual o primeiro número complexo ?")
        type(a)

        print("Qual o segundo número ?")
        type(b)

        print("Qual o terceiro número ?")
        type(c)

        
        adicao = N1 + N2 + N3
        print("Adição =", adicao)
        print("Parte Real =", adicao.real)
        print("Parte Imaginária =", adicao.imag)
    
        Sub = N1 - N2 - N3
        print("Subtração =", sub)
        print("Parte Real =", sub.real)
        print("Parte Imaginária =", sub.imag)
    
        Mult = N1 * N2 * N3
        print("Multiplicação =", mult)
        print("Parte Real =", mult.real)
        print("Parte Imaginária =", mult.imag)
    
        Div = N1 / N2 / N3
        print("Divisão =", div)
        print("Parte Real =", div.real)
        print("Parte Imaginária =", div.imag)

        
    print(calcular_complexos(a, b, c))