from root.utils.PageCreator import PageCreator
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader
from root.utils.Processing import Processing
from root.utils.utils import generate_html_with_json
from root.utils.Scrapper import Scrapper
from root.utils.Processing import Processing
import pandas as pd
import json
import streamlit as st
import os
import tempfile
from pyhtml2pdf import converter



page = PageCreator(
    "Dawan Générateur de CV - CV",
    "Crée ton CV",
    "CV",
    "- Cliquez sur **Générer le CV** pour obtenir un CV personnalisé basé sur les mots-clés et les exigences de l'offre.",
)
@st.cache_data
def get_jobs_dataset(job, location, jobboard) -> pd.DataFrame:
    return pd.DataFrame.from_dict(Scrapper.get_list_jobs(jobboard, job, location))

def html_to_pdf(file_html):
    
    temp_dir = tempfile.mkdtemp()
    path = os.path.join(temp_dir, "CV.html")
    with open(path, "wb") as tempf:
        tempf.write(file_html.encode())
    
    temp_dir2 = tempfile.mkdtemp()
    f = os.path.join(temp_dir2, "CV.pdf")
    converter.convert(f'{path}', f, print_options={"scale": 0.85 })
    
    st.session_state["html_file"] = file_html
    st.session_state["f"] = f

selected_row = []
processing = Processing()

with st.container(border=True):
    row1 = st.columns([3,2,2])
    row2 = st.columns([3,3,2])
    job = row1[0].text_input("Poste")
    location = row1[1].text_input("Lieu")
    jobboard = row1[2].selectbox("JobBoard", ["indeed",])  # Rajouter des jobboards
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
            # Affiche les infos du jobs selectionner
            annonce = Scrapper.get_jobs_infos(st.session_state.get('jobs_df').iloc[selected_row[0]].lien)
            infos = processing.process_jobs_infos(annonce)
            st.write("Info récuperer")
            st.session_state["info"] = infos
        else:
            st.write("Veuillez sélectionner une offre")

uploaded_file_pdf = st.file_uploader("Choose a file", type='pdf', key='pdf')

if uploaded_file_pdf is not None:
    bytes_data = uploaded_file_pdf.read()

    # Voir le PDF
    pdf_viewer(bytes_data)
    reader = PdfReader(uploaded_file_pdf)
    pa = reader.pages[0]

    # Générer le JSON directement via le CV
    cv_content = pa.extract_text(extraction_mode="layout")

##Implementer la creation de CV ainsi qu'ajouter les soft skill et technologie


    if st.button("Générer le json") and "info" in st.session_state:
        processing2 = Processing()
        generated_json = json.loads(processing2.generate_json(cv_content))
        array= json.loads(st.session_state["info"])
        generated_json["soft-skills"] = array["softskills"]
        generated_json["codingLanguages"] = array["technologies"]
        
        try:
            #Appelle l'IA uniquement si aucune n'a était crée ou le fichier est different
            if "cv_content" not in st.session_state:
                g= generate_html_with_json(generated_json, "style1.css")
                st.session_state["html_file2"] = g
                st.session_state["cv_content"] = cv_content
                
            elif st.session_state["cv_content"] != cv_content:
                g= generate_html_with_json(generated_json, "style1.css")
                st.session_state["html_file2"] = g
                st.session_state["cv_content"] = cv_content
            
        except json.decoder.JSONDecodeError:
            st.error("Le JSON est invalide. Veuillez réessayer.")

    #Genere un nouveau pdf si le fichier html n'existe pas ou n'est pas le même
    if "pdf_file" not in st.session_state and "html_file2" in st.session_state:
        if "html_file" not in st.session_state  :
            html_to_pdf(st.session_state["html_file2"])
            
        elif st.session_state["html_file"] != st.session_state["html_file2"]:
            html_to_pdf(st.session_state["html_file2"])
        
        
        btn = st.download_button(
                    label="Download fichier pdf",
                    data= open(st.session_state["f"],'rb'),
                    file_name="CV.pdf",
                    mime="application/octet-stream"
                )
        
        st.components.v1.html(st.session_state["html_file"], height=800, scrolling=True)