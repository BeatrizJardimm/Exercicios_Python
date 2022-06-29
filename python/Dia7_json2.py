#importando a biblioteca para manipular JSON
import json

# 5- Guarde o arquivo JSON 2 nomeando-o como campeonato em uma variável e printe todos os seus dados.

abreJson = open('./json/campeonatoJSON.json', encoding="utf-8") #abrindo o arquivo no código
campeonato = json.load(abreJson) #transformando o arquivo em um json compreensível
#Abrimos o arquivo fora da função para que ele possa ser usado nos outros exercícios

def questao5():
    return campeonato #retorna o arquivo inteiro


# 6- Faça com que o programa printe apenas os primeiros dados dentro de edicao_atual, fase_atual, rodada_atual usando o JSON 2.

def questao6():
    edicao = campeonato["edicao_atual"]["edicao_id"] #busca o objeto "edicao_id" no arquivo JSON e armazena na variavel
    fase = campeonato["fase_atual"]["fase_id"] #busca o objeto "fase_id" no arquivo JSON e armazena na variavel
    rodada = campeonato["rodada_atual"]["nome"] #busca o objeto "nome" no arquivo JSON e armazena na variavel

    print("ID da edição atual: ",edicao) #mostra a id da edição na tela
    print("ID da fase atual: ", fase) #mostra a id da fase na tela
    print("Rodada atual: ", rodada) #mostra qual é a rodada atual

    return '' #criando um retorno vazio para a função não retornar "None"


# 7- Percorra o JSON 2, utilizando o loop FOR e printe suas chaves principais.

def questao7():
    for i in campeonato: #para cada chave principal no arquivo JSON, 
        print(i)         #mostrar a chave na tela

    return '' #criando um retorno vazio para a função não retornar "None"

########## ÁREA DE EXECUÇÃO DOS EXERCÍCIOS ##########

print("Exercício 5:")
print(questao5())
print('\n')

print("Exercício 6:")
print(questao6())
print('\n')

print("Exercício 7:")
print(questao7())