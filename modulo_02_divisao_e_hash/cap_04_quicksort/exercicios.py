"""
Módulo 2 - Capítulo 4: Exercícios de Fixação
Livro: Entendendo Algoritmos
"""

# EXERCÍCIO 1 (Teórico):
# Por que o Quicksort tem desempenho O(n^2) no pior caso se escolhermos sempre o primeiro elemento
# como pivô em um array que JÁ ESTÁ ORDENADO? (Ex: [1, 2, 3, 4, 5])
RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui: O problema aqui que não tem uma verificação se o array previamente está ordenado.
Nesse caso vamos acabar passando O(n^2) uma para ir até o fim do array e outra para voltar e fazer a ordem.
Isso acaba sendo péssimo, principalmente se o pivot for o primeiro item, que causa ir de um em um item
"""


# EXERCÍCIO 2 (Teórico):
# A notação Big O para o Merge Sort é SEMPRE O(n log n), enquanto o Quicksort pode ser O(n^2) no pior caso.
# Mesmo assim, por que no mundo real muitos desenvolvedores e linguagens preferem o Quicksort ao invés do Merge Sort?
RESPOSTA_EXERCICIO_2 = """
Sua resposta aqui: A preferência geralmente é devido ao quicksort ter seu modelo de implentação in-place,
onde mantemos o espaço na memória constante e o que é influênciado nesse caso seria apenas as chamadas de funções na recursão.
Além disso, temos um uso melhor de cache, visto a referência de memória única, por mais que o quicksort possa no pior caso se O(n^2)
muita das vezes isso não vai acontecer se escolhido um bom pivot.
"""


# EXERCÍCIO 3 (DESAFIO DE CÓDIGO - Busca Binária Recursiva com D&C):
# No Capítulo 1 implementamos a Pesquisa Binária com um loop `while`.
# Agora, use a estratégia Dividir para Conquistar (D&C) e Recursão para implementar
# a função `pesquisa_binaria_recursiva(lista, item, baixo, alto)`.
#
# Dica:
# - Caso-base 1: Se baixo > alto, o item não está na lista -> retorne None.
# - Caso-base 2: Se lista[meio] == item, encontrou -> retorne meio.
# - Caso recursivo: Se lista[meio] > item, chame recursivamente na metade inferior (alto = meio - 1).
#                   Se lista[meio] < item, chame recursivamente na metade superior (baixo = meio + 1).
def pesquisa_binaria_recursiva(
    lista: list, item: int, baixo: int = 0, alto: int | None = None
) -> int | None:
    if alto is None:
        alto = len(lista) - 1

    if baixo > alto:
        return None
    
    meio = (alto + baixo) // 2
    aux = lista[meio]
        
    if aux == item:
        return meio
        
    if aux > item:
        return pesquisa_binaria_recursiva(lista, item, baixo, meio - 1)
    else:
        return pesquisa_binaria_recursiva(lista, item, meio + 1, alto)


if __name__ == "__main__":
    teste_busca = [1, 3, 5, 7, 9, 11, 13, 15]
    print(f"Lista: {teste_busca}")
    print(
        f"Busca pelo 7:  índice {pesquisa_binaria_recursiva(teste_busca, 7)} (esperado: 3)"
    )
    print(
        f"Busca pelo 15: índice {pesquisa_binaria_recursiva(teste_busca, 15)} (esperado: 7)"
    )
    print(
        f"Busca pelo 8:  índice {pesquisa_binaria_recursiva(teste_busca, 8)} (esperado: None)"
    )
