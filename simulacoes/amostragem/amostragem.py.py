import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal contínuo
f = 5.0 # Frequência do sinal (Hz)
t_max = 0.5 # Tempo total de simulação (segundos)

# 1. Gerando o sinal contínuo (alta resolução para simular o tempo contínuo)
t_cont = np.arange(0, t_max, 0.001)
x_cont = np.sin(2 * np.pi * f * t_cont)

# 2. Definindo as três frequências de amostragem diferentes
fs_list = [100.0, 25.0, 8.0]

# Configurando a figura
plt.figure(figsize=(10, 8))

# Loop para processar e plotar cada frequência de amostragem
for i, fs in enumerate(fs_list):
    Ts = 1.0 / fs
    
    # Instantes de amostragem (tn = n * Ts)
    n = np.arange(0, int(t_max * fs))
    t_disc = n * Ts
    
    # Amostrando o sinal: x[n] = x(n * Ts)
    x_disc = np.sin(2 * np.pi * f * t_disc)
    
    # Criando os subplots
    plt.subplot(3, 1, i + 1)
    
    # Plotando o sinal contínuo (linha de fundo)
    plt.plot(t_cont, x_cont, color='gray', linestyle='--', label='Sinal contínuo x(t)')
    
    # Plotando as amostras discretas por cima (stem plot)
    plt.stem(t_disc, x_disc, linefmt='b-', markerfmt='bo', basefmt='k-', label=f'Amostras x[n]')
    
    plt.title(f'Amostragem com fs = {fs} Hz (Ts = {Ts:.3f} s)')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Amplitude')
    plt.legend(loc='upper right')
    plt.grid(True)

plt.tight_layout()
plt.show()