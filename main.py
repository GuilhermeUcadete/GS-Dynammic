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
    # =============================================================================
# Fase 4: Programação Dinâmica Bottom-Up (Iterativa)
# COMPLEXIDADE: O(n*C) — constrói matriz T com n+1 linhas e capacidade+1 colunas
# Mais eficiente para problemas típicos de mochila/portfólio.
# =============================================================================
def portfolio_bottomup(projetos, capacidade):
    """
    Preenche matriz T[i][c]: valor máximo usando os primeiros i projetos e capacidade c.
    Mais eficiente do que abordagens recursivas.
    """
    N = len(projetos)
    C = capacidade
    T = [[0 for _ in range(C + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        valor, horas = projetos[i-1][1], projetos[i-1][2]
        for c in range(C + 1):
            if horas > c:
                T[i][c] = T[i-1][c]
            else:
                T[i][c] = max(T[i-1][c], valor + T[i-1][c - horas])
            # Cada célula T[i][c] representa o melhor valor possível com os i projetos e capacidade c
    return T[N][C]

# =============================================================================
# ANÁLISE DE DESEMPENHO (TEÓRICA)
# -----------------------------------------------------------------------------
# Greedy:      O(n log n) (devido à ordenação). Mais rápida, porém NÃO garante ótimo.
# Recursiva:   O(2^n) — Dobra para cada projeto, altamente ineficiente. Só para n pequeno.
# Memoização:  O(n*C) — Muito mais rápida que a recursiva pura. Responde cada subproblema apenas uma vez.
# Bottom-up:   O(n*C) — Mais eficiente e recomendada na prática, pois não usa pilha de recursão, fácil de adaptar e recuperar quais projetos foram escolhidos.
#
# Entre todas, PD Bottom-Up é a mais eficiente e segura para casos práticos — rápida, previsível e escalável
# ==============================================================================

print('\n--- CASO BASE (PORTFÓLIO PADRÃO) ---')
print('--Fase 1: Solução Gulosa--')
sel_greedy, v_greedy = portfolio_greedy(projetos, capacidade_maxima)
print(f"[Greedy] Valor: {v_greedy}")

print('--Fase 2: Solução Recursiva Pura--')
v_rec = portfolio_recursivo(len(projetos) - 1, capacidade_maxima, projetos)
print(f"[Recursiva] Valor: {v_rec}")

print('--Fase 3: PD Top-Down (Memoização)--')
memo = {}
v_memo = portfolio_memoizacao(len(projetos) - 1, capacidade_maxima, projetos, memo)
print(f"[Memoização] Valor: {v_memo}")

print('--Fase 4: PD Bottom-Up (Iterativa)--')
v_bottom = portfolio_bottomup(projetos, capacidade_maxima)
print(f"[Bottom-Up] Valor: {v_bottom}")

print('\n--- CASO DE FALHA DA ESTRATÉGIA GULOSA ---')
print('Projetos:', [(n, v, e) for n, v, e in caso_falha_gulosa])
sel_greedy, v_greedy = portfolio_greedy(caso_falha_gulosa, 10)
print(f"[Greedy] Valor: {v_greedy}")   # Não é ótimo!
memo = {}
v_memo = portfolio_memoizacao(len(caso_falha_gulosa)-1, 10, caso_falha_gulosa, memo)
print(f"[PD] Valor ótimo: {v_memo}")  # Ótimo!
v_bottom = portfolio_bottomup(caso_falha_gulosa, 10)
print(f"[Bottom-Up] Valor ótimo: {v_bottom}")
