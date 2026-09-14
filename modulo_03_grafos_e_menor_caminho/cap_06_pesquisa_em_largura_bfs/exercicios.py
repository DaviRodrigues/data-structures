"""
Módulo 3 - Capítulo 6: Exercícios de Fixação
Livro: Entendendo Algoritmos (Pesquisa em Largura - BFS e Grafos)
"""

# EXERCÍCIO 1 (Teórico):
# 1. Qual é a principal diferença entre uma Pilha (Stack - LIFO) e uma Fila (Queue - FIFO)?
# 2. Por que DEVEMOS usar uma Fila (FIFO) na Pesquisa em Largura em vez de uma Pilha? O que aconteceria se usássemos uma Pilha?
RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui: 
"""


# EXERCÍCIO 2 (Teórico):
# Por que a complexidade de tempo da BFS é descrita como O(V + E), onde V é o número de Vértices e E é o número de Arestas?
# O que cada uma dessas partes representa na execução do algoritmo?
RESPOSTA_EXERCICIO_2 = """
Sua resposta aqui: 
"""


# EXERCÍCIO 3 (DESAFIO DE CÓDIGO - Contagem de Passos / Menor Rota em Rede Social):
# Implemente a função `distancia_minima(grafo, inicio, destino)` que retorna o NÚMERO MÍNIMO DE CONEXÕES (arestas)
# necessárias para ir de `inicio` até `destino`.
# Se `inicio == destino`, a distância é 0.
# Se não houver caminho possível, retorne -1.
#
# Exemplo:
# rede = {
#     "A": ["B", "C"],
#     "B": ["D"],
#     "C": ["E"],
#     "D": ["F"],
#     "E": ["F"],
#     "F": []
# }
# distancia_minima(rede, "A", "F") -> Deve retornar 3 (A -> B -> D -> F ou A -> C -> E -> F)
# distancia_minima(rede, "A", "Z") -> Deve retornar -1 (destino inalcançável)
def distancia_minima(grafo: dict[str, list[str]], inicio: str, destino: str) -> int:
    # TODO: Implemente a busca BFS mantendo o controle da distância (profundidade de passos)
    pass


if __name__ == "__main__":
    rede_teste = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["E"],
        "D": ["F"],
        "E": ["F"],
        "F": [],
        "G": [],
    }

    print(f"Distância A -> F: {distancia_minima(rede_teste, 'A', 'F')} (Esperado: 3)")
    print(f"Distância A -> A: {distancia_minima(rede_teste, 'A', 'A')} (Esperado: 0)")
    print(f"Distância A -> B: {distancia_minima(rede_teste, 'A', 'B')} (Esperado: 1)")
    print(f"Distância A -> G: {distancia_minima(rede_teste, 'A', 'G')} (Esperado: -1)")
