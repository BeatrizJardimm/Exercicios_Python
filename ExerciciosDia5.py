# -> Cada questão foi desenvolvida dentro de uma função
# -> O código para rodar cada uma delas se encontra no trecho final deste arquivo

# 1- Construa um programa que quando executado mostra "Hello World"

def questao1():
    print("Hello World")


# 2- Construa um programa que armazena em duas variaveis duas notas e apresenta a média entre as duas

def questao2():
    #variáveis que armazenam os valores lidos
    nota1 = float(input("Entre com uma nota: "))
    nota2 = float(input("Entre com outra nota: "))

    #variável que armazena o cálculo da média
    media = (nota1 + nota2)/2

    #mostra o resultado na tela
    print("A média dessas notas é: ", media)


#3- Construa um programa que recebe dois valores, soma esses valores e apresenta se o resultado é par ou impar

def questao3():
    #variáveis que armazenam os valores lidos
    valor1 = int(input("Entre com um valor: "))
    valor2 = int(input("Entre com outro valor: "))

    #variável que armazena a soma dos valores
    soma = valor1 + valor2

    if soma%2 == 0: #verifica se a soma resulta em um valor par
        print("Resultado: ", soma)
        print("A soma dos dois valores resulta em um valor par")
    else: #caso o valor não seja par, esse código é executado
        print("Resultado: ", soma)
        print("A soma dos dois valores resulta em um valor impar")


# 4- Construa um programa que armazena uma idade em uma váriavel e compara, se a idade for maior que 18, apresenta "Maior de idade",
# se a idade for menor que 12, apresenta "Você é uma criança" e se for maior que 12 e menor que 18, apresenta "Você é um adolescente

def questao4():
    #variavel que armazena a idade lida
    idade = int(input("Entre com uma idade: "))

    if idade > 18: #verifica se o usuário tem mais de 18 anos
        print("Maior de idade")
    elif 18 > idade > 12: #verifica se o usuário tem mais de 12 e menos de 18 anos
        print("Você é um adolescente")
    else: #caso o usuário tem menos de 12 anos, esse código é executado
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

    #exibe o resultado na tela
    print("A média aritmética dos valores pares é: ", media)


#6- Construa um programa que receba uma valor inteiro maior que 2 em uma variavel x e apresenta os impares entre 0 e x

def questao6():

    #variável utilizada para conferir se o valor de entrada é maior que 2
    maiorQue2 = False

    #variável que temporariamente armazena um número entre 0 e o valor de entrada
    numero = 0

    #lista que armazena os valores ímpares
    impares = []

    while maiorQue2 == False: #enquanto não é digitado um valor maior que 2:

        #variavel que armazena o valor lido
        valor = int(input("Entre com um valor maior que 2: "))

        if valor <= 2: #verifica se o valor lido é maior que 2
            print("O valor deve ser maior que 2. Tente novamente.")
        else: #caso o valor seja maior que 2, sai do loop
            maiorQue2 = True

    while numero <= valor: #loop que verifica cada numero entre 0 e o valor lido

        if numero%2 != 0: #se o numero for impar ele é adicionado a lista
            impares.append(numero)
        
        #incremento da variavel, ou seja, passa para o próximo numero
        numero += 1
    
    #mostra na tela quais são os números impares
    print("Os valores ímpares entre {0} e 0 são: ".format(valor), impares)



# 7- Crie um programa que contêm uma função que receba dois parâmetros inteiros e retorna a média dos dois valores

def questao7():
    
    #cria uma função para calcular a média (assim como foi feito no exercício 2) e depois retorna o resultado
    def media():
        param1 = int(input("Entre com um valor inteiro: "))
        param2 = int(input("Entre com outro valor inteiro: "))
        media = (param1 + param2)/2
        return media

    #variavel que armazena o resultado do calculo da media
    resultado = media()
    print("A média dos múmeros é ", resultado)    


# 8- Crie um programa que lê 1 valor inteiro para X. Se o valor for par, calcular o fatorial de x em uma função e apresentar o resultado fora da função. Se o valor for impar, apresentar em uma função a tabuada de 1 a 10 de X.

def questao8():
    #armazena o valor lido
    X = int(input("entre com um valor inteiro: "))

    #função para calcular o fatorial de um número e retornar o resultado da operação
    def fatorial(valor):
        #variavel que armazena o resultado final e é incrementada a cada loop
        resultado = 1

        while valor != 0: #enquanto o valor for diferente de 0, a variável resultado é multiplicada por esse valor
            resultado *= valor

            #diminui 1 da variável valor, para que a cada loop a variavel seja multiplicada pelo número antecessor
            valor -= 1

        return resultado

    #função que apresenta a tabuada de 1 a 10 de X
    def tabuada(valor):
        #contador para realizar as multiplicações
        count = 1
        print("A tabuada de {0} é: ".format(X))

        while count <= 10: #entquanto a variavel contador nao chega em 10, realizamos a multiplicação entre o valor de entrada e essa variável
            resultado = count*valor
            
            #mostra na tela o resultado da multiplicação
            print("{0} x {0} = ".format(count, valor), resultado)

            #incrementa a variavel contador
            count += 1

    if X%2 == 0: #se X for par, a função para calcular o fatorial é chamada
        print("O resultado do cálculo fatorial de {0} é: ".format(X), fatorial(X))
    else: #caso X seja impar, chamamos a função de tabuada
        tabuada(X)                    


