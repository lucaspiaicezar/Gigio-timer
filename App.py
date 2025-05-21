import streamlit as st
import random

st.set_page_config(page_title="Simulador do Gigio", page_icon="⏱️", layout="centered")

# Estilo leve e legível
st.markdown("""
    <style>
        html, body {
            background-color: #FFFDE7;
            color: #3E2723;
            font-family: 'Arial', sans-serif;
        }
        .big-title {
            font-size: 28px;
            font-weight: bold;
            text-align: center;
            color: #3E2723;
        }
        .stButton>button {
            background-color: #F57C00;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 8px 16px;
        }
        .stNumberInput input {
            background-color: #FFF3E0;
            color: #3E2723;
        }
    </style>
""", unsafe_allow_html=True)

# Ícone do Gigio
st.image("gigio_icon.png", width=160)

st.markdown("<div class='big-title'>⏱️ Simulador de Atraso do Gigio</div>", unsafe_allow_html=True)

st.write("Gigio sempre promete que vai entrar em alguns minutos... mas será mesmo? Vamos calcular com base no histórico duvidoso dele!")

st.markdown("**Fórmula usada:**\n\n> Tempo Real = Tempo Prometido × R + A")

tempo_prometido = st.number_input("Quanto tempo o Gigio prometeu (em minutos)?", min_value=1, max_value=120, value=10)

if st.button("Calcular Tempo Real Estimado"):
    r = round(random.uniform(2, 5), 2)
    a = random.randint(5, 15)
    tempo_real = round(tempo_prometido * r + a)

    st.success(f"🕒 O Gigio provavelmente vai entrar em **{tempo_real} minutos**.")

    with st.expander("Detalhes do cálculo"):
        st.write(f"Tempo prometido: **{tempo_prometido} min**")
        st.write(f"Fator de erro aleatório (R): **{r}**")
        st.write(f"Ajuste de distração (A): **{a} min**")
        st.write(f"**Fórmula:** {tempo_prometido} × {r} + {a} = **{tempo_real} min**")
