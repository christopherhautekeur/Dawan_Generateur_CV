import streamlit as st

path = "root/pages/"
pg = st.navigation([
        st.Page(path + "Home.py", icon=":material/home:"),
        # st.Page(path + "NLP.py", title="1. Natural Language Processing (NLP)"),
    ])
pg.run()