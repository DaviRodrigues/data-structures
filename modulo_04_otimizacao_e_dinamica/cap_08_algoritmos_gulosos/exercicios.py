"""
Módulo 4 - Capítulo 8: Exercícios de Fixação
Livro: Entendendo Algoritmos (Algoritmos Gulosos e Problemas NP-Completos)
"""

# EXERCÍCIO 1 (Teórico):
# 1. O que caracteriza a estratégia de um "Algoritmo Guloso" (Greedy Algorithm)?
# 2. Por que um algoritmo guloso nem sempre encontra a solução perfeita (ótima global), mas ainda assim é amplamente usado?
RESPOSTA_EXERCICIO_1 = """
Sua resposta aqui:
"""


# EXERCÍCIO 2 (Teórico):
# O que significa dizer que um problema é "NP-Completo"?
# Cite dois exemplos clássicos de problemas NP-Completos mencionados no livro.
RESPOSTA_EXERCICIO_2 = """
Sua resposta aqui:
"""


# EXERCÍCIO 3 (DESAFIO DE CÓDIGO - Problema da Mochila Fracionária / Otimização Gulosa):
# Você é um ladrão que entrou em uma joalheria com uma mochila de capacidade de peso máxima W.
# Cada item tem um valor (R$) e um peso (kg).
# Como são pós/grãos de pedras preciosas, você PODE PEGAR FRAÇÕES dos itens (Mochila Fracionária).
#
# Estratégia Gulosa:
# 1. Calcule a densidade de valor por peso (R$ / kg) de cada item.
# 2. Ordene os itens da maior densidade para a menor.
# 3. Pegue o máximo possível do item mais valioso por kg até encher a mochila.
#
# Retorne o valor total máximo obtido.
#
# Exemplo:
# itens = [
#     {"nome": "Ouro", "valor": 60, "peso": 10},      # 6 R$/kg
#     {"nome": "Prata", "valor": 100, "peso": 20},    # 5 R$/kg
#     {"nome": "Diamante", "valor": 120, "peso": 30}, # 4 R$/kg
# ]
# Capacidade: 50 kg
# Pega: 10kg de Ouro (R$ 60), 20kg de Prata (R$ 100) e 20kg de Diamante (2/3 de 120 = R$ 80).
# Total: 60 + 100 + 80 = R$ 240.0
def mochila_fracionaria_gulosa(itens: list[dict], capacidade: float) -> float:
    # TODO: Implemente a lógica gulosa escolhendo por maior razão valor/peso
    pass


if __name__ == "__main__":
    itens_teste = [
        {"nome": "Ouro", "valor": 60, "peso": 10},
        {"nome": "Prata", "valor": 100, "peso": 20},
        {"nome": "Diamante", "valor": 120, "peso": 30},
    ]
    capacidade_teste = 50

    resultado = mochila_fracionaria_gulosa(itens_teste, capacidade_teste)
    print(f"Valor máximo obtido: {resultado} (Esperado: 240.0)")
