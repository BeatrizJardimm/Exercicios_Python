import pandas as pd
import json

'''
############ JSON 1 ############ 
# 1- Baixe o arquivo do link JSON 1, abra ele no vsCode com Python nomeando-o como partida guarde em uma variável e printe o JSON inteiro no terminal.

abreJson = open('json1.json', encoding="utf-8") #abrindo o arquivo no código
partida = json.load(abreJson) #transformando o arquivo em um json compreensível

print(partida)

# 2- Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal.
#resposta objetiva:
print(partida["copa-do-brasil"][0]["time_mandante"]["nome_popular"])

#resposta completa
if partida["copa-do-brasil"][0]["placar_mandante"] > partida["copa-do-brasil"][0]["placar_visitante"]:
    print(partida["copa-do-brasil"][0]["time_mandante"]["nome_popular"])
elif partida["copa-do-brasil"][0]["placar_visitante"] > partida["copa-do-brasil"][0]["placar_mandante"]:
    print(partida["copa-do-brasil"][0]["time_visitante"]["nome_popular"])
else:
    print("Empate")    

# 3- Do JSON 1 Guarde apenas o Nome do Estádio, o Placar e o Status do jogo dentro de variáveis e mostre-as.
nome_estadio = partida["copa-do-brasil"][0]["estadio"]["nome_popular"]
placar = partida["copa-do-brasil"][0]["placar"]
status_jogo = partida["copa-do-brasil"][0]["status"]

print("Nome do estádio: ", nome_estadio)
print("Placar do jogo: ", placar)
print("Status da partida: ", status_jogo)

# 4- No JSON 1 printe todas as chaves e valores do time visitante

visitante = partida["copa-do-brasil"][0]["time_visitante"]
print(visitante)

############ JSON 2 ############
# 5- Guarde o arquivo JSON 2 nomeando-o como campeonato em uma variável e printe todos os seus dados.

abreJson = open('json2.json', encoding="utf-8") #abrindo o arquivo no código
campeonato = json.load(abreJson) #transformando o arquivo em um json compreensível

print(campeonato)

# 6- Faça com que o programa printe apenas os primeiros dados dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.

edicao = campeonato["edicao_atual"]["edicao_id"]
fase = campeonato["fase_atual"]["fase_id"]
rodada = campeonato["rodada_atual"]["nome"]

print("ID da edição atual: ",edicao)
print("ID da fase atual: ", fase)
print("Rodada atual: ", rodada)

# 7- Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

for i in campeonato:
    print(i)
'''

############ CSV ############
# 8- Abra o arquivo CSV com pandas e guarde em uma variável de sua escolha e printe o conteúdo no terminal

premiados = pd.read_csv("csv1.csv", encoding="utf-8", sep=',')

#print(premiados)

# 9- Usando Pandas, leia apenas os dados da coluna Age do CSV.

idades = pd.read_csv("csv1.csv", encoding="utf-8", sep=',', usecols=["Age"])

#print(idades)

# 10- Usando Pandas, procure por um dado específico (da sua escolha) e printe somente o mesmo utilizando o CSV.

#Printar o nome do filme estrelado por Tom Hanks em 1995 (Forrest Gump)

titulo_filme = premiados.loc[67, "Movie"]
#print(titulo_filme)

# 11- Printe o nome do Ator que ganhou o Oscar em 1993.

vencedor93 = premiados.loc[premiados["Year"] == 1993]
#print("Ator que venceu o Oscar em 1993: ", '\n', vencedor93.loc[:, 'Name'])

# 12- Printe somente o nome dos atores que ganharam o Oscar em 1991 e 2016.

vencedores = premiados[(premiados["Year"] == 1991) | (premiados["Year"] == 2016)]
#print("Atores:", '\n', vencedores.loc[:, "Name"])

# 13- Crie mais uma coluna em tempo de execução juntando os dados movie e year.
############### ERRO #################

str_anos = str(premiados.loc[:, "Year"])

premiados["Filmes"] = premiados["Movie"] + ' ' + str_anos
print(premiados["Filmes"].head())

# 14- Printe todos os nomes e as idades dos atores que ganharam o oscar de 1987 até 1999.

vencedores87_99 = premiados[(premiados["Year"] >= 1987) & (premiados["Year"] <= 1999)]
#print(vencedores87_99.loc[:, ["Name", "Age"]])

# 15- Mostre todos os filmes menos o “The Revenant”.

todos = premiados[premiados["Movie"] != "The Revenant"]
#print(todos["Movie"])