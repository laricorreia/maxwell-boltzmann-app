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

# Velocidade vetorial padrão
v = np.linspace(0, 4000, 500)

# Interface com múltiplas páginas
st.sidebar.title("Navegação")
pagina = st.sidebar.radio("Escolha a visualização:", ["1. Um gás, uma temperatura", "2. Um gás, duas temperaturas", "3. Dois gases, uma temperatura"])

# Página 1
if pagina == "1. Um gás, uma temperatura":
    st.title("Distribuição de Maxwell-Boltzmann")
    st.markdown("### Página 1: Um gás em uma temperatura")

    massa_molar = st.number_input("Massa molar (g/mol)", value=44.0, step=0.1)
    temperatura = st.number_input("Temperatura (K)", value=288.0, step=1.0)
    M = massa_molar / 1000

    f_MB = F_MB(v, M, temperatura)

    fig, ax = plt.subplots()
    ax.plot(v, f_MB, color='green', label=f"{massa_molar} g/mol a {temperatura} K")
    ax.set_title("Distribuição de Maxwell-Boltzmann")
    ax.set_xlabel("Velocidade (m/s)")
    ax.set_ylabel("F(v)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Página 2
elif pagina == "2. Um gás, duas temperaturas":
    st.title("Distribuição de Maxwell-Boltzmann")
    st.markdown("### Página 2: Um gás em duas temperaturas")

    massa_molar = st.number_input("Massa molar (g/mol)", value=44.0, step=0.1)
    T1 = st.number_input("Temperatura 1 (K)", value=288.0, step=1.0)
    T2 = st.number_input("Temperatura 2 (K)", value=740.0, step=1.0)
    M = massa_molar / 1000

    f1 = F_MB(v, M, T1)
    f2 = F_MB(v, M, T2)

    fig, ax = plt.subplots()
    ax.plot(v, f1, label=f"{massa_molar} g/mol a {T1} K", color='blue')
    ax.plot(v, f2, label=f"{massa_molar} g/mol a {T2} K", color='red')
    ax.set_title("Distribuição para um mesmo gás em duas temperaturas")
    ax.set_xlabel("Velocidade (m/s)")
    ax.set_ylabel("F(v)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Página 3
elif pagina == "3. Dois gases, uma temperatura":
    st.title("Distribuição de Maxwell-Boltzmann")
    st.markdown("### Página 3: Dois gases em uma mesma temperatura")

    massa_molar_1 = st.number_input("Massa molar do gás 1 (g/mol)", value=44.0, step=0.1)
    massa_molar_2 = st.number_input("Massa molar do gás 2 (g/mol)", value=2.0, step=0.1)
    temperatura = st.number_input("Temperatura (K)", value=288.0, step=1.0)

    M1 = massa_molar_1 / 1000
    M2 = massa_molar_2 / 1000

    f1 = F_MB(v, M1, temperatura)
    f2 = F_MB(v, M2, temperatura)

    fig, ax = plt.subplots()
    ax.plot(v, f1, label=f"{massa_molar_1} g/mol", color='purple')
    ax.plot(v, f2, label=f"{massa_molar_2} g/mol", color='orange')
    ax.set_title("Distribuição para dois gases em uma mesma temperatura")
    ax.set_xlabel("Velocidade (m/s)")
    ax.set_ylabel("F(v)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
