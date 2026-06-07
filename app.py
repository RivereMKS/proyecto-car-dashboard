import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Leer los datos desde la carpeta notebooks
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# 2. Crear el encabezado de la aplicación web
st.header('Cuadro de Mandos de Anuncios de Venta de Coches')

# 3. Crear las casillas de verificación (Desafío extra)
build_histogram = st.checkbox('Mostrar Histograma de Kilometraje (Odometer)')
build_scatter = st.checkbox(
    'Mostrar Gráfico de Dispersión (Kilometraje vs Precio)')

# --- LÓGICA PARA EL HISTOGRAMA ---
if build_histogram:
    st.write('Generando histograma para el conjunto de datos...')
    # Crear el histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el gráfico interactivo en la app web
    st.plotly_chart(fig_hist, use_container_width=True)

# --- LÓGICA PARA EL GRÁFICO DE DISPERSIÓN ---
if build_scatter:
    st.write('Generando gráfico de dispersión para el conjunto de datos...')
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Mostrar el gráfico interactivo en la app web
    st.plotly_chart(fig_scatter, use_container_width=True)
