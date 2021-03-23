import streamlit as st

def app():
    st.write('Bem-vindo à calculadora de tamanho de amostra para testes A/B ou Multivariantes.')
    st.write('Selecione acima o tipo de teste que irá realizar.')

    # expander = st.beta_expander("FAQ")
    # expander.write("Q: Qual comparação usar? Média ou proporção?")
    # expander.write("A: ")