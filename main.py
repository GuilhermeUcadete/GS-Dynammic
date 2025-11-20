import random

# Dados de exemplo
capacidade_maxima = 10
projetos = [
    ("Projeto A", 12, 4),
    ("Projeto B", 10, 3),
    ("Projeto C", 7, 2),
    ("Projeto D", 4, 3)
]

# CASO EM QUE A SOLUÇÃO GULOSA FALHA:
# Este exemplo, abaixo, força a falha do guloso — escolha de projetos pelos maiores V/E não é ótima.
# Apenas para teste adicional, altere a lista principal ou use assim:
caso_falha_gulosa = [
    ("X", 10, 9),   # V/E = 10/9 = ~1.11
    ("Y", 11, 10),  # V/E = 11/10 = 1.1
    ("Z", 6, 5),    # V/E = 6/5 = 1.2
]
# Capacidade = 10, resposta ótima: Projetos Z + X = 16, o guloso pegaria apenas X ou Y ou Z.

# =============================================================================
# Fase 1: Estratégia Gulosa (Greedy)
# COMPLEXIDADE: O(n log n) devido à ordenação, e O(n) para seleção => O(n log n)
# NÃO GARANTE ÓTIMO. Mais rápida, mas pode errar dependendo dos dados.
# =============================================================================
def portfolio_greedy(projetos, capacidade):
    """
    Seleciona projetos usando a relação Valor/Horas (V/E).
    Nem sempre encontra a solução ótima.
    """
    projetos_ordenados = sorted(projetos, key=lambda x: x[1] / x[2], reverse=True)
    capacidade_restante = capacidade
    selecionados = []
    valor_total = 0

    for nome, valor, horas in projetos_ordenados:
        if horas <= capacidade_restante:
            selecionados.append((nome, valor, horas))
            capacidade_restante -= horas
            valor_total += valor

    return selecionados, valor_total

# =============================================================================
# Fase 2: Solução Recursiva Pura
# COMPLEXIDADE: O(2^n)
# Explora todas as combinações, recalcula subproblemas várias vezes.
# =============================================================================
def portfolio_recursivo(i, capacidade, projetos):
    """
    Exploração total das combinações. Não usa memória extra, é ineficiente para n grande.
    """
    if i < 0 or capacidade <= 0:
        return 0
    nome, valor, horas = projetos[i]
    if horas > capacidade:
        return portfolio_recursivo(i - 1, capacidade, projetos)
    else:
        return max(
            portfolio_recursivo(i - 1, capacidade, projetos),
            valor + portfolio_recursivo(i - 1, capacidade - horas, projetos)
        )

# =============================================================================
# Fase 3: Programação Dinâmica Top-Down (Memoização)
# COMPLEXIDADE: O(n*C) — cada subproblema (i, capacidade) resolvido 1x
# Usa dicionário para armazenar subproblemas e evitar recalculo.
# =============================================================================
def portfolio_memoizacao(i, capacidade, projetos, memo):
    """
    Usa memoização: salva subproblemas, evita recalculos. Rápido para n e capacidade moderados.
    """
    if i < 0 or capacidade <= 0:
        return 0
    key = (i, capacidade)
    if key in memo:
        return memo[key]
    nome, valor, horas = projetos[i]
    if horas > capacidade:
        resultado = portfolio_memoizacao(i - 1, capacidade, projetos, memo)
    else:
        resultado = max(
            portfolio_memoizacao(i - 1, capacidade, projetos, memo),
            valor + portfolio_memoizacao(i - 1, capacidade - horas, projetos, memo)
        )
    memo[key] = resultado
    return resultado