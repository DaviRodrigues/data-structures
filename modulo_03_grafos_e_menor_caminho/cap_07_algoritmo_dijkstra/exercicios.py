"""
Módulo 3 - Capítulo 7: Exercícios de Fixação
Livro: Entendendo Algoritmos (Algoritmo de Dijkstra)
"""

# EXERCÍCIO 1 (Teórico):
# 1. Por que o Algoritmo de Dijkstra NÃO funciona em grafos com arestas de pesos negativos?
# 2. Qual algoritmo clássico deve ser utilizado quando um grafo possui pesos negativos?
RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui: O algoritmo de Dijkstra não funciona em arestas de pesos negativos devido que ele pode
se perder devido que ele pode identificar como mais barato e acabar dando a resposta errada. Nesse caso, utilizamos
o algoritmo de Bellman-Ford, pois ele lida com arestas com pesos negativos.
"""


# EXERCÍCIO 2 (Teórico):
# Em que situações devemos escolher:
# a) Pesquisa em Largura (BFS)?
# b) Algoritmo de Dijkstra?
RESPOSTA_EXERCICIO_2 = """
Sua resposta aqui: Pesquisa em largura é ideal quando as arestas não tem pesos ou valores, isso é usado quando
apenas queremos saber o menor caminho e tudo é processado em sequência. Já no caso do Dijkstra é o contrário, temos
pesos nas arestas e o caminho inicialmente não é muito claro, logo podemos inicialmente achar dois caminhos e ir afunilando
até encontrar o caminho mais barato.
"""


# EXERCÍCIO 3 (DESAFIO DE CÓDIGO - Calculadora de Frete / Menor Custo de Envio):
# Dada uma malha logística entre cidades com seus custos de pedágio/combustível,
# implemente a função `calcular_rota_mais_barata(grafo, origem, destino)` que retorne
# uma tupla com (custo_minimo, lista_de_cidades_na_rota).
#
# Exemplo de Grafo:
# malha = {
#     "SaoPaulo": {"Campinas": 40, "Santos": 30},
#     "Campinas": {"RibeiraoPreto": 120, "SaoCarlos": 90},
#     "Santos": {"SaoJose": 150},
#     "SaoCarlos": {"RibeiraoPreto": 40},
#     "SaoJose": {"RibeiraoPreto": 100},
#     "RibeiraoPreto": {}
# }
# calcular_rota_mais_barata(malha, "SaoPaulo", "RibeiraoPreto")
# -> Retorno esperado: (160, ["SaoPaulo", "Campinas", "RibeiraoPreto"])
def achar_no_mais_barato(custos: dict[str, float], processados: set[str]) -> str | None:
    """Encontra o nó com o menor custo que ainda não foi finalizado."""
    menor_custo = float("inf")
    nodo_mais_barato = None

    for nodo, custo in custos.items():
        if custo < menor_custo and nodo not in processados:
            menor_custo = custo
            nodo_mais_barato = nodo

    return nodo_mais_barato

def calcular_rota_mais_barata(
    grafo: dict[str, dict[str, float]], origem: str, destino: str
) -> tuple[float, list[str]]:
    # TODO: Inicialize as tabelas de custos e pais dinamicamente a partir da origem e aplique o Dijkstra
    custos = {no: float("inf") for no in grafo}
    for vizinho, peso in grafo.get(origem, {}).items():
        custos[vizinho] = peso
        
    pais = {no: None for no in grafo}
    for vizinho in grafo.get(origem, {}):
        pais[vizinho] = origem
        
    processados = set()
    nodo = achar_no_mais_barato(custos, processados)
    
    while nodo is not None:
        custo = custos[nodo]
        vizinhos = grafo.get(nodo, {})
        
        for vizinho, valor in vizinhos.items():
            novo_custo = custo + valor
            if novo_custo < custos.get(vizinho, float("inf")):
                custos[vizinho] = novo_custo
                pais[vizinho] = nodo
                
        processados.add(nodo)
        nodo = achar_no_mais_barato(custos, processados)
    
    caminho_completo = [destino]
    passo = pais.get(destino)
    while passo is not None:
        caminho_completo.append(passo)
        passo = pais.get(passo)
    caminho_completo.reverse()
    
    return (custos[destino], caminho_completo)


if __name__ == "__main__":
    malha = {
        "SaoPaulo": {"Campinas": 40, "Santos": 30},
        "Campinas": {"RibeiraoPreto": 120, "SaoCarlos": 90},
        "Santos": {"SaoJose": 150},
        "SaoCarlos": {"RibeiraoPreto": 40},
        "SaoJose": {"RibeiraoPreto": 100},
        "RibeiraoPreto": {},
    }

    custo, rota = calcular_rota_mais_barata(malha, "SaoPaulo", "RibeiraoPreto")
    print(f"Custo calculado: {custo} (Esperado: 160)")
    print(
        f"Rota calculada: {rota} (Esperado: ['SaoPaulo', 'Campinas', 'RibeiraoPreto'])"
    )
