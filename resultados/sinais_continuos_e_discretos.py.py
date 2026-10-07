import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
f = 2.0        # Frequência do sinal em Hz (2 oscilações por segundo)
A = 5.0        # Amplitude
Fs = 20.0      # Frequência de amostragem em Hz
Ts = 1 / Fs    # Período de amostragem

# Sinal contínuo (Simulado usando uma alta resolução temporal)
t_cont = np.arange(0, 1.0, 0.001)  # de 0 a 1 segundo com passos de 1 ms
x_cont = A * np.sin(2 * np.pi * f * t_cont)

# Sinal discreto (Amostrado)
n = np.arange(0, 20)               # 20 amostras (cobre 1 segundo, pois Fs = 20)
t_disc = n * Ts                    # Mapeando o índice n para o tempo real em segundos
x_disc = A * np.sin(2 * np.pi * f * t_disc)

# --- Plotagem dos Resultados ---
plt.figure(figsize=(10, 6))

# Gráfico do Sinal Contínuo
plt.subplot(2, 1, 1)
plt.plot(t_cont, x_cont, color='blue', linewidth=2)
plt.title('Sinal Contínuo no Tempo: $x(t) = 5 \sin(4\pi t)$')
plt.ylabel('Amplitude (V)')
plt.grid(True)

# Gráfico do Sinal Discreto
plt.subplot(2, 1, 2)
# Utiliza-se 'stem' para representar sequências discretas graficamente
plt.stem(t_disc, x_disc, linefmt='red', markerfmt='ro', basefmt='k')
plt.title('Sinal Discreto no Tempo ($F_s = 20$ Hz): $x[n]$')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude (V)')
plt.grid(True)

plt.tight_layout()
plt.show()

# Imprimindo os primeiros 5 valores da sequência discreta para análise numérica
print("Índice (n) | Tempo (s) | Valor x[n]")
print("-" * 35)
for i in range(5):
    print(f"    {n[i]}      |   {t_disc[i]:.2f}    |  {x_disc[i]:.4f}")