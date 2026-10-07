import numpy as np
import matplotlib.pyplot as plt

# Definindo o tempo n
n = np.arange(-5, 11)

# Sinal de entrada x[n]: Pulso de amplitude 1 entre n=0 e n=4
x = np.where((n >= 0) & (n <= 4), 1.0, 0.0)

# Simulação dos Sistemas
# Sistema 1: y[n] = 2x[n] (Ganho simples)
y1 = 2 * x

# Sistema 3: y[n] = x[n]^2 (Não Linear)
y3 = x**2

# Sistema 5: y[n] = n * x[n] (Variante no tempo e Não BIBO Estável)
y5 = n * x

# --- Plotagem dos Gráficos ---
plt.figure(figsize=(12, 10))

# 1. Sinal de Entrada
plt.subplot(4, 1, 1)
plt.stem(n, x, linefmt='k-', markerfmt='ko', basefmt='k-')
plt.title('Sinal de Entrada: x[n] (Limitado a amplitude 1)')
plt.ylabel('Amplitude')
plt.grid(True)

# 2. Sistema 1
plt.subplot(4, 1, 2)
plt.stem(n, y1, linefmt='b-', markerfmt='bo', basefmt='k-')
plt.title('Sistema 1 (Linear e Estável): y[n] = 2 * x[n]')
plt.ylabel('Amplitude')
plt.grid(True)

# 3. Sistema 3
plt.subplot(4, 1, 3)
plt.stem(n, y3, linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title('Sistema 3 (Não Linear): y[n] = (x[n])^2')
plt.ylabel('Amplitude')
plt.grid(True)

# 4. Sistema 5
plt.subplot(4, 1, 4)
plt.stem(n, y5, linefmt='g-', markerfmt='go', basefmt='k-')
plt.title('Sistema 5 (Instável e Variante no Tempo): y[n] = n * x[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# Demonstração numérica da Variância no tempo do Sistema 5
print("Prova de Variância no Tempo para y[n] = n * x[n] com n0 = 2")
print(" n | Entrada x[n] | Entrada Atrasada x[n-2] | T{x[n-2]} | Saida Atrasada y[n-2]")
print("-" * 80)
for i in range(5, 12): # Verificando n de 0 a 6
    # x[n-2] logicamente deslocado
    x_atrasado = 1 if 2 <= n[i] <= 6 else 0
    # APLICANDO o sistema na entrada atrasada: T{x[n-2]} = n * x[n-2]
    T_x_atrasado = n[i] * x_atrasado
    # Atrasando a saida que ja estava pronta: y[n-2] = (n-2) * x[n-2]
    y_atrasado = (n[i] - 2) * x_atrasado
    print(f" {n[i]:1d} |      {int(x[i])}       |            {x_atrasado}            |     {T_x_atrasado}     |          {y_atrasado}")