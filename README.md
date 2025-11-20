## Membros da Equipe
- **Guilherme Ulacco** RM558418
- **Matheus Hostim** RM556517
- **Eduardo Lima** RM554804

***

## Descrição do Projeto
Este projeto apresenta quatro abordagens para o Problema do Portfólio de Projetos (Mochila 0/1):

1. **Estratégia Gulosa (Greedy):** Seleciona projetos por ordem da maior relação Valor/Horas-Especialista. Não garante resultado ótimo.
2. **Recursiva Pura:** Explora todas as combinações de projetos sem armazenamento intermediário.
3. **Programação Dinâmica Top-Down (Memoização):** Recursiva com armazenamento de subproblemas para otimizar o tempo.
4. **Programação Dinâmica Bottom-Up (Iterativa):** Utiliza tabela para obter a solução ótima de forma eficiente.

O objetivo é escolher projetos que maximizem o valor total sem ultrapassar o limite de Horas-Especialista disponíveis.

***

## Estrutura do Diretório
```text
portfolio-projetos/
├── main.py           # Código principal com todas as funções e testes
└── README.md         # Este documento de orientação
```

***

## Instruções de Uso
1. Navegue até a pasta do projeto.
2. Execute:
   ```sh
   python main.py
   ```
3. O script exibe o resultado das quatro estratégias, mostrando os valores máximos alcançados em cada método e um caso de teste onde o método guloso não encontra a solução ótima.

***

## Observações
- O código está comentado e apresenta análise teórica das complexidades de tempo de cada abordagem.
- Casos de teste demonstram as limitações da estratégia gulosa comparado às abordagens ótimas.
- Para adaptar ou ampliar os testes, basta modificar as listas de projetos e capacidade no arquivo `main.py`.
