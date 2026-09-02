"""
Módulo 1 - Capítulo 3: Recursão e a Pilha de Chamadas (Call Stack)
Livro: Entendendo Algoritmos (Aditya Y. Bhargava)
"""

# =====================================================================
# 1. CONTAGEM REGRESSIVA (Exemplo de Caso-base e Caso recursivo)
# =====================================================================

def contagem_regressiva(i: int):
    """
    Imprime números de i até 1.
    - Caso-base: i <= 0 (para a recursão)
    - Caso recursivo: i > 0 (chama a si mesma com i - 1)
    """
    print(i)
    if i <= 1:
        # Caso-base
        return

    # Caso recursivo
    contagem_regressiva(i - 1)


# =====================================================================
# 2. FATORIAL E A PILHA DE CHAMADAS (Call Stack)
# =====================================================================

def fatorial(x: int, nivel: int = 0) -> int:
    """
    Calcula x! (fatorial de x) demonstrando a Pilha de Chamadas.
    Fatorial: 5! = 5 * 4 * 3 * 2 * 1 = 120
    """
    indentacao = "  " * nivel
    print(f"{indentacao}-> [EMPILHANDO] Chamando fatorial({x})")

    if x <= 1:
        # Caso-base
        print(f"{indentacao}<- [DESEMPILHANDO] Caso-base atingido! fatorial(1) = 1")
        return 1

    # Caso recursivo
    resultado = x * fatorial(x - 1, nivel + 1)
    print(f"{indentacao}<- [DESEMPILHANDO] Retornando {x} * fatorial({x-1}) = {resultado}")
    return resultado


if __name__ == "__main__":
    print("--- 1. Contagem Regressiva ---")
    contagem_regressiva(5)

    print("\n--- 2. Fatorial com Rastreamento da Pilha ---")
    num = 4
    res = fatorial(num)
    print(f"\nResultado final de {num}! = {res}")

