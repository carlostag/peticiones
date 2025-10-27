import streamlit as st
import pandas as pd
import os
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# -------------------------------------------------
# CONFIGURACIÓN DE LA APP
# -------------------------------------------------

# Clave API desde Streamlit Secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Título de la aplicación
st.title("🤖 PandasAI Chatbot - Peticiones de Reparación")

# Ruta del archivo Excel
EXCEL_PATH = "peticiones.xlsx"

# -------------------------------------------------
# CARGA DE DATOS
# -------------------------------------------------
try:
    data = pd.read_excel(EXCEL_PATH)
    st.success("✅ Archivo cargado correctamente.")
    st.dataframe(data.head())
except Exception as e:
    st.error(f"❌ Error al cargar el archivo: {str(e)}")
    st.stop()

# -------------------------------------------------
# INICIALIZACIÓN DEL MODELO LLM (GROQ vía OpenAI wrapper)
# -------------------------------------------------
try:
    llm = OpenAI(
        api_token=GROQ_API_KEY,
        model="llama-3.3-70b-versatile",
        api_base="https://api.groq.com/openai/v1"
    )
    st.success("🧠 Modelo Groq inicializado correctamente (vía OpenAI wrapper).")
except Exception as e:
    st.error(f"❌ Error al inicializar el modelo Groq: {str(e)}")
    st.stop()

# -------------------------------------------------
# CREACIÓN DEL SMART DATAFRAME
# -------------------------------------------------
try:
    df = SmartDataframe(data, config={"llm": llm})
    st.success("📊 SmartDataframe creado con éxito.")
except Exception as e:
    st.error(f"❌ Error al crear el SmartDataframe: {str(e)}")
    st.stop()

# -------------------------------------------------
# INTERFAZ DE CHAT
# -------------------------------------------------
st.markdown("### 💬 Haz una pregunta sobre los datos:")

user_query = st.text_input("Escribe tu consulta:")

if user_query:
    try:
        with st.spinner("Pensando... 🤔"):
            result = df.chat(user_query)

        st.markdown("### 🧾 **Respuesta:**")

        if isinstance(result, str) and result.lower().endswith((".png", ".jpg", ".jpeg")) and os.path.exists(result):
            st.image(result)
        else:
            st.write(result)

    except Exception as e:
        st.error(f"❌ Error al procesar la consulta: {str(e)}")
