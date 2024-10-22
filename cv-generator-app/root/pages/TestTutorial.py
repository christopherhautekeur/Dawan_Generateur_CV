from root.utils.PageCreator import PageCreator
import streamlit as st

page = PageCreator(
    "Dawan Générateur de CV - Home",
    "Page d'accueil",
    "Home",
    "- Bienvenue sur le Générateur de CV de Dawan ! Cette application permet de générer des CV/lettres de motivations et de proposer des offres pertinentes selon vos recherches.",
)
texts = {"Motivation Header": "Motivation", "CV Header": "CV", "Alternance Header": "Alternance"}
if page.create_tutorial(texts):

    with st.empty():
        st.write("insérer une nouvelle page ici")