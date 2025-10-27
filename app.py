import streamlit as st
import pandas as pd
import os
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

# -------------------------------------------------
# CONFIGURACIÓN DE LA APP
# -------------------------------------------------

# Clave API desde Streamlit Secrets
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except KeyError:
    st.error("❌ No se encontró la clave API en Streamlit Secrets. Asegúrate de configurar 'GROQ_API_KEY'.")
    st.stop()

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
        model="llama3-8b-8192",  # Cambiado a un modelo alternativo soportado
        api_base="https://api.groq.com/openai/v1"
    )
    st.success("🧠 Modelo Groq inicializado correctamente (vía OpenAI wrapper).")
except Exception as e:
    st.error(f"❌ Error al inicializar el modelo Groq: {str(e)}")
    st.error("Modelos soportados por Groq: 'llama3-8b-8192', 'mixtral-8x7b-32768', 'gemma-7b-it'. Intentando con el SDK nativo de Groq...")
    
    # Intento con Groq SDK como respaldo
    try:
        from pandasai.llm import Groq
        llm = Groq(api_key=GROQ_API_KEY, model="llama3-8b-8192")
        st.success("🧠 Modelo Groq inicializado correctamente con SDK nativo.")
    except Exception as e2:
        st.error(f"❌ Error al inicializar con Groq SDK: {str(e2)}")
        st.error("Por favor, verifica tu clave API y la configuración del modelo en https://console.groq.com.")
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
