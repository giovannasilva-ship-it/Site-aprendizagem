from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# Wrapper mínimo: mantém o HTML, CSS e JavaScript existentes dentro de um iframe.
st.set_page_config(page_title="Site da Aprendizagem CIEE", layout="wide", initial_sidebar_state="collapsed")

HTML_PATH = Path(__file__).parent / "index.html"
if not HTML_PATH.exists():
    st.error(f"Arquivo não encontrado: {HTML_PATH.name}. Mantenha app.py e index.html na mesma pasta.")
    st.stop()

html = HTML_PATH.read_text(encoding="utf-8")
components.html(html, height=950, scrolling=True)