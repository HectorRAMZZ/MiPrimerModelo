import streamlit as st
import random
import time

# Configuración inicial
st.set_page_config(page_title="parctica ecuaciones", page_icon="🧮")

st.title("🧮 repaso de la clase")
st.write("Resuelve la ecuación de primer grado:")
st.info("capturad e pantalla y ajuata")

# Función para generar ecuación
def generar_ecuacion():
    a = random.randint(1, 10)
    x = random.randint(1, 10)
    b = random.randint(1, 10)
    
    # ax + b = resultado
    resultado = a * x + b
    
    return a, b, resultado, x

# Mantener estado
if "ecuacion" not in st.session_state:
    st.session_state.ecuacion = generar_ecuacion()
    st.session_state.resuelto = False

a, b, resultado, x_correcto = st.session_state.ecuacion

# Mostrar ecuación
st.subheader(f"{a}x + {b} = {resultado}")

# Input usuario
respuesta = st.number_input("Ingresa el valor de x:", step=1)

# Botón verificar
if st.button("Verificar"):
    if respuesta == x_correcto:
        st.success("✅ Correcto!")
        
        # Animación simple
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
        
        st.balloons()
        st.session_state.resuelto = True
    else:
        st.error("❌ Incorrecto, intenta otra vez")

# Botón nueva ecuación
if st.session_state.resuelto:
    if st.button("Nueva ecuación"):
        st.session_state.ecuacion = generar_ecuacion()
        st.session_state.resuelto = False
        st.rerun()
