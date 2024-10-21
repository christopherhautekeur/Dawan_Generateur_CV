import streamlit as st

path = "root/pages/"
pg = st.navigation([
        st.Page(path + "Home.py", icon=":material/home:"),
        st.Page(path + "CVCreator.py", title="Créer son CV"),
        # st.Page(path + "LetterCreator.py", title="Créer une lettre de motivation"),
])
pg.run()