import csv
import os #importa o módulo que possui funções para lidar com caminhos de arquivo e sistema operacional


def ler_csv():    
    base_dir = os.path.dirname(__file__) # pega a pasta que o arquivo leitor_csv está localizado

    caminho_arquivo = os.path.join(
        base_dir,
        "Indices-e-Estatisticas-Hidrometeorologicas-Estacao-Pluviometrica.csv"
    ) #Junta o caminho do arquivo com os dados atribuidos, garantindo que não tenha erro

    dados = []
    with open(caminho_arquivo, newline="", encoding="utf-8") as f:
        #abra o arquivo csv enquanto houver conteudo para ser lido
        # newline ="" -> ajuda a evitar problemas com quebras de linha
        # encoding -> define a codificação, caracteres acentuados
        leitor = csv.reader(f)
        #   Cria um objeto reader que itera sobre as linhas do CSV já separadas em colunas

        for linha in leitor:
            dados.append(linha)
    return dados

