from root.utils.PageCreator import PageCreator
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader
import zipfile
from bs4 import BeautifulSoup

def fichier_html(docx):
    inzip = zipfile.ZipFile(docx)
    soup=BeautifulSoup(inzip.read("word/document.xml").decode('utf-8','ignore'),'lxml-xml')
    return soup.prettify()

def fichier_xml(docx):
    inzip = zipfile.ZipFile(docx)
    return inzip.read("word/document.xml")

page = PageCreator(
    "Elias",
    "Test upload et previsualisation"
)

uploaded_file = st.file_uploader("Choose a file", type=('docx'))
uploaded_file_pdf = st.file_uploader("Choose a file", type=('pdf'), key='pdf')
if uploaded_file is not None:
    tmp = fichier_xml(uploaded_file)
    btn = st.download_button(
                label="Download fichier xml",
                data=tmp,
                file_name="fichier.xml",
                mime="xml"
            )
    tmp2 = fichier_html(uploaded_file)
    btn = st.download_button(
                label="Download fichier html",
                data=tmp2,
                file_name="fichier.html",
                mime="html"
            )
if uploaded_file_pdf is not None:
    st.write("pdf")
    bytes_data = uploaded_file_pdf.read()
    pdf_viewer(bytes_data)
    reader = PdfReader(uploaded_file_pdf)
    pa = reader.pages[0]
    x= pa.extract_text(extraction_mode="layout")
    st.write(x)