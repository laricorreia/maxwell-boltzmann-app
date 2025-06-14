pagina = st.sidebar.radio("Escolha a visualização:", [
    "0. Introdução",
    "1. Um gás, uma temperatura",
    "2. Um gás, duas temperaturas",
    "3. Dois gases, uma temperatura"
])
# Página 0 - Introdução
if pagina == "0. Introdução":
    st.title("Distribuição de Maxwell-Boltzmann")
    st.markdown("### Bem-vindo ao Simulador de Maxwell-Boltzmann 🧪")

    st.markdown(r'''
A **Distribuição de Maxwell-Boltzmann** é uma função estatística que descreve como as velocidades das partículas (gases ideais) se distribuem a uma dada temperatura. Essa distribuição foi formulada por **James Clerk Maxwell** e posteriormente generalizada por **Ludwig Boltzmann**, sendo uma das fundações da **termodinâmica estatística**.

Essa distribuição é fundamental para prever:
- A **probabilidade de uma molécula atingir certa velocidade**
- A **influência da temperatura** sobre a energia cinética das partículas
- A **capacidade de um planeta reter gases em sua atmosfera** (como no caso da Terra e de Vênus)

A equação que representa a distribuição é:

\\[
F(v) = 4\\pi \\left(\\frac{M}{2\\pi RT}\\right)^{3/2} v^2 \\cdot e^{-\\frac{Mv^2}{2RT}}
\\]

Onde:
- \\(F(v)\\): densidade de probabilidade de velocidade \\(v\\)
- \\(M\\): massa molar do gás (em kg/mol)
- \\(T\\): temperatura em kelvin
- \\(R\\): constante universal dos gases ideais (8.314 J/mol·K)

Essa equação é composta por:
- Um **fator pré-exponencial**: relacionado ao crescimento quadrático com a velocidade (\\(v^2\\))
- Um **fator exponencial**: que decresce rapidamente com o aumento de \\(v\\)

---

### 🔍 O que você pode explorar neste app:

- **Página 1** – Visualizar um gás único em uma temperatura fixa
- **Página 2** – Comparar o mesmo gás em duas temperaturas diferentes
- **Página 3** – Comparar dois gases diferentes em uma mesma temperatura

Cada página gera automaticamente:
- O **fator pré-exponencial** vs velocidade
- O **fator exponencial** vs velocidade
- A **função completa F(v)** (distribuição de velocidades)

Use os controles da barra lateral para inserir os valores desejados e estudar o comportamento das moléculas!
''')


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

# Vetor de velocidades
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

    f_pre = fator_pre_exp(v, M, temperatura)
    f_exp = fator_exp(v, M, temperatura)
    f_MB = F_MB(v, M, temperatura)

    fig1, ax1 = plt.subplots()
    ax1.plot(v, f_pre, label="Pré-Exponencial")
    ax1.set_title("Fator Pré-Exponencial × Velocidade")
    ax1.set_xlabel("Velocidade (m/s)")
    ax1.set_ylabel("Valor")
    ax1.grid(True)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.plot(v, f_exp, color='orange', label="Exponencial")
    ax2.set_title("Fator Exponencial × Velocidade")
    ax2.set_xlabel("Velocidade (m/s)")
    ax2.set_ylabel("Valor")
    ax2.grid(True)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    ax3.plot(v, f_MB, color='green', label="F(v)")
    ax3.set_title("Distribuição de Maxwell-Boltzmann")
    ax3.set_xlabel("Velocidade (m/s)")
    ax3.set_ylabel("F(v)")
    ax3.grid(True)
    st.pyplot(fig3)

