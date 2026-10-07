import numpy as np
import matplotlib.pyplot as plt

# Definindo o vetor de índices n
n = np.arange(-6, 7)

# Definindo o sinal original x[n] (Rampa assimétrica de 4 pontos)
# x[n] = n para 0 <= n <= 3, senão 0
x = np.where((n >= 0) & (n <= 3), n, 0)

# Operações
x_atrasado = np.where(((n - 2) >= 0) & ((n - 2) <= 3), n - 2, 0) # x[n - 2]
x_avancado = np.where(((n + 2) >= 0) & ((n + 2) <= 3), n + 2, 0) # x[n + 2]
x_invertido = np.where(((-n) >= 0) & ((-n) <= 3), -n, 0)          # x[-n]
x_amplificado = 2 * x                                            # 2 * x[n]
x_polaridade = -x                                                # -x[n]

# Plotagem dos resultados
plt.figure(figsize=(14, 10))

sinais = [
    (x, '1. Sinal Original: x[n]', 'blue'),
    (x_atrasado, '2. Atraso: x[n - 2]', 'green'),
    (x_avancado, '3. Avanço: x[n + 2]', 'orange'),
    (x_invertido, '4. Inversão Temporal: x[-n]', 'red'),
    (x_amplificado, '5. Amplificação: 2 * x[n]', 'purple'),
    (x_polaridade, '6. Inversão de Polaridade: -x[n]', 'brown')
]

for i, (sig, titulo, cor) in enumerate(sinais, 1):
    plt.subplot(3, 2, i)
    plt.stem(n, sig, linefmt=f'{cor}-', markerfmt=f'{cor}o', basefmt='k-')
    plt.title(titulo)
    plt.xlabel('n')
    plt.ylabel('Amplitude')
    plt.ylim(-7, 7)
    plt.grid(True)

plt.tight_layout()
plt.show()

# Impressão numérica comparativa
print(" n  | x[n] | x[n-2] | x[n+2] | x[-n] | 2*x[n] | -x[n]")
print("-" * 52)
for idx in range(len(n)):
    print(f"{n[idx]:2d}  |  {x[idx]:.0f}   |   {x_atrasado[idx]:.0f}    |   {x_avancado[idx]:.0f}    |  {x_invertido[idx]:.0f}    |   {x_amplificado[idx]:.0f}    |  {x_polaridade[idx]:.0f}")