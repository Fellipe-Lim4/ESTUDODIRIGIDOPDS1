import numpy as np
import matplotlib.pyplot as plt

# Definindo o intervalo do índice discreto n
n = np.arange(-5, 16)

# 1. Impulso Unitário delta[n]
delta = np.where(n == 0, 1.0, 0.0)

# 2. Degrau Unitário u[n]
u = np.where(n >= 0, 1.0, 0.0)

# 3. Exponencial Causativa a^n * u[n] com a = 0.8
a = 0.8
exp_seq = (a**n) * u

# 4. Senoide Discreta A * cos(w0 * n + phi)
A = 2.0
w0 = np.pi / 4  # 0.25 * pi rad/amostra (Período N = 8 amostras)
phi = 0.0
senoide = A * np.cos(w0 * n + phi)

# --- Plotagem das Sequências ---
plt.figure(figsize=(12, 10))

# Subplot 1: Impulso Unitário
plt.subplot(4, 1, 1)
plt.stem(n, delta, linefmt='b-', markerfmt='bo', basefmt='k-')
plt.title('1. Impulso Unitário: $\delta[n]$')
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 2: Degrau Unitário
plt.subplot(4, 1, 2)
plt.stem(n, u, linefmt='g-', markerfmt='go', basefmt='k-')
plt.title('2. Degrau Unitário: $u[n]$')
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 3: Exponencial Real Causativa
plt.subplot(4, 1, 3)
plt.stem(n, exp_seq, linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title(f'3. Exponencial Real Causativa: $a^n u[n]$ ($a = {a}$)')
plt.ylabel('Amplitude')
plt.grid(True)

# Subplot 4: Senoide Discreta
plt.subplot(4, 1, 4)
plt.stem(n, senoide, linefmt='m-', markerfmt='mo', basefmt='k-')
plt.title('4. Senoide Discreta: $A \cos(\omega_0 n + \phi)$ ($A=2, \omega_0=\pi/4, \phi=0$)')
plt.xlabel('Índice Discreto ($n$)')
plt.ylabel('Amplitude')
plt.grid(True)

plt.tight_layout()
plt.show()

# Tabela numérica demonstrativa para os primeiros índices
print(" n  | delta[n] | u[n] | (0.8)^n * u[n] | 2*cos(pi/4 * n)")
print("-" * 55)
for i in range(5, 11):  # amostragem de n = 0 até n = 5
    print(f"{n[i]:2d}  |   {delta[i]:.1f}    |  {u[i]:.1f} |     {exp_seq[i]:.4f}     |    {senoide[i]:.4f}")