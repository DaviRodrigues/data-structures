"""
Módulo 2 - Capítulo 5: Exercícios de Fixação
Livro: Entendendo Algoritmos (Tabelas Hash)
"""

# EXERCÍCIO 1 (Teórico):
# O que é o "Fator de Carga" (Load Factor) em uma Tabela Hash?
# Por que tabelas hash precisam ser redimensionadas (resizing) quando o fator de carga passa de um certo limite (ex: 0.7)?
RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui: Fator de carga auxilia para marcar quando devemos dobrar o tamanho do array, 
assim evitamos colisões e mais de dois itens dentro do array. Lembrando, que precisamos fazer o cálculo do hash para que tudo funcione.
"""


# EXERCÍCIO 2 (Teórico):
# Quais são as principais características de uma "boa" função hash?
# O que acontece com a complexidade de tempo de busca (de O(1) para O(n)) se a função hash for ruim e mapear todas as chaves para o mesmo bucket?
RESPOSTA_EXERCICIO_2 = """
Sua resposta aqui: As principais caracteríscas são:
1 - Consistência no retorno, sendo enviada uma chave e sempre retornar o mesmo valor;
2 - Se quiser converter qualquer número ou palavra pra um índice ele tem que caber no array o fator de carga vai ajudar nesse caso (evita colisões);
3 - Se possível sempre ter uma distribuição de chaves uniformimente espalhadas, assim evita a lista crescer exponencialmente.
"""


# EXERCÍCIO 3 (DESAFIO DE CÓDIGO - Two Sum usando Hash Table):
# Dado um array de números inteiros `nums` e um número inteiro `alvo` (target),
# retorne os ÍNDICES dos dois números de modo que a soma deles seja igual a `alvo`.
#
# Requisito de Complexidade: Deve ser resolvido em tempo O(n) usando uma tabela hash (dicionário),
# e não a abordagem de força bruta O(n^2) com dois loops aninhados.
#
# Exemplo 1:
# nums = [2, 7, 11, 15], alvo = 9 -> Retorna [0, 1] (pois nums[0] + nums[1] == 9)
#
# Exemplo 2:
# nums = [3, 2, 4], alvo = 6 -> Retorna [1, 2] (pois nums[1] + nums[2] == 6)
def two_sum(nums: list[int], alvo: int) -> list[int] | None:
    # TODO: Implemente a lógica utilizando um dicionário para registrar os valores já visitados e seus índices
    hash_map = {}
    
    for idx, num in enumerate(nums):
        aux = alvo - num
        if aux in hash_map:
            return [hash_map[aux], idx]
        
        hash_map[num] = idx
            
    return None


if __name__ == "__main__":
    teste_1 = two_sum([2, 7, 11, 15], 9)
    {2:0, 11:1, 15:2, }
    print(f"Teste 1: {teste_1} (Esperado: [0, 1])")

    teste_2 = two_sum([3, 2, 4], 6)
    print(f"Teste 2: {teste_2} (Esperado: [1, 2])")

    teste_3 = two_sum([3, 3], 6)
    print(f"Teste 3: {teste_3} (Esperado: [0, 1])")
