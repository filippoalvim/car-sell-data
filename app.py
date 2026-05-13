import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')

st.header('Análise de Anúncios de Venda de Carros')
st.write('Explore o conjunto de dados de veículos usando os gráficos abaixo.')

build_histogram = st.checkbox('Criar histograma de quilometragem (odometer)')

if build_histogram:
    st.write('Distribuição da quilometragem dos veículos anunciados')
    fig = px.histogram(car_data, x='odometer', nbins=50,
                       title='Distribuição da Quilometragem',
                       labels={'odometer': 'Quilometragem (milhas)'})
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Criar gráfico de dispersão: preço vs quilometragem')

if build_scatter:
    st.write('Relação entre preço e quilometragem dos veículos')
    fig2 = px.scatter(car_data, x='odometer', y='price',
                      title='Preço vs Quilometragem',
                      labels={'odometer': 'Quilometragem (milhas)', 'price': 'Preço (USD)'},
                      opacity=0.5)
    st.plotly_chart(fig2, use_container_width=True)
