"""
Módulo 1 - Capítulo 1: Exercícios de Fixação
Livro: Entendendo Algoritmos
"""

# EXERCÍCIO 1:
# Suponha que você tenha uma lista com 128 nomes em ordem alfabética.
# No pior caso, quantas etapas a pesquisa binária levaria para encontrar um nome?
RESPOSTA_EXERCICIO_1 = 7  # Substitua pelo número


# EXERCÍCIO 2:
# Se o tamanho da lista duplicar (256 nomes), quantas etapas no máximo a pesquisa binária levará?
RESPOSTA_EXERCICIO_2 = 8  # Substitua pelo número (Isso devido que a pesquisa binária faz de forma exponecial, por isso é muito útil)


# EXERCÍCIO 3 (DESAFIO DE CÓDIGO):
# Modifique ou implemente uma função `pesquisa_binaria_insercao(lista, item)`
# Se o item NÃO estiver na lista, em vez de retornar None, retorne o índice
# onde esse item DEVERIA ser inserido para manter a lista ordenada.
# Exemplo: lista = [1, 3, 5, 6], item = 5 -> retorna 2
# Exemplo: lista = [1, 3, 5, 6], item = 2 -> retorna 1
# Exemplo: lista = [1, 3, 5, 6], item = 7 -> retorna 4
def pesquisa_binaria_insercao(lista: list, item: int) -> int:
    high, low = len(lista) - 1, 0

    while low <= high:
        middle = (high + low) // 2
        
        if lista[middle] == item:
            return middle
        
        if lista[middle] > item:
            high = middle - 1
        else:
            low = middle + 1    
    
    return low   
    
print(pesquisa_binaria_insercao([1, 3, 5, 6], 7, ))      