# Página 2
elif pagina == "2. Um gás, duas temperaturas":
    st.title("Distribuição de Maxwell-Boltzmann")
    st.markdown("### Página 2: Um gás em duas temperaturas")

    massa_molar = st.number_input("Massa molar (g/mol)", value=44.0, step=0.1)
    T1 = st.number_input("Temperatura 1 (K)", value=288.0, step=1.0)
    T2 = st.number_input("Temperatura 2 (K)", value=740.0, step=1.0)
    M = massa_molar / 1000

    f_pre1 = fator_pre_exp(v, M, T1)
    f_exp1 = fator_exp(v, M, T1)
    f_MB1 = F_MB(v, M, T1)

    f_pre2 = fator_pre_exp(v, M, T2)
    f_exp2 = fator_exp(v, M, T2)
    f_MB2 = F_MB(v, M, T2)

    fig1, ax1 = plt.subplots()
    ax1.plot(v, f_pre1, label=f"Pré-exp. T={T1}K", color="blue")
    ax1.plot(v, f_pre2, label=f"Pré-exp. T={T2}K", color="red")
    ax1.set_title("Fator Pré-Exponencial × Velocidade")
    ax1.set_xlabel("Velocidade (m/s)")
    ax1.set_ylabel("Valor")
    ax1.legend()
    ax1.grid(True)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.plot(v, f_exp1, label=f"Exp. T={T1}K", color="blue")
    ax2.plot(v, f_exp2, label=f"Exp. T={T2}K", color="red")
    ax2.set_title("Fator Exponencial × Velocidade")
    ax2.set_xlabel("Velocidade (m/s)")
    ax2.set_ylabel("Valor")
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    ax3.plot(v, f_MB1, label=f"F(v) T={T1}K", color="blue")
    ax3.plot(v, f_MB2, label=f"F(v) T={T2}K", color="red")
    ax3.set_title("Distribuição de Maxwell-Boltzmann")
    ax3.set_xlabel("Velocidade (m/s)")
    ax3.set_ylabel("F(v)")
    ax3.legend()
    ax3.grid(True)
    st.pyplot(fig3)

# Página 3
elif pagina == "3. Dois gases, uma temperatura":
    st.title("Distribuição de Maxwell-Boltzmann")
    st.markdown("### Página 3: Dois gases em uma mesma temperatura")

    massa_molar_1 = st.number_input("Massa molar do gás 1 (g/mol)", value=44.0, step=0.1)
    massa_molar_2 = st.number_input("Massa molar do gás 2 (g/mol)", value=2.0, step=0.1)
    temperatura = st.number_input("Temperatura (K)", value=288.0, step=1.0)

    M1 = massa_molar_1 / 1000
    M2 = massa_molar_2 / 1000

    f_pre1 = fator_pre_exp(v, M1, temperatura)
    f_exp1 = fator_exp(v, M1, temperatura)
    f_MB1 = F_MB(v, M1, temperatura)

    f_pre2 = fator_pre_exp(v, M2, temperatura)
    f_exp2 = fator_exp(v, M2, temperatura)
    f_MB2 = F_MB(v, M2, temperatura)

    fig1, ax1 = plt.subplots()
    ax1.plot(v, f_pre1, label=f"Pré-exp. {massa_molar_1} g/mol", color="purple")
    ax1.plot(v, f_pre2, label=f"Pré-exp. {massa_molar_2} g/mol", color="orange")
    ax1.set_title("Fator Pré-Exponencial × Velocidade")
    ax1.set_xlabel("Velocidade (m/s)")
    ax1.set_ylabel("Valor")
    ax1.legend()
    ax1.grid(True)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    ax2.plot(v, f_exp1, label=f"Exp. {massa_molar_1} g/mol", color="purple")
    ax2.plot(v, f_exp2, label=f"Exp. {massa_molar_2} g/mol", color="orange")
    ax2.set_title("Fator Exponencial × Velocidade")
    ax2.set_xlabel("Velocidade (m/s)")
    ax2.set_ylabel("Valor")
    ax2.legend()
    ax2.grid(True)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    ax3.plot(v, f_MB1, label=f"F(v) {massa_molar_1} g/mol", color="purple")
    ax3.plot(v, f_MB2, label=f"F(v) {massa_molar_2} g/mol", color="orange")
    ax3.set_title("Distribuição de Maxwell-Boltzmann")
    ax3.set_xlabel("Velocidade (m/s)")
    ax3.set_ylabel("F(v)")
    ax3.legend()
    ax3.grid(True)
    st.pyplot(fig3)
