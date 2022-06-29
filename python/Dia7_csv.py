#importando a biblioteca Pandas
import pandas as pd

# 8- Abra o arquivo CSV com pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal

#usa pandas para ler o arquivo csv, especificando qual é o separador dos objetos
premiados = pd.read_csv("./csv/filmesCSV.csv", encoding="utf-8", sep=',')
#Abrimos o arquivo fora da função para que ele possa ser usado nos outros exercícios

def questao8():
    return premiados #retorna o arquivo inteiro


# 9- Usando Pandas, leia apenas os dados da coluna Age do CSV.

def questao9():
    #usa pandas para ler o arquivo csv, especificando qual é o separador dos objetos e a coluna que queremos que seja lida
    idades = pd.read_csv("./csv/filmesCSV.csv", encoding="utf-8", sep=',', usecols=["Age"])
    return idades #retorna os valores dessa coluna em todas as linhas


# 10- Usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.
## Printar o nome do filme estrelado por Tom Hanks em 1995 (Forrest Gump)

def questao10():
    #busca o nome do filme com base no índice da linha e a coluna na qual esse elemento se encontra
    titulo_filme = premiados.loc[67, "Movie"]
    return titulo_filme #retorna o dado localizado


# 11- Printe o nome do Ator que ganhou o Oscar em 1993.

def questao11():
    #busca o nome do ator com base nos valores da coluna "Year" e quando encontra o valor 1993, armazena os dados dessa linha na variavel vencedor93
    vencedor93 = premiados[premiados["Year"] == 1993]
    nomeVencedor = vencedor93.loc[:, 'Name'] #localiza o nome do vencedor dentro da variavel vencedor93 com base na coluna "Name"
    print("Ator que venceu o Oscar em 1993: ", '\n', nomeVencedor) #mostra o nome do vencedor na tela

    return '' #criando um retorno vazio para a função não retornar "None"


# 12- Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

def questao12():
    #busca os nomes com base na coluna "Year" e armazena os dados das linhas onde o valor dessa coluna é 1991 ou 2016
    vencedores = premiados[(premiados["Year"] == 1991) | (premiados["Year"] == 2016)]
    nomesVencedores = vencedores.loc[:, "Name"] #localiza apenas os nomes entre as linhas da variavel "vencedores" com base na coluna "Name"
    print("Atores:", '\n', nomesVencedores) #mostra esses nomes na tela

    return '' #criando um retorno vazio para a função não retornar "None"


# 13- Crie mais uma coluna em tempo de execução juntando os dados movie e year.
############### ERRO #################

def questao13():

    #ao referenciar uma coluna que não existe, ela é criada automaticamente
    # #como não é possível concatenar valores de tipos diferentes, precisamos transformar os anos, que são inteiros, em strings    
    premiados["Filmes"] = premiados["Movie"] + '- {0}'.format(premiados["Year"])

    return premiados.head() #retorna apenas as primeiras linhas

#não sei por que a formatação está ficando bugada

# 14- Printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.

def questao14():
    #busca com base na coluna "Year" e armazena os dados das linhas onde o valor dessa coluna está entre 1987 e 1999
    vencedores87_99 = premiados[(premiados["Year"] >= 1987) & (premiados["Year"] <= 1999)]
    #pega todas as linhas, localiza o nome a idade de cada vencedor com base em suas respectivas colunas e retorna esses dados
    return vencedores87_99.loc[:, ["Name", "Age"]]


# 15- Mostre todos os filmes menos o “The Revenant”.

def questao15():
    #busca com base na coluna "Movie" e armazena na variável todas as linhas onde o valor dessa coluna não é "The Revenant"
    todos = premiados[premiados["Movie"] != "The Revenant"]
    return todos.loc[:, "Movie"] #localiza o valor da coluna "Movie" em cada linha e retorna esses valores


########## ÁREA DE EXECUÇÃO DOS EXERCÍCIOS ##########

print("Exercício 8:")
print(questao8())
print('\n')

print("Exercício 9:")
print(questao9())
print('\n')

print("Exercício 10:")
print(questao10())
print('\n')

print("Exercício 11:")
print(questao11())
print('\n')

print("Exercício 12:")
print(questao12())
print('\n')

print("Exercício 13:")
print(questao13())
print('\n')


print("Exercício 14:")
print(questao14())
print('\n')

print("Exercício 15:")
print(questao15())