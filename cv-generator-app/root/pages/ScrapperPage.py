import streamlit as st
from root.utils.Scrapper import Scrapper
from root.utils.Processing import Processing
import pandas as pd


@st.cache_data
def get_jobs_dataset(job, location, jobboard) -> pd.DataFrame:
    return pd.DataFrame.from_dict(Scrapper.get_list_jobs(jobboard, job, location))


st.set_page_config(
    page_title="Jobboards",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title('Jobboards')

selected_row = []
processing = Processing()

with st.container(border=True):
    row1 = st.columns([3,2,2])
    row2 = st.columns([3,3,2])
    job = row1[0].text_input("Poste")
    location = row1[1].text_input("Lieu")
    jobboard = row1[2].selectbox("JobBoard", ["indeed",])
    if st.button('Rechercher'):
        if 'jobs_df' not in st.session_state:
            st.session_state['jobs_df'] = pd.DataFrame()
        if job == '' or location == '':
            st.write("Veuillez saisir un poste et une ville")
        else:
            st.session_state['jobs_df'] = get_jobs_dataset(job, location, jobboard)

if 'jobs_df' in st.session_state:
    column_configuration = {
        'poste': st.column_config.TextColumn(
            "Poste", width="large"
        ),
        'entreprise': st.column_config.TextColumn(
            "Entreprise", width="small",
        ),
        'lien': None,
    }

    jobs_list = st.dataframe(
        st.session_state.get('jobs_df'),
        column_config=column_configuration,
        use_container_width=True,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
    )

    selected_row = jobs_list.selection.rows

    if st.button("Recuperer les infos du poste"):
        if len(selected_row) > 0:
            annonce = Scrapper.get_jobs_infos(st.session_state.get('jobs_df').iloc[selected_row[0]].lien)
            infos = processing.process_jobs_infos(annonce)
            st.json(infos)
        else:
            st.write("Veuillez sélectionner une offre")




