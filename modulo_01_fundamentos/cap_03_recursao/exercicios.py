"""
Módulo 1 - Capítulo 3: Exercícios de Fixação
Livro: Entendendo Algoritmos
"""

# EXERCÍCIO 1 (Teórico):
# O que acontece se uma função recursiva não tiver um caso-base (ou se a condição nunca for atingida)?
# Qual é o nome do erro que o sistema operacional / Python dispara quando isso acontece?
RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui: No caso seria out of memory devido que vai gerar um estouro na memória
"""


# EXERCÍCIO 2 (DESAFIO DE CÓDIGO - Soma Recursiva):
# Escreva uma função recursiva que calcule a soma de todos os números em uma lista.
# Dica:
# - Caso-base: Se a lista estiver vazia ([]), a soma é 0.
# - Caso recursivo: lista[0] + soma_recursiva(lista[1:])
def soma_recursiva(lista: list) -> int:
    if not lista:
        return 0
    
    return lista[0] + soma_recursiva(lista[1:])


# EXERCÍCIO 3 (DESAFIO DE CÓDIGO - Contagem de Elementos):
# Escreva uma função recursiva que CONTE o número de itens em uma lista
# (sem usar a função len(lista)!).
# Dica:
# - Caso-base: Se a lista estiver vazia, o total é 0.
# - Caso recursivo: 1 + conta_elementos(lista[1:])
def conta_elementos(lista: list) -> int:
    if not lista:
        return 0
    
    return 1 + conta_elementos(lista[1:])


# EXERCÍCIO 4 (DESAFIO EXTRA - Encontrar o Valor Máximo):
# Encontre o valor mais alto em uma lista utilizando apenas recursão.
# Dica:
# - Caso-base: Se a lista tiver apenas 1 elemento, o máximo é esse elemento (lista[0]).
# - Caso recursivo: Calcule o máximo do restante (max_sub = maximo_recursivo(lista[1:])),
#   e retorne lista[0] se for maior que max_sub, senão retorne max_sub.
def maximo_recursivo(lista: list) -> int:
    if len(lista) == 1:
        return lista[0]
    
    max_sub = maximo_recursivo(lista[1:])
    if lista[0] > max_sub:
        return lista[0]
    
    return max_sub


if __name__ == "__main__":
    numeros = [2, 4, 10, 6, 8]
    print(f"Lista de teste: {numeros}")
    # print(f"Soma: {soma_recursiva(numeros)} (esperado: 30)")
    # print(f"Contagem: {conta_elementos(numeros)} (esperado: 5)")
    print(f"Máximo: {maximo_recursivo(numeros)} (esperado: 10)")

