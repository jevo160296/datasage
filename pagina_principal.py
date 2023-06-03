import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from streamlit_lottie import st_lottie


def main():
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # Establecer logo
    st.sidebar.image("content/Logo.png")

    st.sidebar.header("Filtros")
    lenguaje = st.sidebar.multiselect(
        "Lenguajes",
        options=["Scala", "Python", "SQL", "R", "Java"],
        default=["Scala", "Python", "SQL", "R", "Java"],
    )

    lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_dews3j6m.json")

    # Definir la paleta de colores de morado
    purple_palette = ['#6B52AE', '#8357B4', '#9D5CC1', '#B861C9', '#D266D0']

    # Establecer la paleta de colores de morado
    sns.set_palette(purple_palette)

    # Título de la página
    st.markdown(
        '<h1 style="text-align: center; font-weight: bold;">Bienvenido a DataSage 🧙‍♂️</h1>',
        unsafe_allow_html=True)

    # Descripción de la empresa
    st.markdown(
        'En DataSage, ofrecemos servicios de asesoramiento en ingeniería de datos para ayudarte a gestionar y analizar tus datos de manera efectiva.')

    with st.container():

        # Servicios ofrecidos
        st.write("-----")

        st.markdown('<h2 style="text-align: center;">Nuestros servicios</h2>', unsafe_allow_html=True)

        left_column, right_column = st.columns(2)

        st.write("-----")

        with left_column:
            # Servicios ofrecidos

            st.markdown('- Diseño y optimización de arquitecturas de datos')
            st.markdown('- Integración y transformación de datos')
            st.markdown('- Análisis y visualización de datos')
            st.markdown('- Implementación de pipelines de datos')

        with right_column:
            st_lottie(lottie_coding, height=300, key='data')

    # Gráfico de ejemplo - Distribución de datos
    st.markdown('<h2 style="text-align: center;">Distribución de datos</h2>', unsafe_allow_html=True)

    with st.container():

        left_column, right_column = st.columns(2)

        st.write("-----")

        with left_column:

            # Generar datos de ejemplo
            data1 = pd.DataFrame({
                'Año': [2019, 2020, 2021, 2022, 2023],
                'Ingresos': [50000, 60000, 75000, 90000, 110000]
            })

            # Widget de selección del tipo de gráfico
            chart_type1 = st.selectbox('Selecciona el tipo de gráfico', ('bar', 'line', 'histogram'), key='chart_type1')

            # Widget de selección del eje x
            x_axis1 = 'Año'

        with right_column:
            # Crear gráfico dinámico
            fig1, ax1 = plt.subplots()

            if chart_type1 == 'bar':
                sns.barplot(data=data1, x=x_axis1, y='Ingresos', ax=ax1)
                plt.ylabel('Ingresos')
            elif chart_type1 == 'line':
                sns.lineplot(data=data1, x=x_axis1, y='Ingresos', ax=ax1)
                plt.ylabel('Ingresos')
            elif chart_type1 == 'pie':
                ax1.pie(data1['Ingresos'], labels=data1['Año'], autopct='%1.1f%%')
                ax1.set_aspect('equal')
                ax1.set_title('Distribución de ingresos por año')
            elif chart_type1 == 'histogram':
                sns.histplot(data=data1, x='Ingresos', kde=True, bins=5, ax=ax1)
                plt.xlabel('Ingresos')
                plt.ylabel('Frecuencia')
                plt.title('Histograma de ingresos')

            plt.xlabel(x_axis1)

            # Mostrar gráfico en la página
            st.pyplot(fig1)

    # Gráfico de ejemplo - Análisis de datos
    st.markdown('<h2 style="text-align: center;">Análisis de datos</h2>', unsafe_allow_html=True)

    with st.container():

        left_column, right_column = st.columns(2)

        st.write("-----")

        with left_column:

            # Generar datos de ejemplo

            data2 = pd.DataFrame({
                'Lenguaje': ['Python', 'R', 'SQL', 'Java', 'Scala'],
                'Popularidad': [80, 60, 40, 30, 20]
            })

            data2 = data2[data2['Lenguaje'].isin(lenguaje)]

            # Widget de selección del tipo de gráfico

            chart_type2 = st.selectbox('Selecciona el tipo de gráfico', ('bar', 'line', 'histogram'), key='chart_type2')

            # Widget de selección del eje y
            y_axis = 'Lenguaje'

        with right_column:

            # Crear gráfico dinámico
            fig2, ax2 = plt.subplots()

            if chart_type2 == 'bar':
                sns.barplot(data=data2, x='Popularidad', y=y_axis, ax=ax2)
                plt.xlabel('Popularidad')
            elif chart_type2 == 'line':
                sns.lineplot(data=data2, x='Popularidad', y=y_axis, ax=ax2)
                plt.xlabel('Popularidad')
            elif chart_type2 == 'pie':
                ax2.pie(data2['Popularidad'], labels=data2['Lenguaje'], autopct='%1.1f%%')
                ax2.set_aspect('equal')
                ax2.set_title('Distribución de popularidad por lenguaje')
            elif chart_type2 == 'histogram':
                sns.histplot(data=data2, x='Popularidad', kde=True, bins=5, ax=ax2)
                plt.xlabel('Popularidad')
                plt.ylabel('Frecuencia')
                plt.title('Histograma de popularidad')

            plt.ylabel(y_axis)

            # Mostrar gráfico en la página
            st.pyplot(fig2)

    # Información de contacto
    st.markdown('<h2 style="text-align: center;">Contáctanos</h2>', unsafe_allow_html=True)
    st.markdown('Si estás interesado en nuestros servicios, por favor, no dudes en ponerte en contacto con nosotros:')
    st.markdown('- Teléfono: 6067524281')
    st.markdown('- Correo electrónico: info@datasage.com')


# Ejecuta tu aplicación de Streamlit
if __name__ == '__main__':
    main()
