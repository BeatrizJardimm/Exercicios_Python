#importando a biblioteca para manipular JSON
import json

# 1- Baixe o arquivo do link JSON 1, abra ele no vsCode com Python nomeando-o como partida guarde em uma variável e printe o JSON inteiro no terminal.

abreJson = open('./json/partidaJSON.json', encoding="utf-8") #abrindo o arquivo no código
partida = json.load(abreJson) #transformando o arquivo em um json compreensível
#Abrimos o arquivo fora da função para que ele possa ser usado nos outros exercícios

def questao1():
    return partida #mostra o arquivo no terminal


# 2- Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal.

# variável que armazena o caminho para acessar qualquer objeto do arquivo JSON,
# agora, em vez de digitar esse caminho toda vez, precisamos apenas chamar a variável e o objeto desejado
caminho_objetos = partida["copa-do-brasil"][0]
# ATENÇÃO: essa variável será utilizada em todos os exercícios, não só na questão 2.

def questao2():

    ##resposta completa (confere qual dos dois times teve o maior placar ou se teve empate):
    if caminho_objetos["placar_mandante"] > caminho_objetos["placar_visitante"]:
        resultado = caminho_objetos["time_mandante"]["nome_popular"]
    elif caminho_objetos["placar_visitante"] > caminho_objetos["placar_mandante"]:
        resultado = caminho_objetos["time_visitante"]["nome_popular"]
    else:
        resultado = "Empate"
    
    return resultado #a função retorna o valor da variável resultado
    
## a resposta objetiva seria:
# print(caminho_objetos["time_mandante"]["nome_popular"])         


# 3- Do JSON 1 Guarde apenas o Nome do Estádio, o Placar e o Status do jogo dentro de variáveis e mostre-as.

def questao3():
    #busca o nome do estadio no arquivo JSON e guarda o valor nessa variavel
    nome_estadio = caminho_objetos["estadio"]["nome_popular"]
    placar = caminho_objetos["placar"] #busca o placar no arquivo e armazena
    status_jogo = caminho_objetos["status"] #busca o status do jogo e guarda

    print("Nome do estádio: ", nome_estadio) #mostra o nome do estadio na tela
    print("Placar do jogo: ", placar) #mostra o placar do jogo na tela
    print("Status da partida: ", status_jogo) #mostra o status da partida na tela

    return '' #criando um retorno vazio para a função não retornar "None"


# 4- No JSON 1 printe todas as chaves e valores do time visitante

def questao4():
    #busca o objeto "time_visitante" no arquivo JSON e armazena na variável
    visitante = caminho_objetos["time_visitante"]
    return visitante #retorna o valor da variavel para ser mostrado na tela

########## ÁREA DE EXECUÇÃO DOS EXERCÍCIOS ##########

print("Exercício 1:")
print(questao1())
print('\n')

print("Exercício 2:")
print(questao2())
print('\n')

print("Exercício 3:")
print(questao3())
print('\n')

print("Exercício 4:")
print(questao4())