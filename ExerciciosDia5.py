# 1- Construa um programa que quando executado mostra "Hello World"

def questao1():
    print("Hello World")


# 2- Construa um programa que armazena em duas variaveis duas notas e apresenta a média entre as duas

def questao2():
    nota1 = int(input("Entre com uma nota: "))
    nota2 = int(input("Entre com outra nota: "))
    media = (nota1 + nota2)/2

    print("A média dessas notas é: ", media)


#3- Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar

def questao3():
    valor1 = int(input("Entre com um valor: "))
    valor2 = int(input("Entre com outro valor: "))
    soma = valor1 + valor2

    if soma%2 == 0:
        print("A soma dos dois valores resulta em um valor par")
    else:
        print("A soma dos dois valores resulta em um valor impar")    


#4- Construa um programa que armazena uma idade em uma váriavel e compara, se a idade for maior que 18, apresenta "Maior de idade", se a idade for menor que 12, apresenta "Você é uma criança" e se for maior que 12 e menor que 18, apresenta "Você é um adolescente

def questao4():
    idade = int(input("Entre com uma idade: "))

    if idade > 18:
        print("Maior de idade")
    elif 18 > idade > 12:
        print("Você é um adolescente")
    else:
        print("Você é uma criança")


#5- Construa um programa que recebe 20 valores para X e no final apresenta a média aritmética dos valores pares digitados

def questao5():

    #lista para armazenar os valores pares
    valores = []

    #contador para o loop
    count = 1

    #loop para receber 20 inputs
    while count <= 20:
        X = int(input("{0}- Entre com um valor: ".format(count)))
        
        #armazena os valores pares na lista
        if X%2 == 0:
            valores.append(X)
        
        #incremento do contador
        count += 1
    
    #calcula a media aritmetica
    media = sum(valores)/len(valores)

    print("A média aritmética dos valores pares é: ", media)


#6- Construa um programa que receba uma valor inteiro maior que 2 em uma variavel x e apresenta os impares entre 0 e x

def questao6():

    #variável utilizada para conferir se o valor de entrada é maior que 2
    maiorQue2 = False

    #variável que temporariamente armazena um número entre 0 e o valor de entrada
    numero = 0

    #lista que armazena os valores ímpares
    impares = []

    while maiorQue2 == False:
        valor = int(input("Entre com um valor maior que 2: "))

        if valor <= 2:
            print("O valor deve ser maior que 2. Tente novamente.")
        else:
            maiorQue2 = True

    while numero <= valor:
        if numero%2 != 0:
            impares.append(numero)
        
        numero += 1
    
    print("Os valores ímpares entre {0} e 0 são: ".format(valor), impares)


'''
7- Crie um programa que contêm uma função que receba dois parâmetros inteiros e retorna a média dos dois valores

8- Crie um programa que lê 1 valor inteiro para X. Se o valor for par, calcular o fatorial de x em uma função e apresentar o resultado fora da função. Se o valor for impar, apresentar em uma função a tabuada de 1 a 10 de X.

9- Crie um programa que recebe 15 valores e armazena em uma lista, e no final da execução mostre os valores da lista do ultimo para o primeiro

10- Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"]

11- Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas. Entrada: A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo. Saída: Apresente a duração do jogo conforme exemplo abaixo.

12 - Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias. Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.
'''

############# ÁREA DE EXECUÇÃO DOS EXERCÍCIOS #############

print("Exercício 1:")
questao1()

print("Exercício 2:")
questao2()

print("Exercício 3:")
questao3()

print("Exercício 4:")
questao4()

print("Exercício 5:")
questao5()

print("Exercício 6:")
questao6()