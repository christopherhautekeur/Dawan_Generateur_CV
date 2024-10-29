from root.utils.PageCreator import PageCreator
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader
import zipfile
from bs4 import BeautifulSoup
from pyhtml2pdf import converter
import os
import tempfile


def fichier_html(docx):
    inzip = zipfile.ZipFile(docx)
    soup = BeautifulSoup(inzip.read("word/document.xml").decode('utf-8', 'ignore'), 'lxml-xml')
    return soup.prettify()


def fichier_xml(docx):
    inzip = zipfile.ZipFile(docx)
    return inzip.read("word/document.xml")


def html_to_pdf(file_html):
    temp_dir = tempfile.mkdtemp()
    path = os.path.join(temp_dir, file_html.name)
    with open(path, "wb") as tempf:
        tempf.write(file_html.read())
    
    temp_dir2 = tempfile.mkdtemp()
    f = os.path.join(temp_dir2, "CV.pdf")
    converter.convert(f'{path}', f, print_options={"scale": 0.85 })
    
    st.session_state["html_file"] = file_html
    st.session_state["f"] = f

page = PageCreator(
    "Elias",
    "Test upload et previsualisation"
)

uploaded_file = st.file_uploader("Choose a file", type=('docx'))
uploaded_file_pdf = st.file_uploader("Choose a file", type=('pdf'), key='pdf')
uploaded_file_html = st.file_uploader("Choose a file", type=('html'), key='html')

if uploaded_file_html is not None :
    if "html_file" not in st.session_state and "f" not in st.session_state:
        html_to_pdf(uploaded_file_html)
    elif st.session_state["html_file"] != uploaded_file_html:
        html_to_pdf(uploaded_file_html)
    
    pdf_viewer(st.session_state["f"])
    btn = st.download_button(
                label="Download fichier pdf",
                data= open(st.session_state["f"],'rb'),
                file_name="CV.pdf",
                mime="application/octet-stream"
            )
        

if uploaded_file is not None:
    tmp = fichier_xml(uploaded_file)
    btn_xml = st.download_button(
                label="Download fichier xml",
                data=tmp,
                file_name="fichier.xml",
                mime="xml"
            )
    tmp2 = fichier_html(uploaded_file)
    btn_html = st.download_button(
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

    x = pa.extract_text(extraction_mode="layout")

    st.write(x)
