import streamlit as st
import random

st.set_page_config(page_title="Simulador do Gigio", page_icon="⏱️", layout="centered")

# Estilo com paleta suave e legível
st.markdown("""
<style>
    html, body, [class*="css"] {
        background-color: #FFF8E1;
        color: #3E2723;
        font-family: 'Segoe UI', sans-serif;
    }
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        color: #3E2723;
        text-align: center;
        margin-bottom: 10px;
    }
    .stButton>button {
        background-color: #FB8C00;
        color: white;
        font-size: 1.1em;
        padding: 0.6em 1.2em;
        border-radius: 10px;
        margin-top: 10px;
    }
    .stNumberInput input {
        background-color: #FFF3E0;
        color: #3E2723;
    }
</style>
""", unsafe_allow_html=True)

# Ícone do Gigio
st.image("gigio_icon.png", width=160)

st.markdown("<div class='big-font'>⏱️ Simulador de Atraso do Gigio</div>", unsafe_allow_html=True)

st.write("""
**Gigio** sempre diz que vai entrar na call em alguns minutos... mas nunca cumpre!  
Use esta ferramenta para estimar quanto tempo ele **realmente** vai demorar.

**Fórmula usada:**

> Tempo Real = Tempo Prometido × R + A  
> R = Fator de erro aleatório (2 a 5)  
> A = Ajuste por distração (5 a 15 min)
""")

tempo_prometido = st.number_input(
    "Quanto tempo o Gigio prometeu (em minutos)?",
    min_value=1, max_value=120, value=10, step=1
)

if st.button("Calcular Tempo Real Estimado"):
    r = round(random.uniform(2, 5), 2)
    a = random.randint(5, 15)
    tempo_real = round(tempo_prometido * r + a)

    st.success(f"🕒 O Gigio provavelmente vai entrar em **{tempo_real} minutos**.")

    with st.expander("Detalhes do cálculo"):
        st.markdown(f"- Tempo prometido: **{tempo_prometido} min**")
        st.markdown(f"- Fator de erro (R): **{r}**")
        st.markdown(f"- Ajuste de distração (A): **{a} min**")
        st.markdown(f"- Fórmula: `{tempo_prometido} × {r} + {a} = {tempo_real}`")
