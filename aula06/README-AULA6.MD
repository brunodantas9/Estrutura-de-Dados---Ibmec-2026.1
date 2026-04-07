# Aula 06: Filas (FIFO), Pilhas (LIFO) e Deques

[⬅️ Voltar para Estrutura de Dados - Ibmec 2026.1](https://github.com/brunodantas9/Estrutura-de-Dados---Ibmec-2026.1)

## 📖 Visão Geral
Nesta aula, exploramos as estruturas de dados lineares restritivas: **Filas** e **Pilhas**. O foco principal foi entender a diferença entre as políticas de acesso aos dados e como a biblioteca `collections.deque` do Python otimiza essas operações para garantir performance máxima ($O(1)$) tanto no início quanto no fim da estrutura.

## 📁 Conteúdo da Pasta

### 📓 Notebooks de Laboratório
- `lab_06_deque.ipynb`: Prática explorando o `collections.deque` como Fila (FIFO), Pilha (LIFO), Buffer Circular e Rotação de alta performance.
- `lab_06_validador_lifo.ipynb`: Implementação de um analisador sintático que utiliza uma Pilha para validar o balanceamento de símbolos `()`, `[]` e `{}` em expressões matemáticas.

### 🐍 Scripts de Desafio
- `simulador_call_center.py`: Implementação lógica de uma fila de atendimento bancário respeitando a regra do primeiro a chegar, primeiro a ser atendido.

## 🧠 Principais Aprendizados
1. **FIFO (First-In, First-Out):** Conceito de Fila. O primeiro elemento inserido é obrigatoriamente o primeiro a ser removido. Essencial para processamento de pipelines e sistemas de atendimento.
2. **LIFO (Last-In, First-Out):** Conceito de Pilha. O último elemento a entrar é o primeiro a sair. Base para algoritmos de "Desfazer" (Ctrl+Z) e validação de estruturas aninhadas.
3. **Eficiência do `popleft()`:** Compreensão de que remover o primeiro item de uma lista comum no Python é custoso ($O(n)$), enquanto no `deque` é instantâneo ($O(1)$) por ser uma lista duplamente encadeada.
4. **Buffer Circular:** Uso do parâmetro `maxlen` para gerenciar memória automaticamente, descartando dados antigos em sistemas de ingestão contínua.

## 🚀 Como executar o Validador
Para testar a lógica da Pilha no terminal:
```bash
python lab_06_validador_lifo.py