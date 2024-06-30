import itertools
import time
import sys

def carregar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()
        grafo = [list(map(int, linha.split())) for linha in linhas]
    return grafo

def brute_force_tsp(graph, start_v=0):
    num_vertices = len(graph)
    vertices = list(range(num_vertices))
    vertices.remove(start_v)
    
    min_path_cost = float('inf')
    min_path = []

    for permutation in itertools.permutations(vertices):
        current_path_cost = 0
        k = start_v
        
        for vertex in permutation:
            current_path_cost += graph[k][vertex]
            k = vertex
        
        current_path_cost += graph[k][start_v]

        if current_path_cost < min_path_cost:
            min_path_cost = current_path_cost
            min_path = (start_v,) + permutation + (start_v,)

    return min_path, min_path_cost

def main_brute(caminho_arquivo):
    graph = carregar_arquivo(caminho_arquivo)

    start_time = time.time()
    path, cost = brute_force_tsp(graph)
    execution_time = time.time() - start_time

    print("Algoritmo de Força Bruta:")
    print(f"Caminho: {path}")
    print(f"Custo Total: {cost}")
    print(f"Tempo de Execução: {execution_time:.10f} segundos")
    print(f"Arquivo: {caminho_arquivo}")

if __name__ == "__main__":
    example_files = [
        'tsp1_253.txt', 
        'tsp2_1248.txt', 
        'tsp3_1194.txt', 
        'tsp4_7013.txt'
    ]

    sys.setrecursionlimit(10000)

    for file in example_files:
        print("\nComeçou a rodar o exemplo para o arquivo:")
        main_brute(file)
