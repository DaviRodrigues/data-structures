"""
Módulo 2 - Capítulo 5: Tabelas Hash (Hash Tables)
Livro: Entendendo Algoritmos (Aditya Y. Bhargava)
"""

# =====================================================================
# 1. CONCEITO: TABELAS HASH NA PRÁTICA (DICIONÁRIOS EM PYTHON)
# =====================================================================
# Uma Tabela Hash combina uma "Função Hash" com um "Array" tradicional.
# A função hash mapeia strings/chaves diretamente para índices numéricos do array.
# Isso garante busca, inserção e remoção em tempo médio O(1) - Constante!

# Exemplo 1: Livro de Preços (Lookup Direto)
caderno_precos = {}
caderno_precos["maca"] = 3.50
caderno_precos["leite"] = 4.80
caderno_precos["abacate"] = 6.00

print("--- 1. Consulta de Preços (O(1)) ---")
print(f"Preço do leite: R$ {caderno_precos.get('leite', 'Não encontrado')}")


# =====================================================================
# 2. CASO DE USO: FILTRAGEM DE DUPLICADOS (CADERNO ELEITORAL)
# =====================================================================
# Exemplo clássico do livro: verificar se uma pessoa já votou.
votaram = {}


def verifica_eleitor(nome: str) -> None:
    """Verifica se o eleitor já votou em tempo O(1)."""
    if votaram.get(nome):
        print(f"[{nome}] já votou! Mande embora.")
    else:
        votaram[nome] = True
        print(f"[{nome}] pode votar!")


# =====================================================================
# 3. CASO DE USO: CACHE / MEMOIZAÇÃO (EX: SERVIDOR WEB)
# =====================================================================
# Tabelas hash são amplamente usadas para cachear páginas ou consultas pesadas.
cache_servidor = {}


def busca_dados_simulada(url: str) -> str:
    """Simula requisição lenta ao servidor se não estiver em cache."""
    if url in cache_servidor:
        return f"[CACHE HIT] {cache_servidor[url]}"
    else:
        # Simulando uma busca pesada / consulta de banco
        dados = f"Conteúdo renderizado de {url}"
        cache_servidor[url] = dados
        return f"[CACHE MISS -> Buscado e Salvo] {dados}"


# =====================================================================
# 4. IMPLEMENTAÇÃO MANUAL: MINI TABELA HASH COM TRATAMENTO DE COLISÕES
# =====================================================================
# Quando duas chaves diferentes geram o mesmo índice, ocorre uma COLISÃO.
# A forma clássica de resolver é o Encadeamento Separado (Separate Chaining):
# cada posição do array guarda uma lista de pares (chave, valor).


from typing import Any


class MiniHashTable:
    """
    Implementação simplificada de uma Tabela Hash com encadeamento separado.
    """

    def __init__(self, capacidade: int = 10):
        self.capacidade = capacidade
        # Cada "bucket" (balde) inicializa como uma lista vazia
        self.tabela: list[list[tuple[str, Any]]] = [[] for _ in range(capacidade)]

    def _funcao_hash(self, chave: str) -> int:
        """
        Função hash simples: soma os valores ASCII dos caracteres
        e aplica o operador módulo (%) pelo tamanho da tabela.
        """
        soma_ascii = sum(ord(char) for char in chave)
        return soma_ascii % self.capacidade

    def inserir(self, chave: str, valor: Any) -> None:
        """Insere ou atualiza um par chave-valor."""
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]
        print(indice)

        # Verifica se a chave já existe no bucket para atualizar
        for i, (k, _) in enumerate(bucket):
            if k == chave:
                bucket[i] = (chave, valor)
                return

        # Se não existe, insere o novo par (chave, valor)
        bucket.append((chave, valor))
        print(bucket)

    def buscar(self, chave: str) -> Any | None:
        """Busca o valor associado a uma chave."""
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]

        for k, v in bucket:
            if k == chave:
                return v
        return None

    def remover(self, chave: str) -> bool:
        """Remove a chave e seu valor. Retorna True se removeu com sucesso."""
        indice = self._funcao_hash(chave)
        bucket = self.tabela[indice]

        for i, (k, _) in enumerate(bucket):
            if k == chave:
                del bucket[i]
                return True
        return False

    def __repr__(self) -> str:
        linhas = []
        for i, bucket in enumerate(self.tabela):
            linhas.append(f"Bucket {i}: {bucket}")
        return "\n".join(linhas)


if __name__ == "__main__":
    print("\n--- 2. Verificação de Votantes ---")
    verifica_eleitor("Tom")
    verifica_eleitor("Mike")
    verifica_eleitor("Mike")

    print("\n--- 3. Simulação de Cache Web ---")
    print(busca_dados_simulada("facebook.com"))
    print(busca_dados_simulada("google.com"))
    print(busca_dados_simulada("facebook.com"))

    print("\n--- 4. Teste da MiniHashTable Manual ---")
    ht = MiniHashTable(capacidade=5)
    ht.inserir("maca", 3.50)
    ht.inserir("banana", 2.00)
    ht.inserir("abacate", 6.00)
    ht.inserir("mamao", 4.50)

    print("Estado interno dos Buckets:")
    print(ht)

    print(f"\nBusca por 'maca': {ht.buscar('maca')}")
    print(f"Busca por 'uva': {ht.buscar('uva')}")

    print("\nRemovendo 'banana'...")
    ht.remover("banana")
    print(f"Busca por 'banana' após remoção: {ht.buscar('banana')}")
