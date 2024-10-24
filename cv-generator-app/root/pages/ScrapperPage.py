import streamlit as st
from root.utils.Scrapper import Scrapper
from root.utils.Processing import Processing


processing = Processing()

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
    st.json(processing.process_jobs_infos(Scrapper.get_jobs_infos(url)))


if st.button('Liste des offres'):
    st.write(Scrapper.get_list_jobs("https://fr.indeed.com/jobs?q=Developpeur&l=Lille+%2859%29&vjk=dc7d2e98b81558f6"))