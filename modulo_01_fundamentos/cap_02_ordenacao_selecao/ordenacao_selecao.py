"""
Módulo 1 - Capítulo 2: Arrays vs Listas Encadeadas e Ordenação por Seleção (Selection Sort)
Livro: Entendendo Algoritmos (Aditya Y. Bhargava)
"""

# =====================================================================
# 1. ESTRUTURA DE DADOS: Lista Encadeada Simples (Linked List)
# =====================================================================

class Node:
    """Representa um nó na lista encadeada."""
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    """Implementação básica de Lista Encadeada."""
    def __init__(self):
        self.cabeca = None

    def inserir_no_inicio(self, valor):
        """Inserção no início: O(1) - tempo constante"""
        novo_no = Node(valor)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def exibir(self):
        """Percorrer a lista: O(n) - acesso sequencial"""
        if not (atual := self.cabeca):
            return
        elementos = []
        while atual:
            elementos.append(str(atual.valor))
            atual = atual.proximo
        print(" -> ".join(elementos) + " -> None")


# =====================================================================
# 2. ALGORITMO: Ordenação por Seleção (Selection Sort)
# =====================================================================

def busca_menor(arr: list) -> int:
    """Encontra o índice do menor elemento em um array."""
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacao_por_selecao(arr: list) -> list:
    """
    Selection Sort:
    Cria uma nova lista ordenada retirando repetidamente o menor elemento.
    Complexidade de Tempo: O(n^2)
    """
    novo_arr = []
    copia_arr = list(arr)  # Copia para não alterar o array original

    for _ in range(len(copia_arr)):
        menor_idx = busca_menor(copia_arr)
        novo_arr.append(copia_arr.pop(menor_idx))

    return novo_arr


def ordenacao_por_selecao_in_place(arr: list) -> None:
    """
    Selection Sort In-Place (sem criar lista auxiliar na memória).
    Troca os elementos diretamente no próprio array.
    """
    n = len(arr)
    for i in range(n):

        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    print("--- 1. Demonstração de Lista Encadeada ---")
    lista = ListaEncadeada()
    lista.inserir_no_inicio(30)
    lista.inserir_no_inicio(20)
    lista.inserir_no_inicio(10)
    lista.exibir()

    print("\n--- 2. Demonstração de Ordenação por Seleção ---")
    dados = [5, 3, 6, 2, 10, 1]
    print(f"Original: {dados}")
    ordenado = ordenacao_por_selecao(dados)
    print(f"Ordenado (novo array): {ordenado}")

    dados_in_place = [64, 25, 12, 22, 11]
    print(f"\nOriginal (in-place): {dados_in_place}")
    ordenacao_por_selecao_in_place(dados_in_place)
    print(f"Ordenado (in-place):  {dados_in_place}")

