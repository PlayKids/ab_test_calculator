import streamlit as st
import statsmodels.stats.api as sms
from statsmodels.stats.power import zt_ind_solve_power
from math import comb


def sample_size_proportions(baseline_rate,
                            minimum_detectable_effect, 
                            effect_is_relative,
                            confidence, 
                            test_power,
                            variant_number
                            ):
    
    practical_significance = minimum_detectable_effect / 100.
    confidence_level = 1 - (float(confidence)/100.)
    if variant_number > 2:
        combinations = comb(variant_number, 2)
        confidence_level = confidence_level / combinations
    sensitivity = test_power / 100.
    baseline_rate = baseline_rate / 100.
    lift = practical_significance*baseline_rate if effect_is_relative else practical_significance

    effect_size = sms.proportion_effectsize(baseline_rate, 
                                            baseline_rate + lift)
    sample_size = zt_ind_solve_power(effect_size=effect_size, 
                                     power=sensitivity,
                                     alpha=confidence_level, 
                                     ratio=1)
    
    return round(sample_size)


def app():
    st.header("Comparação de duas Proporções (ou taxas)")

    variant_number = st.selectbox("Número de variantes (incluindo controle): ", options=range(2, 6))
    baseline_rate = st.number_input("Proporção atual (em %): ", 0., 100., 50.)
    minimum_detectable_effect = st.number_input("Efeito mínimo que deseja detectar no teste (em %): ", 0., 100., 5.)
    effect_is_relative = st.selectbox("O efeito mínimo é relativo?", options=[True, False])
    confidence = st.number_input("Grau de confiança do teste (em %): ", 90., 100., 95.)
    test_power = st.number_input("Poder do teste (em %): ", 80., 100., 80.)

    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Calcular')
    if pressed:
        sample_size = sample_size_proportions(baseline_rate, 
                                    minimum_detectable_effect, 
                                    effect_is_relative, 
                                    confidence, 
                                    test_power, 
                                    variant_number)

        right_column.subheader(f"Você vai precisar de {round(sample_size)} amostras por variante!")