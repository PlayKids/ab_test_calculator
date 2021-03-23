import streamlit as st
from multiapp import MultiApp
from apps import home, proportions, means

app = MultiApp()

st.title('Calculadora de Tamanho de Amostra - Teste AB')

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Comparação de duas Proporções", proportions.app)
app.add_app("Comparação de duas Médias", means.app)
# The main app
app.run()