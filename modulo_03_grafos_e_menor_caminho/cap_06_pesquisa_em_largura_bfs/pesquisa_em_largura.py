"""
Módulo 3 - Capítulo 6: Pesquisa em Largura (Breadth-First Search - BFS) e Grafos
Livro: Entendendo Algoritmos (Aditya Y. Bhargava)
"""

from collections import deque

# =====================================================================
# 1. REPRESENTAÇÃO DE GRAFOS COM TABELAS HASH (LISTAS DE ADJACÊNCIA)
# =====================================================================
# Um grafo é composto por Vértices (nós) e Arestas (conexões).
# Em Python, representamos grafos usando um dicionário onde:
# - Chave: Nome do nó
# - Valor: Lista de vizinhos diretamente conectados (arestas que saem dele)

# Grafo da rede de amigos do livro: procurando um "vendedor de mangas"
# Convenção do livro: se o nome terminar com a letra 'm', a pessoa é vendedora de mangas!
grafo_amigos = {
    "voce": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
}


# =====================================================================
# 2. FUNÇÃO AUXILIAR DE CRITÉRIO DE BUSCA
# =====================================================================
def pessoa_e_vendedora(nome: str) -> bool:
    """Regra do livro: vendedores de manga têm nomes que terminam com 'm'."""
    return nome.endswith("m")


# =====================================================================
# 3. ALGORITMO BFS (PESQUISA EM LARGURA)
# =====================================================================
# A BFS responde a duas perguntas cruciais:
# 1. Existe um caminho do ponto A até o ponto B?
# 2. Qual é o caminho mais curto (menor número de conexões/arestas)?
#
# Para isso, usa uma FILA (Queue - FIFO: First In, First Out)
# e um CONJUNTO (Set) para evitar visitar nós duplicados (evita loops infinitos).


def pesquisa_em_largura(grafo: dict[str, list[str]], inicio: str) -> str | None:
    """
    Executa a BFS a partir de um nó inicial procurando pelo primeiro vendedor de mangas.
    Retorna o nome da pessoa encontrada ou None.
    Complexidade de Tempo: O(V + E) onde V = Vértices e E = Arestas.
    """
    fila_busca = deque()
    # Adiciona os vizinhos de 1º grau na fila
    fila_busca.extend(grafo.get(inicio, []))

    # Conjunto para rastrear quem já foi verificado (evita ciclos e retrabalho)
    verificados = set()

    print(f"Iniciando busca BFS a partir de: '{inicio}'")

    while fila_busca:
        pessoa = fila_busca.popleft()  # Remove o primeiro da fila (FIFO)

        if pessoa not in verificados:
            print(f"-> Verificando: {pessoa}...")
            if pessoa_e_vendedora(pessoa):
                print(f"🎉 Encontrado! {pessoa} é um(a) vendedor(a) de mangas!")
                return pessoa
            else:
                # Adiciona todos os amigos dessa pessoa no final da fila (vizinhos de próximo grau)
                fila_busca.extend(grafo.get(pessoa, []))
                verificados.add(pessoa)

    print("Nenhum vendedor de mangas encontrado na rede.")
    return None


# =====================================================================
# 4. BFS COM RASTREAMENTO DO MENOR CAMINHO (SHORTEST PATH)
# =====================================================================
def menor_caminho_bfs(
    grafo: dict[str, list[str]], inicio: str, destino: str
) -> list[str] | None:
    """
    Encontra e retorna o caminho com MENOR NÚMERO DE PASSOS entre início e destino.
    Guarda o caminho percorrido até cada nó dentro da fila.
    """
    fila = deque([[inicio]])
    visitados = {inicio}

    while fila:
        caminho_atual = fila.popleft()
        no_atual = caminho_atual[-1]

        if no_atual == destino:
            return caminho_atual

        for vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                novo_caminho = list(caminho_atual)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)

    return None


if __name__ == "__main__":
    print("=" * 60)
    print("1. Busca do Vendedor de Mangas mais próximo (BFS)")
    print("=" * 60)
    resultado = pesquisa_em_largura(grafo_amigos, "voce")
    print(f"Resultado final: {resultado}\n")

    print("=" * 60)
    print("2. Menor Caminho entre dois nós ('voce' até 'thom')")
    print("=" * 60)
    caminho = menor_caminho_bfs(grafo_amigos, "voce", "thom")
    print(
        f"Menor rota ({len(caminho) - 1} passos): {' -> '.join(caminho) if caminho else 'Sem caminho'}"
    )
