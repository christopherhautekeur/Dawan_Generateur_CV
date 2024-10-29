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
