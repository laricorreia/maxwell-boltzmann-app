
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Constante dos gases ideais
R = 8.314  # J/mol·K

# Funções da distribuição de Maxwell-Boltzmann
def fator_pre_exp(v, M, T):
    return 4 * np.pi * (M / (2 * np.pi * R * T)) ** (3 / 2) * v ** 2

def fator_exp(v, M, T):
    return np.exp(-M * v ** 2 / (2 * R * T))

def F_MB(v, M, T):
    return fator_pre_exp(v, M, T) * fator_exp(v, M, T)

# Interface
st.title("Distribuição de Maxwell-Boltzmann Interativa")
st.markdown("Insira os valores para temperatura e massa molar do gás:")

# Entradas do usuário
massa_molar = st.number_input("Massa molar (g/mol)", value=44.0, step=0.1)
temperatura = st.number_input("Temperatura (K)", value=288.0, step=1.0)

# Conversão g/mol → kg/mol
M = massa_molar / 1000

# Vetor de velocidades
v = np.linspace(0, 4000, 500)

# Cálculos
f_pre = fator_pre_exp(v, M, temperatura)
f_exp = fator_exp(v, M, temperatura)
f_total = F_MB(v, M, temperatura)

# Gráfico 1 - Pré-exponencial
fig1, ax1 = plt.subplots()
ax1.plot(v, f_pre, label="Pré-Exponencial")
ax1.set_xlabel("Velocidade (m/s)")
ax1.set_ylabel("Valor")
ax1.set_title("Pré-exponencial × Velocidade")
ax1.grid(True)
st.pyplot(fig1)

# Gráfico 2 - Exponencial
fig2, ax2 = plt.subplots()
ax2.plot(v, f_exp, color='orange', label="Exponencial")
ax2.set_xlabel("Velocidade (m/s)")
ax2.set_ylabel("Valor")
ax2.set_title("Exponencial × Velocidade")
ax2.grid(True)
st.pyplot(fig2)

# Gráfico 3 - Distribuição F(v)
fig3, ax3 = plt.subplots()
ax3.plot(v, f_total, color='green', label="F(v)")
ax3.set_xlabel("Velocidade (m/s)")
ax3.set_ylabel("Distribuição")
ax3.set_title("Distribuição de Maxwell-Boltzmann")
ax3.grid(True)
st.pyplot(fig3)
