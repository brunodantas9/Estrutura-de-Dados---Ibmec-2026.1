import tracemalloc

def fatorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# 1. Inicia o rastreamento de memória
tracemalloc.start()

# 2. Executa o código (seu loop iterativo para um número alto)
fatorial_iterativo(5000)

# 3. Tira um "retrato" (snapshot) do estado atual da memória
snapshot = tracemalloc.take_snapshot()

# 4. Analisa e exibe as estatísticas (ex: top 5 linhas que mais consumiram memória)
top_stats = snapshot.statistics('lineno')
for stat in top_stats[:5]:
    print(stat)

# 5. Opcional: para o rastreamento
tracemalloc.stop()