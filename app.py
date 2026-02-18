import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page
st.set_page_config(page_title="Mon CV", layout="wide")

# Lecture du fichier HTML
with open("/mount/src/cv-de-ass-gueye/app.py", "r", encoding="utf-8") as f:
    html_content = f.read()

# Affichage du HTML dans Streamlit
components.html(html_content, height=1000, scrolling=True)
 
