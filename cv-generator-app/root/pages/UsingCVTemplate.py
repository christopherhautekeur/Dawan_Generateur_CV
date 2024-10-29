from root.utils.PageCreator import PageCreator
import streamlit as st

path = "root/cv-templates/styles/"

page = PageCreator(
    "Dawan - Utilisation d'un template pré-enregistré",
    "Page d'utilisation d'un template pré-enregistré",
    "Utilisation d'un template pré-enregistré",
    "- Cliquez sur **Générer le CV** pour obtenir un CV personnalisé basé sur les mots-clés et les exigences de l'offre.",
)

# Lire le template de css
with open(path + "style1.css", "r", encoding="utf-8") as file:
    css = file.read()

# Lire l'html du CV
with open("root/cv-templates/cv-template.html", "r", encoding="utf-8") as file:
    cv_html = file.read()

# Récupérer le json de Christopher
user_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890",
    "experience-line": "5 ans d'expérience en développement logiciel chez XYZ",
    "experiences": [["Développeur Backend", "Entreprise XYZ, Paris (2020 - Présent)"],
                    ["Ingénieur Logiciel", "Entreprise ABC, Lyon (2018 - 2020)"],
                    ["Stagiaire Développeur", "Startup 123, Toulouse (2017 - 2018)"]],
    "address": "123 Rue de Paris, 75001 Paris, France",
    "formations": [["Master en Informatique", "Université de Paris (2016)"],
                    ["Licence en Informatique", "Université de Lyon (2014)"]],
    "codingLanguages": ["Python", "JavaScript", "HTML", "CSS"],
    "soft-skills": ["Positivité", "Travail d'équipe", "Gestion de projets agiles"],
    "languages": ["Français (natif)", "Anglais (courant)"],
    "hobbies": ["Cyclisme", "Sport", "Informatique"],
    "outils": ["Git", "Docker", "Jenkins"],
    "frameworks": ["Django, Flask, React"],
}

for key, value in user_data.items():
    if key == "experiences":
        experience = "\n".join([f"<li><strong>{exp[0]}</strong> - {exp[1]}</li>" for exp in value])
        cv_html = cv_html.replace(f"{{{{{key}}}}}", experience)

    elif key == "formations":
        formation = "\n".join([f"<li><strong>{form[0]}</strong> - {form[1]}</li>" for form in value])
        cv_html = cv_html.replace(f"{{{{{key}}}}}", formation)

    elif key in ["codingLanguages", "soft-skills", "languages", "hobbies", "outils", "frameworks"]:
        skills = ", ".join(value)
        cv_html = cv_html.replace(f"{{{{{key}}}}}", skills)

    else:
        cv_html = cv_html.replace(f"{{{{{key}}}}}", value)

# Ajouter le style CSS
cv_html += f"<style>{css}</style>"

# Afficher le template de CV
if st.button("Visualiser le CV"):
    # st.code(cv_html)
    st.components.v1.html(cv_html, height=800, scrolling=True)

