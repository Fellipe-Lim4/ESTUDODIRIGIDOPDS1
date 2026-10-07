import numpy as np
import matplotlib.pyplot as plt

# 1. Geração do Sinal Original e Contaminado
n = np.arange(0, 60)
# Sinal original: Pulso que vale 1 entre n=10 e n=40
x_original = np.where((n >= 10) & (n <= 40), 1.0, 0.0)

# Adicionando ruído gaussiano (média 0, desvio padrão 0.2)
np.random.seed(42) # Para reprodutibilidade
ruido = np.random.normal(0, 0.2, len(n))
x_contaminado = x_original + ruido

# 2. Definição das Respostas ao Impulso (h[n])
M_vals = [3, 5, 10]
h = {M: np.ones(M) / M for M in M_vals}

# 3. Filtragem por Convolução
y = {M: np.convolve(x_contaminado, h[M]) for M in M_vals}

# 4. Representação Gráfica
plt.figure(figsize=(12, 12))

# Plot do Sinal Original e Contaminado
plt.subplot(4, 1, 1)
plt.plot(n, x_original, 'k--', label='Original', linewidth=2)
plt.stem(n, x_contaminado, linefmt='r-', markerfmt='r.', basefmt='k-', label='Contaminado')
plt.title('Sinal Original e Contaminado com Ruído')
plt.legend()
plt.grid(True)

# Plot dos Sinais Filtrados
cores = {3: 'b', 5: 'g', 10: 'm'}
for i, M in enumerate(M_vals, 2):
    plt.subplot(4, 1, i)
    ny = np.arange(len(y[M]))
    
    # Exibe a resposta ao impulso no canto do gráfico como texto
    hn_str = f"h[n] = 1/{M} * [{', '.join(['1']*M)}]"
    
    plt.stem(ny, y[M], linefmt=f'{cores[M]}-', markerfmt=f'{cores[M]}.', basefmt='k-')
    plt.plot(n, x_original, 'k--', alpha=0.5, label='Ref. Original') # Referência
    plt.title(f'Sinal Filtrado com M = {M} | {hn_str}')
    plt.legend()
    plt.grid(True)

plt.tight_layout()
plt.show()