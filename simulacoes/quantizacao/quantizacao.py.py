import numpy as np
import matplotlib.pyplot as plt

# 1. Parâmetros do Sinal Original
t = np.arange(0, 1, 0.001)  # Tempo de 0 a 1 segundo
f = 1.0                     # Frequência de 1 Hz
Vref = 5.0                  # Tensão de referência (fundo de escala)

# Gerando um sinal que varia entre 0V e 5V (Senoide deslocada e escalonada)
sinal_original = (Vref / 2) + (Vref / 2) * np.sin(2 * np.pi * f * t)

# Casos de estudo solicitados: 3, 4 e 8 bits
bits_N = [3, 4, 8]

plt.figure(figsize=(14, 10))

for i, N in enumerate(bits_N):
    # Cálculos matemáticos
    L = 2**N
    delta_V = Vref / L
    
    # 2. Processo de Quantização
    # Divide a tensão pelo passo (ΔV) e pega a parte inteira (índice do degrau)
    indice_degrau = np.floor(sinal_original / delta_V)
    # Garante que o índice não passe do máximo permitido (L-1)
    indice_degrau = np.clip(indice_degrau, 0, L - 1) 
    # Multiplica pelo passo para obter a tensão quantizada final
    sinal_quantizado = indice_degrau * delta_V
    
    # 3. Cálculo do erro
    erro_quantizacao = sinal_quantizado - sinal_original
    
    # --- Gráficos do Sinal ---
    plt.subplot(3, 2, 2*i + 1)
    plt.plot(t, sinal_original, 'gray', linestyle='--', label='Original')
    plt.step(t, sinal_quantizado, 'b', where='post', label=f'Quantizado N={N}')
    plt.title(f'Sinal - N = {N} (L = {L} níveis, ΔV = {delta_V:.3f} V)')
    plt.ylabel('Amplitude (V)')
    plt.legend(loc='upper right')
    plt.grid(True)
    
    # --- Gráficos do Erro ---
    plt.subplot(3, 2, 2*i + 2)
    plt.plot(t, erro_quantizacao, 'r')
    plt.title(f'Erro de Quantização - N = {N}')
    plt.ylabel('Erro (V)')
    plt.grid(True)

plt.tight_layout()
plt.show()

# Imprimindo tabela de resultados numéricos no terminal
print(" N (bits) | Níveis (L) | Resolução (ΔV) em V | Erro Máximo (aprox) em V")
print("-" * 75)
for N in bits_N:
    L = 2**N
    delta_V = Vref / L
    print(f"    {N}     |    {L:3}     |      {delta_V:.5f}      |      ± {delta_V:5f}")