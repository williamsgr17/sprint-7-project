import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Visor de datos de anuncios de coches en venta')  # encabezado

# botón que construye un histograma
# hist_button = st.button('Construir histograma')  # crear un botón

# if hist_button:  # al hacer clic en el botón
#     # escribir un mensaje
#     st.write(
#         'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

#     # crear un histograma
#     fig = px.histogram(car_data, x="odometer")

#     # mostrar un gráfico Plotly interactivo
#     st.plotly_chart(fig, use_container_width=True)

# # botón que construye un gráfico de dispersión
# scatter_button = st.button('Construir gráfico de dispersión')  # crear un botón

# if scatter_button:  # al hacer clic en el botón
#     # escribir un mensaje
#     st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

#     # crear un gráfico de fispersión
#     fig_2 = px.scatter(car_data, x="odometer", y='price')

#     # mostrar un gráfico Plotly interactivo
#     st.plotly_chart(fig_2, use_container_width=True)


# reemplazar los botones por casillas de verificación

# crear una casilla de verificación
build_histogram = st.checkbox(
    'Construir un histograma')  # casilla de verificación

if build_histogram:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


# casilla de verificación
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de fispersión
    fig_2 = px.scatter(car_data, x="odometer", y='price')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
