import numpy as np
import matplotlib.pyplot as plt

# --- Etapa 2: Geração computacional (Sinal "Contínuo") ---
f0 = 1.2
t_cont = np.arange(0, 2.5, 0.001) # Alta resolução simulando tempo contínuo (2.5 segundos)
# Modelo: x(t) = 1.0*cos(2*pi*1.2*t) - 0.5*cos(2*pi*2.4*t) + 0.3*cos(2*pi*3.6*t)
x_cont = 1.0 * np.cos(2 * np.pi * f0 * t_cont) - 0.5 * np.cos(2 * np.pi * 2 * f0 * t_cont) + 0.3 * np.cos(2 * np.pi * 3 * f0 * t_cont)

# --- Etapa 3: Amostragem ---
fs = 100 # Frequência de amostragem de 100 Hz
Ts = 1 / fs
n = np.arange(0, 2.5, Ts) # Instantes discretos
x_n = 1.0 * np.cos(2 * np.pi * f0 * n) - 0.5 * np.cos(2 * np.pi * 2 * f0 * n) + 0.3 * np.cos(2 * np.pi * 3 * f0 * n)

# --- Etapa 4: Quantização ---
def quantizar(sinal, bits):
    n_niveis = 2**bits
    val_min, val_max = np.min(sinal), np.max(sinal)
    passo = (val_max - val_min) / (n_niveis - 1)
    return np.round((sinal - val_min) / passo) * passo + val_min

x_4bits = quantizar(x_n, 4) # 16 níveis
x_8bits = quantizar(x_n, 8) # 256 níveis

# --- Etapa 5: Inclusão de ruído ---
# Ruído gaussiano (simulando artefatos musculares de alta frequência e contato do eletrodo)
np.random.seed(42)
ruido = np.random.normal(0, 0.2, len(x_n))
x_ruido = x_8bits + ruido # Aplicamos o ruído sobre o sinal digitalizado (8 bits)

# --- Etapa 6: Processamento por Sistema LTI (Filtro FIR de Média Móvel) ---
M = 5 # Filtro de média móvel com 5 amostras (suavização de 50 ms)
h = np.ones(M) / M
y = np.convolve(x_ruido, h, mode='same') # Convolução discreta (mode='same' mantém o eixo de tempo alinhado)

# --- Etapa 7: Comparação dos Resultados (Plotagem) ---
plt.figure(figsize=(14, 16))

# 1. Sinal Contínuo vs Amostrado
plt.subplot(5, 1, 1)
plt.plot(t_cont, x_cont, 'b-', alpha=0.5, label='Contínuo x(t)')
plt.stem(n, x_n, linefmt='r-', markerfmt='r.', basefmt='k-', label='Amostrado x[n]')
plt.title('Etapa 3: Sinal Contínuo e Amostragem (fs = 100 Hz)')
plt.legend()
plt.grid(True)

# 2. Efeito da Quantização
plt.subplot(5, 1, 2)
plt.step(n, x_4bits, 'g-', label='Quantizado (4 bits - 16 níveis)', where='mid')
plt.plot(n, x_8bits, 'r--', label='Quantizado (8 bits - 256 níveis)', alpha=0.8)
plt.title('Etapa 4: Quantização (4 bits vs 8 bits)')
plt.legend()
plt.grid(True)

# 3. Sinal Original vs Ruído
plt.subplot(5, 1, 3)
plt.plot(n, x_8bits, 'k-', linewidth=2, label='Sinal de Interesse (8 bits)')
plt.plot(n, ruido, 'm-', alpha=0.5, label='Ruído Aleatório')
plt.title('Etapa 5: Sinal Original e Ruído Adicionado')
plt.legend()
plt.grid(True)

# 4. Sinal Contaminado
plt.subplot(5, 1, 4)
plt.plot(n, x_ruido, 'r-', label='Sinal Contaminado xr[n]')
plt.title('Sinal Corrompido pronto para Processamento')
plt.legend()
plt.grid(True)

# 5. Filtragem por Convolução
plt.subplot(5, 1, 5)
plt.plot(n, x_ruido, 'r-', alpha=0.3, label='Sinal Contaminado')
plt.plot(n, y, 'b-', linewidth=2, label=f'Sinal Filtrado y[n] (M={M})')
plt.title('Etapa 6: Processamento por Convolução LTI')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()