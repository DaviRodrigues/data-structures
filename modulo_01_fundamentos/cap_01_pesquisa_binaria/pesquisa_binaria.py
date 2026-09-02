"""
Módulo 1 - Capítulo 1: Pesquisa Binária (Binary Search)
Livro: Entendendo Algoritmos (Aditya Y. Bhargava)
"""

def pesquisa_simples(lista: list, item: int) -> tuple[int | None, int]:
    """
    Busca Linear / Simples:
    Verifica elemento por elemento da esquerda para a direita.
    
    Retorna:
        tuple (indice_encontrado, total_tentativas)
    """
    tentativas = 0
    for i, valor in enumerate(lista):
        tentativas += 1
        if valor == item:
            return i, tentativas
    return None, tentativas


def pesquisa_binaria(lista: list, item: int) -> tuple[int | None, int]:
    """
    Busca Binária:
    A cada tentativa, corta o espaço de busca pela metade.
    PRÉ-REQUISITO: A lista precisa estar ORDENADA!
    
    Retorna:
        tuple (indice_encontrado, total_tentativas)
    """
    baixo = 0
    alto = len(lista) - 1
    tentativas = 0

    while baixo <= alto:
        tentativas += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio, tentativas
        elif chute > item:
            # Chute muito alto: descarta a metade superior
            alto = meio - 1
        else:
            # Chute muito baixo: descarta a metade inferior
            baixo = meio + 1

    return None, tentativas


if __name__ == "__main__":
    # Teste 1: Lista pequena
    minha_lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    alvo = 17

    idx, steps = pesquisa_binaria(minha_lista, alvo)
    print(f"Lista: {minha_lista}")
    print(f"Buscando o número {alvo}:")
    print(f" -> Encontrado no índice: {idx} em apenas {steps} passos!")

    # Teste 2: Comparação de escala (1 milhão de elementos)
    tamanho = 256
    lista_gigante = list(range(1, tamanho + 1))
    pior_caso = tamanho  # Último elemento da lista

    print("\n" + "="*50)
    print(f"Comparativo de Busca com lista de {tamanho:,} elementos:")
    print("="*50)

    _, passos_simples = pesquisa_simples(lista_gigante, pior_caso)
    _, passos_binaria = pesquisa_binaria(lista_gigante, pior_caso)

    print(f"Pesquisa Simples (Linear - O(n)):    {passos_simples:,} passos")
    print(f"Pesquisa Binária (O(log n)):        {passos_binaria} passos")

