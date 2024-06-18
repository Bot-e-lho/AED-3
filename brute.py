import os
import time
from itertools import permutations


def carregar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()
        grafo = [list(map(int, linha.split())) for linha in linhas]
    return grafo


def custo_caminho(caminho, grafo):
    custo = 0
    for i in range(len(caminho) - 1):
        custo += grafo[caminho[i]][caminho[i + 1]]
    custo += grafo[caminho[-1]][caminho[0]]
    return custo


def valor_otimo(nome_arquivo):
    valor = int(nome_arquivo.split('_')[1].split('.')[0])
    return valor


def forca_bruta_tsp(grafo):
    num_vertices = len(grafo)
    todos_caminhos = permutations(range(num_vertices))
    menor_custo = float('inf')
    melhor_caminho = None
    for caminho in todos_caminhos:
        custo_atual = custo_caminho(caminho, grafo)
        if custo_atual < menor_custo:
            menor_custo = custo_atual
            melhor_caminho = caminho
    return melhor_caminho, menor_custo


def resolver_instancia_brute(caminho_arquivo):
    grafo = carregar_arquivo(caminho_arquivo)
    valor = valor_otimo(os.path.basename(caminho_arquivo))

    start = time.time()
    caminho, custo = forca_bruta_tsp(grafo)
    tempo_execucao = time.time() - start

    print("Arquivo: {}".format(caminho_arquivo))
    print("Valor Ótimo: {}".format(valor))
    print("Algoritmo de Força Bruta:")
    print("Caminho: {}".format(caminho))
    print("Custo: {}".format(custo))
    print("Tempo de Execução: {:.4f} segundos".format(tempo_execucao))

    print()


example_files = ['tsp1_253.txt', 'tsp2_1248.txt', 'tsp3_1194.txt', 'tsp4_7013.txt', 'tsp5_27603.txt']
for file in example_files:
    resolver_instancia_brute(file)
