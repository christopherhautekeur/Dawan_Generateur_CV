import re
import streamlit as st


def valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email)


def valid_phone_number(phone_number):
    phone_regex = r"^(?:\+33|0)[1-9](?:[\s.-]?\d{2}){4}$"
    return re.match(phone_regex, phone_number)


def valid_zip_code(zip_code):
    zip_code_regex = r"^\d{5}$"
    return re.match(zip_code_regex, zip_code)


def valid_name(name):
    name_regex = r"^[a-zA-Z\s]+$"
    return re.match(name_regex, name)


def valid_address(address):
    address_regex = r"^[a-zA-Z0-9\s.,-]+$"
    return re.match(address_regex, address)


def footer():
    st.write("---")
    st.markdown(
        "<p style='color: #777;text-align: center;'>Générateur de CV • Dawan • 2024</p>",
        unsafe_allow_html=True
    )


def generate_html_with_json(data_json, style):
    path = "root/cv-templates/styles/"
    # Lire le template de css
    with open(path + style, "r", encoding="utf-8") as file:
        css = file.read()

    # Lire l'html du CV
    with open("root/cv-templates/cv-template.html", "r", encoding="utf-8") as file:
        cv_html = file.read()

    for key, value in data_json.items():
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

    return cv_html
