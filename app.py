import streamlit as st
import base64

st.set_page_config(page_title="Mensaje Secreto", page_icon="🔐")

st.title("🔐 Generador de Mensajes Secretos")

texto = st.text_area("Escribe tu mensaje:")

modo = st.radio("Selecciona una opción:", ["Codificar", "Decodificar"])

# Codificar (Base64)
def codificar(texto):
    texto_bytes = texto.encode("utf-8")
    base64_bytes = base64.b64encode(texto_bytes)
    return base64_bytes.decode("utf-8")

# Decodificar
def decodificar(texto):
    try:
        base64_bytes = texto.encode("utf-8")
        texto_bytes = base64.b64decode(base64_bytes)
        return texto_bytes.decode("utf-8")
    except:
        return "⚠️ No es un mensaje válido"

if st.button("Procesar"):
    if texto.strip() == "":
        st.warning("Escribe algo primero")
    else:
        if modo == "Codificar":
            resultado = codificar(texto)
            st.code(resultado)
        else:
            resultado = decodificar(texto)
            st.success(resultado)
