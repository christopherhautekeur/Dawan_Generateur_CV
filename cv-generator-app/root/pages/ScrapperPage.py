import streamlit as st
from root.utils.Scrapper import Scrapper

st.set_page_config(
    page_title='Scrapper',
    page_icon=" ",
    layout="centered",
    initial_sidebar_state="auto",
)

# Titre
st.title('Scrapper')

url = st.text_input("Entrez l'url de la page")

if st.button('Scrap'):
    st.write(Scrapper.get_jobs_infos(url))