# 9- Crie um programa que recebe 15 valores e armazena em uma lista, e no final da execução mostre os valores da lista do ultimo para o primeiro

def questao9():
    #lista para armazenar os valores lidos
    lista = []

    #variavel contador
    count = 1

    while count <= 15: # enquanto o contador não atinge o limite
        #variavel que temporariamente armazena o valor lido
        valor = input("{0} - Entre com um valor: ".format(count))
        
        #adiciona o valor lido à lista
        lista.append(valor)

        #incrementa o contador
        count += 1

    #variavel que representa o index da lista (começando plea última posição)
    i = -1

    print("Os valores da lista do último para o primeiro são: ")

    while i >= -len(lista): #enquanto não chegamos ao primeiro eemento da lista, exibimos o elemento que corresponde ao index atual
        print(lista[i])

        #decremento do index
        i -= 1


# 10- Crie um programa que recebe uma lista com três frutas e compare com uma lista com os valores ["maça", "banana", "pera"]

def questao10():
    #lista para armazenar as frutas lidas
    listaRecebida = []
    #lista a ser comparada
    listaDeComparacao = ["maça", "banana", "pera"]
    #contador
    count = 0

    while count < 3: #enquanto não forem lidas 3 frutas, o usuário entra com uma fruta e esta é armazenada em listaRecebida 
        fruta = str(input("Entre com uma fruta: "))
        listaRecebida.append(fruta)
        count += 1
    
    #index
    i = 0

    while i < len(listaRecebida): #loop para analisar os valores de cada index dentro de listaRecebida

        if listaRecebida[i] in listaDeComparacao: #se a fruta do index atual se encontra na listaDeComparacao, mostramos essa fruta na tela
            print("A fruta {0} está na lista!".format(listaRecebida[i]))

        #incremento do index    
        i += 1


# 11- Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas. Entrada: A entrada contém dois valores inteiros representando a hora de início e a hora de fim do jogo. Saída: Apresente a duração do jogo conforme exemplo abaixo.

def questao11():
    #variavel que armazena a informação solicitada
    momentoJogo = str(input("O jogo começou e terminou no mesmo dia? (s/n): "))

    if momentoJogo == 's': #caso o jogo tenha sido realizado em um único dia
        
        #lemos a hora inicial e final do jogo
        inicio = int(input("Entre com a hora inicial (sem os minutos): "))
        final = int(input("Entre com a hora final (sem os minutos): "))

        #e determinamos a duração do jogo a partir da subtração entre a hora final e a hora inicial
        duracao = final - inicio

    else: #caso o jogo tenha sido concluido no dia seguinte

        #lemos a hora inicial e final do jogo
        inicio = int(input("Entre com a hora inicial (sem os minutos): "))
        final = int(input("Entre com a hora final (sem os minutos): "))

        #calculamos a o tempo gasto durante o primeiro dia
        tempoDia1 = 24 - inicio

        #e então somamos o tempo do primeiro dia com o do dia seguinte
        duracao = tempoDia1 + final
    
    if duracao > 24: #caso o jogo tenha durado mais de 24 horas, ele excedeu o tempo máximo
        print("O jogo durou {0} hora(s)".format(duracao))
        print("Esse jogo excede o limite de duração de 24 horas.")

    elif duracao < 1: #caso o jogo tenha durado menos de 1 hora, ele não chegou ao tempo mínimo
        print("O jogo durou {0} hora(s)".format(duracao))
        print("Esse jogo não chegou a ter o tempo de duração mínimo (1 hora).")   
        
    else: #caso a duração do jogo esteja entre 1 e 24 horas, ele se encontra dentro dos limites
        print("O jogo durou {0} hora(s)".format(duracao))



# 12 - Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias. Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

def questao12():
    dias = int(input("Entre com sua idade em dias: "))

    idadeAnos = dias//365
    diasSobrando = dias%365
    print(diasSobrando)
    idadeMeses = diasSobrando//30
    idadeDias = diasSobrando%30

    print("Sua idade é de:")
    print(idadeAnos, "ano(s)")
    print(idadeMeses, "mes(es)")
    print(idadeDias, "dia(s)")
    print("CORRIGIR ESSE EXERCICIO!!!!!!!!!!")

############# ÁREA DE EXECUÇÃO DOS EXERCÍCIOS #############

'''
print("Exercício 1:")
questao1()
print('\n')

print("Exercício 2:")
questao2()
print('\n')

print("Exercício 3:")
questao3()
print('\n')

print("Exercício 4:")
questao4()
print('\n')

print("Exercício 5:")
questao5()
print('\n')

print("Exercício 6:")
questao6()
print('\n')

print("Exercício 7:")
questao7()
print('\n')

print("Exercício 8:")
questao8()
print('\n')

print("Exercício 9:")
questao9()
print('\n')

print("Exercício 10:")
questao10()
print('\n')

print("Exercício 11:")
questao11()
print('\n')
'''
print("Exercício 12:")
questao12()