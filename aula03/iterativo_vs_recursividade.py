""" Implemente uma função `fatorial_iterativo(n)` usando um loop `for` ou `while`. """

def fatorial_iterativo(n):
    resultado = 1
    for i in range (1, n + 1):
        resultado *= i
    return resultado
    


print(f'5! (Iterativo) = {fatorial_iterativo(5)}')


"""
Implemente uma função `fatorial_recursivo(n)` que chama a si mesma.
Lembre-se do **Caso Base** ($n=0$ ou $n=1$) e do **Passo Recursivo**.
"""

def fatorial_recursivo(n):
    if n < 2:
     return 1
    else :
       return n * fatorial_recursivo (n - 1)
    

# Teste
print(f'5! (Recursivo) = {fatorial_recursivo(5)}')



"""
Agora vamos comparar o desempenho das duas abordagens para valores maiores de $n$.
Utilizaremos a biblioteca `time`.
"""

import time

def medir_tempo(funcao, n):
    inicio = time.time()
    resultado = funcao(n)
    fim = time.time()
    tempo_total = fim - inicio
    return tempo_total

# Teste com N=900 (Cuidado com o limite de recursão!)
n_teste = 900

tempo_it = medir_tempo(fatorial_iterativo, n_teste)
tempo_rec = medir_tempo(fatorial_recursivo, n_teste)

print(f'Tempo Iterativo: {tempo_it:.6f} segundos')
print(f'Tempo Recursivo: {tempo_rec:.6f} segundos')

"""
Monitoramento de memória
"""

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



