from ex115.lib.interface import *


def arquivo_existe(nome):
        try:
            a = open(nome, 'rt')  # rt significa abrir para read e text - abrir para leitura em modo texto
            a.close()
        except FileNotFoundError:
            return False
        else:
            return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')  # wt+ significa: escreve um arquivo de texto - e o '+' significa que caso o arquivo não exista, ele cria
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')  # 'a' significa append... para inserir dados no arquivo
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
