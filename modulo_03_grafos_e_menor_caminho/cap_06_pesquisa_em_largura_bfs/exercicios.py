"""
Módulo 3 - Capítulo 6: Exercícios de Fixação
Livro: Entendendo Algoritmos (Pesquisa em Largura - BFS e Grafos)
"""

# EXERCÍCIO 1 (Teórico):
# 1. Qual é a principal diferença entre uma Pilha (Stack - LIFO) e uma Fila (Queue - FIFO)?
# 2. Por que DEVEMOS usar uma Fila (FIFO) na Pesquisa em Largura em vez de uma Pilha? O que aconteceria se usássemos uma Pilha?
from collections import deque


RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui: Inicialmente a diferença ente pilha e fila é no manuseo dos dados. Enquanto a pilha realiza o Last in First out, onde
o último a entrar é o primeiro a sair a fila faz o First in First out, que é o contrário. No caso de usar a Fila em pesquisa de largura
é devido que queremos começar do início e ir montando a trilha, já com a Pilha o problema é que teriamos que montar a trilha e ir retirando de 
trás para frente. Diante disso iria gerar um O (n^2) e não um O (v + e).
"""


# EXERCÍCIO 2 (Teórico):
# Por que a complexidade de tempo da BFS é descrita como O(V + E), onde V é o número de Vértices e E é o número de Arestas?
# O que cada uma dessas partes representa na execução do algoritmo?
RESPOSTA_EXERCICIO_2 = """
Sua resposta aqui: No caso a complexidade do BFS é descrita pelo O (v + e) devido que v são as vertices que você visita, no máximo uma vez.
Por exemplo no dicionário a chave é o identificador único. No caso da aresta, são os nós adjacentes em listas que temos que passar
até chegar no fim da lista. Além disso, podemos usar O (V) para armazenar as interações de itens a serem visitados e os que já foram visitados.
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
    
    # Idealmente aqui poderiamos adicionar uma defesa pra vertices que não existem no grafo
    # exemplo o G, poderiamos fazer um inicio/destino not in grafo, assim não adariamos no grafo todo
    # evitando o alto valor em O (V + E)
    if inicio not in grafo or destino not in grafo:
        return -1
    
    fila = deque([(inicio, 0)])
    visitados = {inicio}
    
    while fila:
        no_atual, distancia = fila.popleft()
        if no_atual == destino:
            return distancia
        
        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, distancia + 1)) 
    
    return -1


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
