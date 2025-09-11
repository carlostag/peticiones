import streamlit as st
import pandas as pd
from langchain_groq.chat_models import ChatGroq
from pandasai import SmartDataframe

# Acceder a la clave API desde Streamlit Secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Título de la app
st.title("PandasAI Chatbot Peticiones Reparación")

# Ruta fija del archivo Excel
EXCEL_PATH = "peticiones.xlsx"

# Carga del archivo Excel
try:
    data = pd.read_excel(EXCEL_PATH)
    st.success("Archivo cargado correctamente.")
    st.dataframe(data.head())
except Exception as e:
    st.error(f"Error al cargar el archivo: {str(e)}")
    st.stop()

# Inicialización del modelo LLM
try:
    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        api_key=GROQ_API_KEY
    )
except Exception as e:
    st.error(f"Error al inicializar el modelo Groq: {str(e)}")
    st.stop()

# Inicialización de SmartDataframe
try:
    df = SmartDataframe(data, config={"llm": llm})
except Exception as e:
    st.error(f"Error al crear el SmartDataframe: {str(e)}")
    st.stop()

# Interfaz de chat
user_query = st.text_input("Haz una pregunta sobre los datos:")

if user_query:
    try:
        with st.spinner("Pensando..."):
            result = df.chat(user_query)
        st.markdown("**Respuesta:**")
        st.write(result)
    except Exception as e:
        st.error(f"Error al procesar la consulta: {str(e)}")
