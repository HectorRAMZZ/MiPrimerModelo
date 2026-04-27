import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Configuración de la página
st.set_page_config(page_title="Clasificador Iris", page_icon="🌸")

st.title("🌸 Clasificador de Flores Iris")
st.markdown("""
Esta aplicación pone a prueba modelos de Machine Learning (KNN y SVM) entrenados para predecir 
la especie de una flor Iris basándose en las medidas de sus sépalos y pétalos.
""")

# Función para cargar los modelos (el decorador @st.cache_resource evita recargas innecesarias)
@st.cache_resource
def cargar_modelos():
    knn = joblib.load('modelo_iris_knn.pkl')
    svm = joblib.load('modelo_iris_svm.pkl')
    return knn, svm

# Intentar cargar los modelos
try:
    modelo_knn, modelo_svm = cargar_modelos()
    modelos_listos = True
except FileNotFoundError:
    st.error("⚠️ No se encontraron los archivos .pkl. Asegúrate de que 'modelo_iris_knn.pkl' y 'modelo_iris_svm.pkl' estén en el mismo directorio que este script.")
    modelos_listos = False

if modelos_listos:
    # --- BARRA LATERAL: ENTRADA DE DATOS ---
    st.sidebar.header("📏 Medidas de la Flor")
    
    # Sliders para capturar las características de la flor
    sepal_length = st.sidebar.slider("Longitud del Sépalo (cm)", min_value=4.0, max_value=8.0, value=5.8, step=0.1)
    sepal_width = st.sidebar.slider("Ancho del Sépalo (cm)", min_value=2.0, max_value=4.5, value=3.0, step=0.1)
    petal_length = st.sidebar.slider("Longitud del Pétalo (cm)", min_value=1.0, max_value=7.0, value=4.3, step=0.1)
    petal_width = st.sidebar.slider("Ancho del Pétalo (cm)", min_value=0.1, max_value=2.5, value=1.3, step=0.1)

    # --- ÁREA PRINCIPAL: SELECCIÓN Y PREDICCIÓN ---
    st.subheader("Configuración del Modelo")
    opcion_modelo = st.selectbox(
        "Elige el modelo que deseas poner a prueba:",
        ("K-Nearest Neighbors (KNN)", "Support Vector Machine (SVM)")
    )

    # Mapeo de los resultados numéricos a los nombres de las especies
    nombres_especies = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}

    # Botón para ejecutar la predicción
    if st.button("🔍 Clasificar Flor", type="primary"):
        # Preparar los datos en el formato que espera scikit-learn (2D array)
        datos_entrada = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
        
        # Seleccionar el modelo elegido
        modelo_activo = modelo_knn if opcion_modelo == "K-Nearest Neighbors (KNN)" else modelo_svm
        
        # Hacer la predicción
        prediccion_num = modelo_activo.predict(datos_entrada)[0]
        especie_predicha = nombres_especies[prediccion_num]
        
        # Mostrar el resultado
        st.success(f"El modelo **{opcion_modelo}** clasifica esta flor como: **Iris {especie_predicha}**")
