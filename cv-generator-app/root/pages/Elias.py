from root.utils.PageCreator import PageCreator
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader

page = PageCreator(
    "Elias",
    "Test upload et previsualisation"
)
promptrep = st.text_input('Mot à remplacer')
promptnou = st.text_input('Nouveau mot')
uploaded_file = st.file_uploader("Choose a file", type=('pdf'), key='pdf')
if uploaded_file is not None:

    bytes_data = uploaded_file.read()
    pdf_viewer(bytes_data)
    reader = PdfReader(uploaded_file)
    pa = reader.pages[0]
    x= pa.extract_text(extraction_mode="layout")
    st.write(x)
