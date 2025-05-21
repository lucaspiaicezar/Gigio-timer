import streamlit as st import random

st.set_page_config(page_title="Simulador do Gigio", page_icon="⏱️", layout="centered")

st.markdown("""

<style>
    body {
        background-color: #FFE082;
    }
    .reportview-container, .main, .block-container {
        background-color: #FFE082 !important;
        color: #3E2723;
    }
    .big-font {
        font-size: 28px !important;
        color: #3E2723;
        text-align: center;
    }
    .stButton>button {
        background-color: #FB8C00;
        color: white;
        padding: 0.5em 1em;
        font-size: 1.2em;
        border-radius: 10px;
    }
    .stNumberInput input {
        background-color: #FFF3E0;
        color: #3E2723;
    }
</style>""", unsafe_allow_html=True)

st.image("gigio_icon.png", width=180)

st.markdown("<div class='big-font'>⏱️ <b>Simulador de Atraso do Gigio</b></div>", unsafe_allow_html=True)

st.write(""" Gigio sempre diz que vai entrar na call em alguns minutos... mas nunca cumpre! Use esta ferramenta para estimar quanto tempo ele realmente vai demorar.

Fórmula usada:

> Tempo Real = Tempo Prometido × R + A



R: Fator aleatório de erro (2 a 5)

A: Ajuste por distração (5 a 15 minutos) """)


tempo_prometido = st.number_input("Digite o tempo prometido pelo Gigio (em minutos):", min_value=1, max_value=120, value=10, step=1)

if st.button("Calcular Tempo Real Estimado"): r = round(random.uniform(2, 5), 2) a = random.randint(5, 15) tempo_real = round(tempo_prometido * r + a)

st.success(f"🕒 O Gigio provavelmente vai entrar em **{tempo_real} minutos**")

with st.expander("Ver detalhes do cálculo"):
    st.markdown(f"- Tempo prometido: **{tempo_prometido} min**")
    st.markdown(f"- Fator de erro (R): **{r}**")
    st.markdown(f"- Ajuste de distração (A): **{a} min**")
    st.markdown(f"- Fórmula aplicada: **{tempo_prometido} × {r} + {a} = {tempo_real} min**")

