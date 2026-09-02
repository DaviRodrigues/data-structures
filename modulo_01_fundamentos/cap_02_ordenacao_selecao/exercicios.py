"""
Módulo 1 - Capítulo 2: Exercícios de Fixação
Livro: Entendendo Algoritmos
"""

# EXERCÍCIO 1 (Teórico):
# Suponha que você esteja criando um aplicativo para anotar os pedidos dos clientes em um restaurante.
# Seu aplicativo precisa armazenar uma lista de pedidos. Os garçons adicionam pedidos ao final da lista,
# e a cozinha retira o primeiro pedido da lista para prepará-lo.
# Você usaria um Array ou uma Lista Encadeada para essa fila de pedidos? Por quê?
RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui: Lista Encadeada devido que não há necessidade de acesso instantâneo e sim sequencial
"""


# EXERCÍCIO 2 (Teórico):
# O Facebook armazena uma lista de milhões de usuários. Toda vez que alguém faz login,
# o sistema precisa buscar o nome de usuário (utilizando Pesquisa Binária).
# Considerando que a Pesquisa Binária exige que os dados fiquem ordenados e precisem de
# acesso aleatório instantâneo aos elementos do meio, qual estrutura é melhor para armazenar
# esses usuários: Array ou Lista Encadeada?
RESPOSTA_EXERCICIO_2 = """
Sua resposta aqui: Array devido a ideia ser apenas leitura e ainda mais quando se precisa de velocidade,
mas para algo mais ideal um hashmap seria o caso
"""


# EXERCÍCIO 3 (DESAFIO DE CÓDIGO):
# Implemente a ordenação por seleção em ordem DECRESCENTE (do maior para o menor).
# Dica: Você pode criar uma função `busca_maior` ou adaptar a lógica.
def ordenacao_decrescente(arr: list) -> list:
    # SEU CÓDIGO AQUI
    n = len(arr) - 1
    for i in range(n, -1, -1):
        
        min_idx = i
        for j in range(i-1, -1, -1):
            if arr[j] < arr[min_idx]:
                min_idx = j
            
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr


if __name__ == "__main__":
    teste = [14, 3, 77, 2, 45, 10]
    resultado = ordenacao_decrescente(teste)
    print(f"Original: {teste}")
    print(f"Decrescente: {resultado}")

