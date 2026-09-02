"""
Módulo 2 - Capítulo 4: Dividir para Conquistar (D&C) e Quicksort
Livro: Entendendo Algoritmos (Aditya Y. Bhargava)
"""

import random
import time

# =====================================================================
# 1. ALGORITMO QUICKSORT (Versão Didática Pythônica)
# =====================================================================


def quicksort(arr: list) -> list:
    """
    Ordenação Quicksort usando a estratégia Dividir para Conquistar:
    - Caso-base: arrays com 0 ou 1 elementos já estão ordenados.
    - Caso recursivo: escolhe um pivô, particiona em menores e maiores,
      e ordena recursivamente as duas partes.
    """
    if len(arr) < 2:
        # Caso-base
        return arr
    else:
        # Caso recursivo: escolhemos o primeiro elemento como pivô
        pivo = arr[0]

        # Sub-array de todos os elementos menores ou iguais ao pivô
        menores = [i for i in arr[1:] if i <= pivo]

        # Sub-array de todos os elementos maiores que o pivô
        maiores = [i for i in arr[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)


# =====================================================================
# 2. QUICKSORT COM PIVÔ ALEATÓRIO (Evita o Pior Caso O(n^2))
# =====================================================================


def quicksort_aleatorio(arr: list) -> list:
    """
    Quicksort com pivô aleatório:
    Garante tempo médio O(n log n) mesmo se o array já estiver ordenado.
    """
    if len(arr) < 2:
        return arr
    else:
        # Escolhe um índice aleatório para o pivô
        pivo_idx = random.randint(0, len(arr) - 1)
        pivo = arr[pivo_idx]

        resto = arr[:pivo_idx] + arr[pivo_idx + 1 :]
        menores = [i for i in resto if i <= pivo]
        maiores = [i for i in resto if i > pivo]

        return quicksort_aleatorio(menores) + [pivo] + quicksort_aleatorio(maiores)


if __name__ == "__main__":
    lista_exemplo = [10, 5, 2, 3, 7, 8, 1, 9]
    print(f"Lista original: {lista_exemplo}")
    print(f"Lista ordenada (Quicksort): {quicksort(lista_exemplo)}")

    # Comparação de velocidade: Quicksort vs Selection Sort
    tamanho = 3000
    lista_teste = [random.randint(1, 100000) for _ in range(tamanho)]

    print("\n" + "=" * 55)
    print(f"Teste de Desempenho com {tamanho} elementos aleatórios:")
    print("=" * 55)

    # Quicksort O(n log n)
    t0 = time.perf_counter()
    resultado_qs = quicksort(lista_teste)
    t1 = time.perf_counter()
    tempo_qs = t1 - t0
    print(f"Quicksort (O(n log n)):           {tempo_qs:.6f} segundos")

    # Selection Sort O(n^2)
    def selection_sort_teste(arr):
        copia = list(arr)
        ordenado = []
        for _ in range(len(copia)):
            menor = min(copia)
            copia.remove(menor)
            ordenado.append(menor)
        return ordenado

    t0 = time.perf_counter()
    selection_sort_teste(lista_teste)
    t1 = time.perf_counter()
    tempo_ss = t1 - t0
    print(f"Selection Sort (O(n^2)):          {tempo_ss:.6f} segundos")
    print(f"-> O Quicksort foi aproximadamente {tempo_ss / tempo_qs:.1f}x mais rápido!")
