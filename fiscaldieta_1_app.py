import streamlit as st

def calcular_tmb():
    st.title("Calculadora de Taxa Metabólica Basal (TMB) e Meta de Dieta de Pontos")

    # Pergunta o sexo
    sexo = st.radio("Qual é o seu sexo?", ('Masculino', 'Feminino'))
    idade = st.number_input("Qual é a sua idade em anos?", min_value=0, value=None, step=1)
    peso = st.number_input("Qual é o seu peso em kg?", min_value=0.0, value=None, step=0.1)
    altura = st.number_input("Qual é a sua altura em cm?", min_value=0.0, value=None, step=0.1)

    # Verifica se os campos necessários estão preenchidos
    if idade is not None and peso is not None and altura is not None:
        # Calcula a TMB com base no sexo
        if sexo == 'Masculino':
            tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * idade)
        else:
            tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * idade)

        st.write(f"**Sua TMB é aproximadamente {tmb:.2f} calorias por dia.**")

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
        st.write(f"**Seu gasto calórico total aproximado é de {gasto_total:.2f} calorias por dia.**")

        # Calcula a meta de calorias para a dieta
        meta_calorias = max(gasto_total - 1000, 1000 if sexo == 'Feminino' else 1200)
        meta_pontos = meta_calorias / 3.6

        # Exibindo metas em um quadro de destaque com fundo amarelo e texto preto
        st.markdown(
            f'''
            <div style="border: 2px solid #FFD700; padding: 20px; border-radius: 10px; background-color: #FFFFE0; color: black;">
                <h3 style="text-align: center;">Metas de Dieta</h3>
                <p style="text-align: center; font-size: 20px;"><b>Meta calórica diária: {meta_calorias:.2f} calorias</b></p>
                <p style="text-align: center; font-size: 20px;"><b>Meta diária em pontos: {meta_pontos:.2f} pontos</b></p>
            </div>
            ''', unsafe_allow_html=True
        )
    else:
        st.write("Por favor, preencha todos os campos para calcular sua TMB e metas de dieta.")

calcular_tmb()
