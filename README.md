# 💻 Portfólio de Estrutura de Dados - IBMEC 2026.1

Este repositório reúne as atividades práticas, laboratórios e desafios desenvolvidos durante a disciplina de **Estruturas de Dados** do curso de Ciência de Dados e IA. O foco central é a eficiência computacional, medição de performance e a escolha correta de algoritmos para diferentes cenários.

**Estudante:** Bruno Augusto  
**Instituição:** IBMEC - Brasília  
**Professor:** Luís Aramis

---

## 🚀 Tecnologias e Ferramentas Utilizadas
- **Linguagem:** Python 3.x
- **Ambiente:** Jupyter Notebook / VS Code
- **Bibliotecas:** `collections.deque`, `time`, `hashlib`, `sys`
- **Controle de Versão:** Git & GitHub

---

## 📂 Mapa do Repositório

| Pasta | Conteúdo Principal | Destaque Técnico |
| :--- | :--- | :--- |
| [**/aula01**](./aula01) | Configuração de Ambiente | Benchmark inicial de hardware. |
| [**/aula03**](./aula03) | Recursividade vs. Iteração | [cite_start]Uso da Call Stack e prevenção de Stack Overflow. |
| [**/aula04**](./aula04) | Vetores e Matrizes | [cite_start]Alocação de memória contígua e correção de Aliasing. |
| [**/aula05**](./aula05) | Listas Encadeadas | [cite_start]Alocação dinâmica de nós e manipulação de ponteiros manuais. |
| [**/aula06**](./aula06) | Pilhas e Filas | [cite_start]Políticas LIFO/FIFO e uso de `collections.deque` em O(1). |

---

## 🧠 Conceitos-Chave Aplicados

### ⏳ Análise Assintótica (Big O)
Durante o curso, todas as estruturas foram testadas empiricamente para validar sua complexidade:
- **Acesso direto em Vetores:** $O(1)$.
- **Busca em Listas Encadeadas:** $O(n)$.
- **Inserção no Início (Fila/Vetor):** Diferença entre $O(1)$ amortizado e $O(n)$.

### 💾 Gerenciamento de Memória
- [cite_start]Diferenciação entre memória contígua (estática) e encadeada (dinâmica).
- [cite_start]Identificação e correção de vazamentos de memória (Memory Leaks).
- [cite_start]Entendimento de objetos mutáveis e referências (Aliasing).

---

## 🛠️ Como Executar os Laboratórios

1. **Clonar o projeto:**
   ```bash
   git clone [https://github.com/brunodantas9/Estrutura-de-Dados---Ibmec-2026.1.git](https://github.com/brunodantas9/Estrutura-de-Dados---Ibmec-2026.1.git)
   cd Estrutura-de-Dados---Ibmec-2026.1