import streamlit as st
from statsmodels.stats.power import zt_ind_solve_power
from math import comb


def sample_size_means(baseline_metric,
                      minimum_detectable_effect, 
                      confidence, 
                      test_power,
                      metric_sigma,
                      variant_number
                      ):
    
    confidence_level = 1 - (float(confidence)/100.)
    if variant_number > 2:
        combinations = comb(variant_number, 2)
        confidence_level = confidence_level / combinations

    sensitivity = test_power / 100.
    baseline_metric = baseline_metric
    lift = baseline_metric * (minimum_detectable_effect/100.)
    new_mean = baseline_metric + lift

    # difference between the two means divided by the standard deviation
    effect_size = (new_mean - baseline_metric) / metric_sigma 
    sample_size = zt_ind_solve_power(effect_size=effect_size, 
                                     power=sensitivity,
                                     alpha=confidence_level, 
                                     ratio=1)
    
    return round(sample_size)

def app():
    st.header("Comparação de duas Médias (valores absolutos)")

    variant_number = st.selectbox("Número de variantes (incluindo controle): ", options=range(2, 6))
    baseline_metric = st.number_input("Métrica atual: ", 0., 100., 10.)
    metric_standard_deviation = st.number_input("Desvio Padrão da Métrica atual:  ", 0., 1000., 5.)
    minimum_detectable_effect = st.number_input("Efeito mínimo que deseja detectar no teste (em %): ", 0., 100., 5.)
    confidence = st.number_input("Grau de confiança do teste (em %): ", 90., 100., 95.)
    test_power = st.number_input("Poder do teste (em %): ", 80., 100., 80.)

    left_column, right_column = st.beta_columns(2)
    pressed = left_column.button('Calcular')
    if pressed:
        sample_size = sample_size_means(baseline_metric,
                                    minimum_detectable_effect, 
                                    confidence, 
                                    test_power,
                                    metric_standard_deviation,
                                    variant_number)

        right_column.subheader(f"Você vai precisar de {round(sample_size)} amostras por variante!")