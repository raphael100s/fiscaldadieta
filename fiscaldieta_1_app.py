import streamlit as st

def calcular_tmb():
    st.title("Calculadora de Taxa Metabólica Basal (TMB) e Meta de Dieta de Pontos")

    # Pergunta o sexo
    sexo = st.radio("Qual é o seu sexo?", ('Masculino', 'Feminino'))
    idade = st.number_input("Qual é a sua idade em anos?", min_value=0, value=0)
    peso = st.number_input("Qual é o seu peso em kg?", min_value=0.0, value=0.0)
    altura = st.number_input("Qual é a sua altura em cm?", min_value=0.0, value=0.0)

    # Calcula a TMB com base no sexo
    if sexo == 'Masculino':
        tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
    else:
        tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

    st.write(f"Sua TMB é aproximadamente {tmb:.2f} calorias por dia.")

    # Nível de atividade
    nivel_atividade = st.selectbox(
        "Escolha o seu nível de atividade física:",
        ["Sedentário", "Levemente ativo", "Moderadamente ativo", "Muito ativo", "Extremamente ativo"]
    )

    fatores_atividade = {
        "Sedentário": 1.2,
        "Levemente ativo": 1.375,
        "Moderadamente ativo": 1.55,
        "Muito ativo": 1.725,
        "Extremamente ativo": 1.9
    }

    gasto_total = tmb * fatores_atividade[nivel_atividade]
    st.write(f"Seu gasto calórico total aproximado é de {gasto_total:.2f} calorias por dia.")

    # Calcula a meta de calorias para a dieta
    meta_calorias = max(gasto_total - 1000, 1000 if sexo == 'Feminino' else 1200)
    st.write(f"Sua meta calórica para a dieta é de aproximadamente {meta_calorias:.2f} calorias por dia.")

    # Calcula a meta em pontos
    meta_pontos = meta_calorias / 3.6
    st.write(f"Sua meta em pontos para a dieta é de aproximadamente {meta_pontos:.2f} pontos por dia.")

calcular_tmb()
