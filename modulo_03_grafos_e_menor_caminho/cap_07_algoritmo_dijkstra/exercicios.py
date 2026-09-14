"""
Módulo 3 - Capítulo 7: Exercícios de Fixação
Livro: Entendendo Algoritmos (Algoritmo de Dijkstra)
"""

# EXERCÍCIO 1 (Teórico):
# 1. Por que o Algoritmo de Dijkstra NÃO funciona em grafos com arestas de pesos negativos?
# 2. Qual algoritmo clássico deve ser utilizado quando um grafo possui pesos negativos?
RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui: 
"""


# EXERCÍCIO 2 (Teórico):
# Em que situações devemos escolher:
# a) Pesquisa em Largura (BFS)?
# b) Algoritmo de Dijkstra?
RESPOSTA_EXERCICIO_2 = """
Sua resposta aqui: 
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
# -> Retorno esperado: (170, ["SaoPaulo", "Campinas", "SaoCarlos", "RibeiraoPreto"])
def calcular_rota_mais_barata(
    grafo: dict[str, dict[str, float]], origem: str, destino: str
) -> tuple[float, list[str]]:
    # TODO: Inicialize as tabelas de custos e pais dinamicamente a partir da origem e aplique o Dijkstra
    pass


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
    print(f"Custo calculado: {custo} (Esperado: 170)")
    print(
        f"Rota calculada: {rota} (Esperado: ['SaoPaulo', 'Campinas', 'SaoCarlos', 'RibeiraoPreto'])"
    )
