'''
-----------------------------------------------------------------------------------------

Desafio final de leitura de dados em CSV e JSON:

- Em Python crie uma aplicação que mostre elementos específicos em uma tabela periódica:

A aplicação deve ter no mínimo 15 elementos da tabela periódica, não precisa ser todos pois são muitos, escolha os que você quiser.

Elementos Actinídeos

89 - actínio (Ac)
90 - tório (Th)
91 - protactínio (Pa)
92 - urânio (U)
93 - netúnio (Np)
94 - plutônio (Pu)
95 - amerício (Am)
96 - cúrio (Cm)
97 - berquélio (Bk)
98 - califórnio (Cf)
99 - einstéinio (Es)
100 - férmio (Fm)
101 - mendelévio (Md)
102 - nobélio (No)
103 - laurêncio (Lr)

Crie um CSV com um header contendo:

Simbolo, Nome, NumeroAtomico, Linha, Coluna, EstadoFisico.

E adicione abaixo nas colunas os respectivos dados retirados do seguinte site: https://ptable.com/#Propriedades

Exemplo:

Simbolo, Nome, NumeroAtomico, Linha, Coluna, EstadoFisico.

Cr, Cromio, 24, 4, 6, Solido

Faça isso com no mínimo 15 elementos, aí já terá o CSV pronto para manipular.
'''

import pandas as pd

elementos = pd.read_csv("elementosActinideos.csv", encoding="utf-8", sep=',')

#A) Crie uma “aplicação” em loop que tenha uma opção para listar todos os elementos da tabela, porém mostrando apenas uma propriedade do elemento. Ex: listar todos os nomes dos elementos na tabela.

def questaoA():

    loop = True

    while loop:
        print("Bem-vindo à minha lista de elementos radioativos!!!")
        print("Escolha uma das propriedades abaixo para mostrar seu valor em todos os elementos da tabela:")
        print("1 - Símbolo")
        print("2 - Nome")
        print("3 - Número Atômico")
        print("4 - Linha")
        print("5 - Coluna")
        print("6 - Estado Físico")
        print("7 - Sair da aplicação")
        propriedade = int(input("Entrada: "))

        match propriedade:
            case 1:
                print(elementos.loc[:, "Simbolo"])
            case 2:
                print(elementos.loc[:, "Nome"])
            case 3:
                print(elementos.loc[:, "NumeroAtomico"])
            case 4:
                print(elementos.loc[:, "Linha"])
            case 5:
                print(elementos.loc[:, "Coluna"])
            case 6:
                print(elementos.loc[:, "EstadoFisico"])
            case 7:
                print("Até mais :)")
                loop = False

#B) Listar todos os dados de determinado elemento, buscando através do seu símbolo.

def questaoB():

    simbolo = str(input("Entre com o símbolo de um dos elementos: "))

    dados = elementos[elementos["Simbolo"] == simbolo]
    print(dados)

#C) Listar todos os dados de todos os elementos inseridos.

def questaoC():
    input("Digite qualquer tecla para listar todos os elementos e suas características: ")
    print(elementos)

########## ÁREA DE EXECUÇÃO DOS EXERCÍCIOS ##########

print("Questão A: ")
questaoA()
print('\n')

print("Questão B: ")
questaoB()
print('\n')

print("Questão C: ")
questaoC()
print('\n')