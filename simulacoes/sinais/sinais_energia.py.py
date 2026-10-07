import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. Análise do Sinal de Energia (Pulso Retangular)
# ---------------------------------------------------------
n_energia = np.arange(-10, 15)
# Sinal x1[n] = 2 para 0 <= n <= 4, e 0 para os demais
x1 = np.where((n_energia >= 0) & (n_energia <= 4), 2.0, 0.0)

# Cálculo numérico da Energia (Soma dos quadrados)
E_num = np.sum(np.abs(x1)**2)

# Cálculo numérico da Potência no intervalo total analisado
# O len(n_energia) simula o 2N+1 do intervalo limitado
P_x1_estimada = E_num / len(n_energia) 

# ---------------------------------------------------------
# 2. Análise do Sinal de Potência (Senoide)
# ---------------------------------------------------------
N_pot = 1000  # Intervalo de simulação -N até N
n_potencia = np.arange(-N_pot, N_pot + 1)
# Sinal x2[n] = 2 * sen(pi * n / 2)
x2 = 2.0 * np.sin(np.pi * n_potencia / 2.0)

# Cálculo da energia ao longo dessa janela gigantesca (E tenderá a infinito)
E_x2_infinita = np.sum(np.abs(x2)**2)

# Cálculo numérico da Potência (Média da energia no intervalo 2N+1)
P_num = E_x2_infinita / (2 * N_pot + 1)

# ---------------------------------------------------------
# Apresentação dos Resultados
# ---------------------------------------------------------
plt.figure(figsize=(12, 6))

# Gráfico Sinal de Energia
plt.subplot(1, 2, 1)
plt.stem(n_energia, x1, linefmt='b-', markerfmt='bo', basefmt='k-')
plt.title('Sinal de Energia: Pulso Retangular')
plt.xlabel('n')
plt.ylabel('x1[n]')
plt.grid(True)

# Gráfico Sinal de Potência (Mostrando apenas um pequeno trecho para visualização)
plt.subplot(1, 2, 2)
trecho = (n_potencia >= -5) & (n_potencia <= 5)
plt.stem(n_potencia[trecho], x2[trecho], linefmt='r-', markerfmt='ro', basefmt='k-')
plt.title('Sinal de Potência: Senoide (Trecho visível)')
plt.xlabel('n')
plt.ylabel('x2[n]')
plt.grid(True)

plt.tight_layout()
plt.show()

# Imprimindo verificações no terminal
print("--- Validação Numérica ---")
print(f"Sinal x1 (Energia) -> Energia Total = {E_num:.2f} | Potência Estimada = {P_x1_estimada:.4f} (Tende a 0 se intervalo crescer)")
print(f"Sinal x2 (Potência) -> Energia na janela analisada = {E_x2_infinita:.2f} (Explodindo para infinito) | Potência Média = {P_num:.4f}")