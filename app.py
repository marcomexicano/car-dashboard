import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Dashboard de Anuncios de Autos')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de histograma para odometer')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de gráfico de dispersión odometer vs price')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)
