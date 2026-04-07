# Aula 03: Recursividade e Complexidade de Memória

[⬅️ Voltar para Estrutura de Dados - Ibmec 2026.1](https://github.com/brunodantas9/Estrutura-de-Dados---Ibmec-2026.1)

## 📖 Visão Geral
Esta aula explora o conceito de funções que chamam a si mesmas e o impacto disso na **Pilha de Chamadas (Call Stack)**. O foco principal foi entender quando a recursão é elegante e quando ela se torna ineficiente em termos de memória (causando o famoso *Stack Overflow*).

## 📁 Conteúdo da Pasta

### 📓 Notebooks de Laboratório
- `lab_03_recursao.ipynb`: Implementações básicas e conceitos fundamentais.
- `lab_03_pratica_escolha.ipynb`: Exercícios práticos focados na tomada de decisão entre algoritmos iterativos e recursivos.
- `lab_03_benchmark_extra.ipynb`: Testes de performance e medição de tempo adicionais.

### 🐍 Scripts de Comparação
- `iterativo_vs_recursividade.py`: Comparação direta de lógica e sintaxe entre loops tradicionais e recursão.
- `benchmark_monitoramento_memoria.py`: Script avançado que mede o consumo de RAM durante a execução dos códigos.

### 📚 Material Teórico
- Slides e plano de aula detalhando a análise assintótica e o veredito sobre o uso de recursividade.

## 🧠 Principais Aprendizados
1. **Caso Base:** A importância vital de definir a condição de parada para evitar recursão infinita.
2. **Custo de Memória ($O(n)$):** Compreensão prática de que cada chamada recursiva adiciona um novo *frame* na pilha, consumindo memória proporcional à profundidade da recursão.
3. **Benchmarking e Decisão:** Através dos scripts de monitoramento, observamos como a iteração costuma ser mais eficiente em termos de recursos computacionais, apesar da recursão ser mais legível e ideal para certos problemas ramificados (como árvores, grafos ou fractais).

## 🚀 Como executar os testes de performance

Para visualizar a diferença de consumo de memória na sua própria máquina, execute o script de benchmarking através do seu terminal:

```bash
python benchmark_monitoramento_memoria.py