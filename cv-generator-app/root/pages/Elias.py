from root.utils.PageCreator import PageCreator
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader
import svgwrite

dwg = svgwrite.Drawing("GeoBase_test.svg", profile="tiny")

def visitor_svg_rect(op, args, cm, tm):
    if op == b"re":
        (x, y, w, h) = (args[i].as_numeric() for i in range(4))
        dwg.add(dwg.rect((x, y), (w, h), stroke="red", fill_opacity=0.05))


def visitor_svg_text(text, cm, tm, fontDict, fontSize):
    (x, y) = (cm[4], cm[5])
    dwg.add(dwg.text(text, insert=(x, y), fill="blue"))


page = PageCreator(
    "Elias",
    "Test upload et previsualisation"
)

uploaded_file = st.file_uploader("Choose a file", type=('pdf'), key='pdf')
if uploaded_file is not None:

    bytes_data = uploaded_file.read()
    pdf_viewer(bytes_data)
    reader = PdfReader(uploaded_file)
    pa = reader.pages[0]
    x = pa.extract_text(
        visitor_operand_before=visitor_svg_rect, visitor_text=visitor_svg_text
    )
    st.write(x)