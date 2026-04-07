# Aula 05: Listas Encadeadas (Estruturas Dinâmicas)

[⬅️ Voltar para Estrutura de Dados - Ibmec 2026.1](https://github.com/brunodantas9/Estrutura-de-Dados---Ibmec-2026.1)

## 📖 Visão Geral
Nesta aula, abandonamos a dependência de memória contígua (vetores) para implementar uma **Lista Encadeada Simples** do zero. O foco foi entender como gerenciar ponteiros manualmente usando Orientação a Objetos, criando uma estrutura capaz de crescer dinamicamente sem a necessidade de realocação física na RAM.

## 📁 Conteúdo da Pasta

### 📓 Notebooks de Laboratório
- `lab_05_aquecimento.ipynb`: Prática manual de conexão de nós e lógica de "caça ao tesouro" na memória.
- `lab_05_linked_list.ipynb`: Implementação completa da classe gerente `LinkedList` com métodos de manipulação de ponteiros.

## 🧠 Principais Aprendizados e Métodos Implementados
1. **Classe `Node`:** Criação da unidade básica de armazenamento com `valor` e o ponteiro `next`.
2. **`prepend(valor)`:** Inserção no início da lista com complexidade **O(1)**, demonstrando a superioridade em relação aos vetores tradicionais.
3. **`append(valor)`:** Inserção no final através da travessia completa da lista (**O(n)**).
4. **`search(valor)`:** Implementação de motor de busca sequencial para localizar dados na memória dinâmica.
5. **`count_nodes()`:** Algoritmo de contagem iterativa de elementos.
6. **`remove(valor)`:** Lógica de exclusão de nós, aprendendo a importância de não "soltar a corda" da memória antes de reancorar os ponteiros.
7. **`reverse()`:** Manipulação avançada de ponteiros (prev, current, next) para inverter a direção da lista sem criar novos objetos.

