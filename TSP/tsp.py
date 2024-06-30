import time
import heapq
import os
import sys


def custo_caminho(caminho, grafo):
    custo = 0
    for i in range(len(caminho) - 1):
        custo += grafo[caminho[i]][caminho[i + 1]]
    custo += grafo[caminho[-1]][caminho[0]]
    return custo


def prim_mst(grafo):
    num_vertices = len(grafo)
    arestas_mst = []
    visitados = [False] * num_vertices
    heap_minimo = [(0, 0, -1)]
    while heap_minimo:
        custo, vertice, pai = heapq.heappop(heap_minimo)
        if visitados[vertice]:
            continue
        visitados[vertice] = True
        if pai != -1:
            arestas_mst.append((pai, vertice))
        for vizinho in range(num_vertices):
            if not visitados[vizinho] and grafo[vertice][vizinho] != 0:
                heapq.heappush(heap_minimo, (grafo[vertice][vizinho], vizinho, vertice))
    return arestas_mst


def caminho_preordem(arestas_mst, vertice_inicial=0):
    from collections import defaultdict
    arvore = defaultdict(list)
    for u, v in arestas_mst:
        arvore[u].append(v)
        arvore[v].append(u)
    lista_preordem = []
    visitados = set()

    def dfs(vertice):
        visitados.add(vertice)
        lista_preordem.append(vertice)
        for vizinho in arvore[vertice]:
            if vizinho not in visitados:
                dfs(vizinho)

    dfs(vertice_inicial)
    return lista_preordem


def tornar_hamiltoniano(percurso_preordem):
    visitados = set()
    caminho_hamiltoniano = []
    for vertice in percurso_preordem:
        if vertice not in visitados:
            visitados.add(vertice)
            caminho_hamiltoniano.append(vertice)
    caminho_hamiltoniano.append(caminho_hamiltoniano[0])
    return caminho_hamiltoniano


def aprox_tsp_mst(grafo):
    mst = prim_mst(grafo)
    percurso_pre = caminho_preordem(mst)
    ciclo_hamiltoniano = tornar_hamiltoniano(percurso_pre)
    return ciclo_hamiltoniano, custo_caminho(ciclo_hamiltoniano, grafo)


def carregar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()
        grafo = [list(map(int, linha.split())) for linha in linhas]
    return grafo


def valor_otimo(nome_arquivo):
    valor = int(nome_arquivo.split('_')[1].split('.')[0])
    return valor


def main_mst(caminho_arquivo):
    grafo = carregar_arquivo(caminho_arquivo)
    valor = valor_otimo(os.path.basename(caminho_arquivo))

    start = time.time()
    caminho_aproximado, custo_aproximado = aprox_tsp_mst(grafo)
    tempo_execucao = time.time() - start

    print("Arquivo: {}".format(caminho_arquivo))
    print("Valor Ótimo: {}".format(valor))
    print("Algoritmo Aproximativo:")
    print("Caminho: {}".format(caminho_aproximado))
    print("Custo: {}".format(custo_aproximado))
    print("Tempo de Execução: {:.4f} segundos".format(tempo_execucao))

    print()


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)

    example_files = [
        'tsp1_253.txt', 
        'tsp2_1248.txt', 
        'tsp3_1194.txt', 
        'tsp4_7013.txt',
        'tsp5_27603.txt'
    ]

    sys.setrecursionlimit(10000)

    for file in example_files:
        absolute_path = os.path.join(script_dir, file)
        print("\nComeçou a rodar o exemplo para o arquivo:")
        main_mst(absolute_path)
