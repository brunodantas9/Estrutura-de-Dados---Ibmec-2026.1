# Aula 01: Configuração de Ambiente e Benchmark

## Sobre esta Aula
Esta pasta contém as atividades introdutórias da disciplina de Estruturas de Dados. O objetivo principal foi validar a configuração do ambiente Python e realizar uma análise empírica de tempo de execução utilizando a função nativa de ordenação do Python (`Timsort`).

## Arquivos
- `hello.py`: Script simples para validação do ambiente e versão do Python.
- `benchmark_inicial.py`: Script para medir o tempo de ordenação de listas com números aleatórios variando o tamanho de `N`.

## Resultados do Benchmark
Após rodar o script de benchmark, observamos o tempo de execução (em segundos) para diferentes tamanhos de listas. 

| Tamanho da Lista (N) | Tempo de Execução (s) |
| :--- | :--- |
| 1.000.000 | 0.2326 |
| 5.000.000 | 1.2608 |
| 10.000.000 | 2.9734 |
| 100.000.000 | 40.0658 |

**Observação:** Podemos notar que o crescimento do tempo respeita uma certa linearidade (característico do $O(N \log N)$ em listas semi-aleatórias para o Timsort).

### Especificações da Máquina (Setup de Teste)
Para fins de reprodutibilidade, os testes acima foram executados no seguinte hardware:
- **Processador:** 13th Gen Intel(R) Core(TM) i7-1360P (2.20 GHz)
- **RAM:** 16GB
- **SO:** Windows 11
- **Python:** 3.12.6

## Como executar localmente
Se você já clonou o repositório principal, navegue até esta pasta e execute os scripts:

```bash
cd aula01
python hello.py
python benchmark_inicial.py