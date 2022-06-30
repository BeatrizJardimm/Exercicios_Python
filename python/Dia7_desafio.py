'''
Desafio final de leitura de dados em CSV e JSON:

1- Em Python crie uma aplicação que mostre elementos específicos em uma tabela periódica:
2- A aplicação deve ter no mínimo 15 elementos da tabela periódica, não precisa ser todos pois são muitos, escolha os que você quiser.
3- Crie um CSV com um header contendo: Simbolo, Nome, NumeroAtomico, Linha, Coluna, EstadoFisico.
4- E adicione abaixo nas colunas os respectivos dados retirados do seguinte site: https://ptable.com/#Propriedades
Exemplo:
Simbolo, Nome, NumeroAtomico, Linha, Coluna, EstadoFisico.
Cr, Cromio, 24, 4, 6, Solido

--> Para montar o arquivo, escolhi todos os elementos radioativos conhecidos
--> Uma lista desses elementos pode ser encontrada em: https://brasilescola.uol.com.br/quimica/elementos-radioativos.htm
'''

#importando a biblioteca Pandas
import pandas as pd

#usa pandas para ler o arquivo csv, especificando qual é o separador dos objetos
elementos = pd.read_csv("./csv/elementosRadioativos.csv", encoding="utf-8", sep=',')

#A) Crie uma “aplicação” em loop que tenha uma opção para listar todos os elementos da tabela, porém mostrando apenas uma propriedade do elemento. Ex: listar todos os nomes dos elementos na tabela.

def questaoA():

    #variavel para entrar/sair do loop
    loop = True

    while loop: #enquanto loop for igual a True

        #mostra as opções do menu na tela
        print("Bem-vindo à minha lista de elementos radioativos!!!")
        print("Escolha uma das propriedades abaixo para mostrar seu valor em todos os elementos da tabela:")
        print("1 - Símbolo")
        print("2 - Nome")
        print("3 - Número Atômico")
        print("4 - Linha")
        print("5 - Coluna")
        print("6 - Estado Físico")
        print("7 - Sair da aplicação")
        #variavel para guardar o valor de entrada (índice do menu)
        propriedade = int(input("Entre com um índice válido: "))

        #match-case para lidar com cada opção de entrada
        match propriedade:
            case 1: #listar os símbolos
                print(elementos.loc[:, "Simbolo"])
            case 2: #listar os nomes
                print(elementos.loc[:, "Nome"])
            case 3: #listar os números atômicos
                print(elementos.loc[:, "NumeroAtomico"])
            case 4: #listar as linhas
                print(elementos.loc[:, "Linha"])
            case 5: #listar as colunas
                print(elementos.loc[:, "Coluna"])
            case 6: #listar os estados físicos
                print(elementos.loc[:, "EstadoFisico"])
            case 7: #sair do loop
                print("Até mais :)")    
                loop = False #seta a variável loop para False e entao sai do loop


#B) Listar todos os dados de determinado elemento, buscando através do seu símbolo.

def questaoB():

    #variável para armazenar o valor de entrada
    simbolo = str(input("Entre com o símbolo de um dos elementos (em letras maiúsculas): "))

    print(elementos.loc[:, "Simbolo"])

    #variavel que armazena todos os dados da linha que apresenta o símbolo correspondente ao que foi digitado pelo usuário
    if simbolo in list(elementos.loc[:, "Simbolo"]):
        dados = elementos[elementos["Simbolo"] == simbolo]
        print(dados) #mostra os dados do elemento na tela
    else:
        print("Este não é um símbolo válido")


#C) Listar todos os dados de todos os elementos inseridos.

def questaoC():
    # criei um input antes de listar os dados apenas com o intuito de não listá-los "de cara"
    # esse input não é utilizado posteriormente
    input("Digite qualquer tecla para listar todos os elementos e suas características: ")
    
    print(elementos) #mostra os dados de todos os elementos na tela

########## ÁREA DE EXECUÇÃO DOS EXERCÍCIOS ##########

print("Questão A: ")
questaoA()
print('\n')

print("Questão B: ")
questaoB()
print('\n')

print("Questão C: ")
questaoC()
<<<<<<< HEAD
print('\n')
=======
print('\n')
>>>>>>> db9c46f8acc9bf0d32f33bfc9f1674fc4cd963a8
