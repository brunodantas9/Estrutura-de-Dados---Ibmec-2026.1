# Aula 04: Vetores, Matrizes e Memória Física

[⬅️ Voltar para Estrutura de Dados - Ibmec 2026.1](https://github.com/brunodantas9/Estrutura-de-Dados---Ibmec-2026.1)

## 📖 Visão Geral
Esta aula desmistifica como o hardware enxerga as variáveis por baixo dos panos do Python. O foco principal foi entender a alocação de memória linear (contígua) para vetores, a matemática que garante o acesso em tempo constante $O(1)$ e os custos mecânicos de inserção/remoção. Além disso, exploramos a "ilusão do 2D" e as armadilhas de referências de memória na criação de matrizes (Aliasing).

## 📁 Conteúdo da Pasta

### 📓 Notebooks de Laboratório
- `lab_04_vetores_matrizes.ipynb`: Benchmarks empíricos testando a diferença de tempo de inserção/remoção no início $O(n)$ vs no final $O(1)$ de vetores, além da prova de tempo cúbico $O(n^3)$ na multiplicação de matrizes.
- `lab_04_armadilha_matrizes.ipynb`: Estudo de caso isolando o "Bug da Cópia Rasa" (`Shallow Copy`). Uso da função `id()` para diagnosticar aliasing de memória em objetos mutáveis e a correção utilizando *List Comprehension*.

### 📚 Material Teórico
- Slides da aula com diagramas da fita de memória RAM, a transição do modelo matemático para a arquitetura física e a introdução ao conceito de Vetorização de Hardware (SIMD).

## 🧠 Principais Aprendizados
1. **A Ilusão do 2D:** A memória RAM é estritamente unidimensional (uma fita linear). Estruturas multidimensionais são ilusões criadas pelo cálculo de índices do tipo: $Endereço = Base + (Indice \times Tamanho)$.
2. **Custo do Deslocamento:** Em vetores contíguos, inserir ou remover elementos do início gera um "efeito cascata" custoso $O(n)$, pois obriga o processador a deslocar fisicamente todos os outros itens.
3. **A Armadilha do Aliasing:** Criar matrizes usando o operador de multiplicação (`[[0]*3]*3`) apenas clona os ponteiros (referências) na memória, fazendo com que a alteração de uma célula altere a coluna inteira.
4. **Alocação Isolada:** A forma segura ("Jeito Pythônico") de instanciar matrizes nativas é forçando a criação de novos blocos físicos com *List Comprehension*: `[[0]*3 for _ in range(3)]`.