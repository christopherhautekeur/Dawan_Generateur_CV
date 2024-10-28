from root.utils.PageCreator import PageCreator
import streamlit as st
import re
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader
from root.utils.Processing import Processing
import json

page = PageCreator(
    "Dawan Générateur de CV - CV",
    "Crée ton CV",
    "CV",
    "- Cliquez sur **Générer le CV** pour obtenir un CV personnalisé basé sur les mots-clés et les exigences de l'offre.",
)

radio = st.radio("Créer son CV via", ["Formulaire", "PDF"])

if radio == "Formulaire":  # Formulaire
    with st.form("my_form"):

        prenom = st.text_input("Prénom")
        nom = st.text_input("Nom")

        col1, col2 = st.columns(2)
        with col1:
            email = st.text_input("Adresse e-mail")

        with col2:
            telephone = st.text_input("Numéro de téléphone")

        adresse = st.text_input("Adresse")

        col5, col6 = st.columns(2)
        with col5:
            code_postal = st.text_input("Code postal")

        with col6:
            ville = st.text_input("Ville")

        if st.form_submit_button("Soumettre"):
            # Vérifier que le prénom/nom/ville contient que des lettres

            # Vérifier le bon format de l'adresse email

            # Vérifier le bon format du numéro

            # Vérifier le bon format du code postal

            # Enregistrer les données dans un fichier JSON

            st.success("CV envoyé")

            st.session_state.user_data = {
                "name": nom + " " + prenom,
                "email": email,
                "phone": telephone,
                "experience-line": "",
                "experiences": [],
                "address": adresse + ", " + code_postal + " " + ville,
                "formations": [],
                "codingLanguages": [],
                "soft-skills": [],
                "languages": [],
                "hobbies": [],
                "outils": [],
                "frameworks": [],
            }

            st.json(st.session_state.user_data)

else:  # PDF
    uploaded_file_pdf = st.file_uploader("Choose a file", type='pdf', key='pdf')

    if uploaded_file_pdf is not None:
        bytes_data = uploaded_file_pdf.read()

        # Voir le PDF
        pdf_viewer(bytes_data)
        reader = PdfReader(uploaded_file_pdf)
        pa = reader.pages[0]

        # Générer le JSON directement via le CV
        cv_content = pa.extract_text(extraction_mode="layout")

        if st.button("Générer le json"):
            processing = Processing()
            generated_json = processing.generate_json(cv_content)
            # st.write(generated_json)
            st.json(json.loads(generated_json))
