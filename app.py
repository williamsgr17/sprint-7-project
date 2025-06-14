import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
# agregar columna 'manufacturer'
car_data['manufacturer'] = car_data['model'].str.split().str[0]

st.header('💻 VISOR DE DATOS SOBRE ANUNCIOS DE VEHÍCULOS EN VENTA')  # encabezado

st.subheader("Vista previa del dataset")
st.dataframe(car_data.head(10))

st.subheader('📊 Tipos de vehículos por fabricante')

# crear una casilla de verificación
build_bar = st.checkbox(
    # casilla de verificación
    'Mostrar gráfico', key='gráfico de barras')

if build_bar:  # al hacer clic en el botón
    # crear un histograma
    fig = px.bar(car_data, x="manufacturer", color='type')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.subheader('🚗 Histograma de `condición` vs `año del modelo`')

# crear una casilla de verificación
build_histogram = st.checkbox(
    'Mostrar histograma')  # casilla de verificación

if build_histogram:  # al hacer clic en el botón
    # crear un histograma
    fig = px.histogram(car_data, x="model_year", color='condition')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


st.subheader(
    '💲Distribución de los kilometros del vehículo en relación con su precio')

build_scatter = st.checkbox(
    'Mostrar gráfico', key='gráfico de dispersión')  # casilla de verificación

if build_scatter:  # al hacer clic en el botón
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
