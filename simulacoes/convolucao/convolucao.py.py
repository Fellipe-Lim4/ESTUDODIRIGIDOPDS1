import numpy as np
import matplotlib.pyplot as plt

# Sinais do Experimento 1
x = np.array([1, 2, 1])
h = np.array([1, 1])

# 3. Cálculo computacional da convolução
y = np.convolve(x, h)

# 4. Comparação
print("Resultados do Experimento 1:")
print(f"Sinal x[n]: {x}")
print(f"Sinal h[n]: {h}")
print(f"Sinal y[n] (Computacional): {y}")
# O resultado impresso será [1 3 3 1], idêntico ao cálculo manual.

# 5. Representação Gráfica
nx = np.arange(len(x))
nh = np.arange(len(h))
ny = np.arange(len(y))

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(nx, x, linefmt='b-', markerfmt='bo', basefmt='k-')
plt.title('Sinal de Entrada x[n]')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(nh, h, linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title('Resposta ao Impulso h[n]')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(ny, y, linefmt='g-', markerfmt='go', basefmt='k-')
plt.title('Sinal de Saída y[n] = x[n] * h[n]')
plt.grid(True)

plt.tight_layout()
plt.show()