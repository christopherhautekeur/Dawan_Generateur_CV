import streamlit as st

path = "root/pages/"
pg = st.navigation([
        st.Page(path + "Home.py", title="Accueil", icon=":material/home:"),
        st.Page(path + "Tutorials.py", title="Guide d'utilisation", icon=":material/help:"),
        st.Page(path + "CVGeneratorFinal.py", title="Générer son CV Final", icon=":material/picture_as_pdf:"),
        st.Page(path + "CVGenerator.py", title="Générer son CV", icon=":material/picture_as_pdf:"),
        # st.Page(path + "CoverLetterGenerator.py", title="Générer sa lettre de motivation", icon=":material/picture_as_pdf:"),
        st.Page(path + "UsingCVTemplate.py", title="Générer son CV via template", icon=":material/picture_as_pdf:"),
        st.Page(path + "ScrapperPage.py", title="Scrapper"),
        # st.Page(path + "Elias.py", title="Test Elias"),
        st.Page(path + "CVGeneratorSkill.py", title="Générer skill CV"),

])
pg.run()
