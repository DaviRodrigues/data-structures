"""
Módulo 4 - Capítulo 8: Algoritmos Gulosos (Greedy Algorithms) e Problemas NP-Completos
Livro: Entendendo Algoritmos (Aditya Y. Bhargava)

Neste arquivo implementamos:
1. O clássico Problema da Cobertura de Conjuntos (Set-Covering Problem).
2. Algoritmo Guloso de Aproximação para encontrar estações de rádio com cobertura ótima.
"""


# =====================================================================
# 1. PROBLEMA DA COBERTURA DE CONJUNTOS (SET-COVERING)
# =====================================================================
# Cenário: Você quer abrir um programa de rádio e alcançar ouvintes em todos os estados da lista.
# Cada estação de rádio cobre um conjunto de estados, e há um custo por estação.
# Como selecionar o menor número de estações para cobrir todos os estados?
#
# Solução Exata (Força Bruta): 2^n combinações -> O(2^n) - Intratável para muitas estações!
# Solução Gulosa (Aproximação): Escolhe a cada passo a estação que cobre mais estados ainda não cobertos.
# Complexidade Gulosa: O(n^2) onde n é o número de estações.


def cobertura_de_conjuntos_gulosa(
    estados_necessarios: set[str], estacoes: dict[str, set[str]]
) -> set[str]:
    """
    Algoritmo guloso de aproximação:
    1. Enquanto houver estados para cobrir:
       - Escolhe a estação que cobre o maior número de estados restantes (não cobertos).
       - Adiciona essa estação ao resultado final.
       - Remove os estados cobertos por ela do conjunto de estados necessários.
    """
    estados_restantes = set(estados_necessarios)
    estacoes_escolhidas = set()

    while estados_restantes:
        melhor_estacao = None
        estados_cobertos_pela_melhor = set()

        for estacao, estados_que_cobre in estacoes.items():
            # Interseção (&): estados que essa estação cobre E que ainda precisamos cobrir
            cobertos = estados_restantes & estados_que_cobre

            # Se essa estação cobre mais estados do que a nossa melhor escolha atual
            if len(cobertos) > len(estados_cobertos_pela_melhor):
                melhor_estacao = estacao
                estados_cobertos_pela_melhor = cobertos

        if melhor_estacao is None:
            # Caso não haja estações suficientes para cobrir todos os estados
            break

        estados_restantes -= estados_cobertos_pela_melhor
        estacoes_escolhidas.add(melhor_estacao)

    return estacoes_escolhidas


if __name__ == "__main__":
    print("=" * 65)
    print("Problema da Cobertura de Conjuntos (Algoritmo Guloso)")
    print("=" * 65)

    # Estados que precisamos cobrir no Brasil (exemplo didático)
    estados_alvo = {"sp", "rj", "mg", "es", "pr", "sc", "rs", "ba"}

    # Estações disponíveis e suas respectivas áreas de cobertura
    estacoes_disponiveis = {
        "k_sul": {"pr", "sc", "rs"},
        "k_sudeste": {"sp", "rj", "mg", "es"},
        "k_litoral": {"rj", "es", "ba"},
        "k_centro_sul": {"sp", "pr", "mg"},
        "k_nordeste_sul": {"ba", "mg", "es"},
    }

    print(f"Estados desejados: {estados_alvo}\n")
    print("Estações disponíveis:")
    for estacao, cobertura in estacoes_disponiveis.items():
        print(f"  - {estacao}: {cobertura}")

    escolhas = cobertura_de_conjuntos_gulosa(estados_alvo, estacoes_disponiveis)

    print("\n" + "=" * 65)
    print(f"Estações selecionadas pelo Algoritmo Guloso: {escolhas}")
    print(f"Total de estações necessárias: {len(escolhas)}")
    print("=" * 65)
