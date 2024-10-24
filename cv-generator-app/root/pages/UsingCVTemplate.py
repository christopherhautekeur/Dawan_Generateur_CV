from root.utils.PageCreator import PageCreator
import streamlit as st

path = "root/cv-templates/"

page = PageCreator(
    "Dawan - Utilisation d'un template pré-enregistré",
    "Page d'utilisation d'un template pré-enregistré",
    "Utilisation d'un template pré-enregistré",
    "- Cliquez sur **Générer le CV** pour obtenir un CV personnalisé basé sur les mots-clés et les exigences de l'offre.",
)

# Lire le template de CV
with open(path + "cv-template1.html", "r", encoding="utf-8") as file:
    cv_html = file.read()

# Modification des données personnelles

# Récupérer le json de Christopher
user_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "experience": "5 ans d'expérience en développement logiciel chez XYZ",
    "address": "123 Rue de Paris, 75001 Paris, France",
}

for key, value in user_data.items():
    cv_html = cv_html.replace(f"{{{{{key}}}}}", value)

# Afficher le template de CV
if st.button("Visualiser le CV"):
    st.components.v1.html(cv_html, height=800, scrolling=True)






