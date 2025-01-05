# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 12:20:39 2025

@author: rjime
"""

import pandas as pd

# Datos de comportamiento de neumáticos en Bahréin
compound_durations = {
    "C3": {"Seco": 27, "Lluvia": 22, "Lluvia Extrema": 20},
    "C2": {"Seco": 36, "Lluvia": 22, "Lluvia Extrema": 20},
    "C1": {"Seco": 41, "Lluvia": 22, "Lluvia Extrema": 20},
    "CI": {"Seco": 22, "Lluvia": 22, "Lluvia Extrema": 20},
    "CW": {"Seco": 20, "Lluvia": 20, "Lluvia Extrema": 20}
}

compound_time_differences = {
    "C3": {"Seco": 0.000, "Lluvia": 10.946, "Lluvia Extrema": 14.527},
    "C2": {"Seco": 0.479, "Lluvia": 10.946, "Lluvia Extrema": 14.527},
    "C1": {"Seco": 0.718, "Lluvia": 10.946, "Lluvia Extrema": 14.527},
    "CI": {"Seco": 4.260, "Lluvia": 0.000, "Lluvia Extrema": 2.057},
    "CW": {"Seco": 5.905, "Lluvia": 1.351, "Lluvia Extrema": 0.000}
}

# Cargar el archivo con el separador correcto
file_path = "C:/Users/rjime/Desktop/TFG- BA/Anteproyecto/Fuentes de las BDDD/Propias/Circuits_specifics.csv"
circuits_data_df = pd.read_csv(file_path, sep=';')

# Crear un DataFrame para almacenar los resultados
compounds = []

for _, circuit in circuits_data_df.iterrows():
    for compound, durations in compound_durations.items():
        for condition, laps in durations.items():
            # Ajuste de durabilidad según vueltas del circuito
            adjusted_laps = min(laps, circuit["Nº vueltas"] * (laps / 57))  # 57 vueltas del circuito de referencia
            compounds.append({
                "Circuito": circuit["Nombre de GP"],
                "Compuesto": compound,
                "Estado de pista": condition,
                "Duración Estimada (Vueltas)": adjusted_laps,
                "Dif. con C3 (s)": compound_time_differences[compound][condition] - compound_time_differences["C3"][condition],
                "Dif. con C2 (s)": compound_time_differences[compound][condition] - compound_time_differences["C2"][condition],
                "Dif. con C1 (s)": compound_time_differences[compound][condition] - compound_time_differences["C1"][condition],
                "Dif. con CI (s)": compound_time_differences[compound][condition] - compound_time_differences["CI"][condition],
                "Dif. con CW (s)": compound_time_differences[compound][condition] - compound_time_differences["CW"][condition]
            })

# Convertir a DataFrame
compounds_df = pd.DataFrame(compounds)

# Guardar como archivo CSV
output_path = "compuestos_neumaticos_f1.csv"
compounds_df.to_csv(output_path, index=False)

print(f"Archivo generado: {output_path}")
