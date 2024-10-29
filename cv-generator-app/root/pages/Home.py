from root.utils.PageCreator import PageCreator
import streamlit as st
from root.utils.utils import footer


page = PageCreator(
    "Dawan Générateur de CV - Home",
    "Page d'accueil",
    "Home",
    "- Bienvenue sur le Générateur de CV de Dawan ! Cette application permet de générer des CV/lettres de motivations et de proposer des offres pertinentes selon vos recherches.",
)

st.info("**Bienvenue sur le Générateur de CV de Dawan !**  \n  Créer un CV ou une lettre de motivation de niveau professionnel en quelques clics. ")
st.warning("Choisissez une option ci-dessous pour commencer.")
st.write("")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="background-color: #eaf4f4; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
        <img src="https://img.icons8.com/ios-filled/100/4CAF50/artificial-intelligence.png" alt="Icône IA" style="width: 80px; margin-right: 20px;">
            <h3 style="color:#3b7d7d;">CV généré par IA</h3>
            <p style="color:#2e5f5f;">Laissez notre technologie élaborer un CV personnalisé avec vos données. Recevez un document optimisé en quelques clics.</p>
            <button style="padding: 10px 20px; border: none; background-color: #4CAF50; color: white; border-radius: 5px; cursor: pointer;">
                <a href="#" style="text-decoration: none; color: white;">Commencer avec l'IA</a>
            </button>
        </div>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div style="background-color: #f1e7e7; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
            <img src="https://img.icons8.com/ios-filled/100/2196F3/edit-file.png" style="width: 50px; height: 50px; float: left; margin-right: 20px;">
            <h3 style="color:#7d3b3b;">Création de CV personnalisée</h3>
            <p style="color:#5f2e2e;">Modifiez chaque section pour concevoir un CV qui vous ressemble. Parfait pour ceux qui souhaitent un contrôle total sur leur présentation.</p>
            <button style="padding: 10px 20px; border: none; background-color: #2196F3; color: white; border-radius: 5px; cursor: pointer;">
                <a href="#" style="text-decoration: none; color: white;">Créer un CV maintenant</a>
            </button>
        </div>
        """, unsafe_allow_html=True
    )

st.write("")

st.markdown("### Astuces pour réussir votre CV et votre lettre de motivation :bulb:")

col3, col4 = st.columns(2)

with col3:
    st.markdown("**1. Personnalisez votre CV**")
    st.write("Mettez en avant les compétences spécifiques au poste visé.")

    st.markdown("**2. Soyez direct**")
    st.write("Optez pour des phrases brèves et percutantes.")

    st.markdown("**3. Organisez votre CV**")
    st.write("Utilisez des sections claires pour améliorer la lisibilité.")

with col4:
    st.markdown("**4. Mettez en avant vos réussites**")
    st.write("Intégrez des chiffres pour illustrer vos accomplissements, par exemple \"+20% ventes\".")

    st.markdown("**5. Incluez vos soft skills**")
    st.write("Mentionnez des qualités personnelles pertinentes pour le poste.")

    st.markdown("**6. Relisez soigneusement**")
    st.write("Corrigez les fautes et vérifiez votre document avant de l'envoyer.")


footer()

