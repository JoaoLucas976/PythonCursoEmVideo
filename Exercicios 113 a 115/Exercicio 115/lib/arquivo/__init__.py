import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho("PESSOAS CADASTRADAS")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<34}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome="Desconhecido", idade=0):
    try:
        a = open(arq, 'at')
    except:
        print("Houve um erro na abertura do arquivo")
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print("Houve um erro no cadastro")
        else:
            print("Nome cadastrado com sucesso")
        finally:
            a.close()