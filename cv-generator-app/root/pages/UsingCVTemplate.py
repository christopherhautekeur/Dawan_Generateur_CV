from root.utils.PageCreator import PageCreator
from root.utils.utils import generate_html_with_json

page = PageCreator(
    "Dawan - Utilisation d'un template pré-enregistré",
    "Page d'utilisation d'un template pré-enregistré",
    "Utilisation d'un template pré-enregistré",
    "- Cliquez sur **Générer le CV** pour obtenir un CV personnalisé basé sur les mots-clés et les exigences de l'offre.",
)

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

generate_html_with_json(user_data, "style1.css")
