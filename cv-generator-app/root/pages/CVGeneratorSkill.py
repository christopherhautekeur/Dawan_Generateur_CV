from root.utils.PageCreator import PageCreator
import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from pypdf import PdfReader
import json
from root.utils.Scrapper import Scrapper
from root.utils.Processing import Processing

def create_checkbox_competence_to_add(json_file,sl ,tl,text):
    array= json.loads(json_file)
    st.write("softskill")
    for soft in array["softskills"]:
        if(soft in text.lower()):
            nl= [soft,st.checkbox(soft,value=True)]
            sl.append(nl)
        else:
            nl= [soft,st.checkbox(soft)]
            sl.append(nl)
    st.write("technologies")
    for tech in array["technologies"]:
        if(tech in text.lower()):
            nl= [tech,st.checkbox(tech,value=True)]
            tl.append(nl)
        else:
            nl= [tech,st.checkbox(tech)]
            tl.append(nl)
            
def recreate_checkbox(soft_list ,tech_list, a, a_b, b, b_b):     
    st.write("softskill")
    for ln in st.session_state["soft_list"]:
        nl= [ln[0],st.checkbox(ln[0],value=ln[1])]
        soft_list.append(nl)
    if a_b:
        if a != "":
            nl= [a,st.checkbox(a,value=True)]
            soft_list.append(nl)
            
    st.write("technologies")
    for ln in st.session_state["tech_list"]:
        nl= [ln[0],st.checkbox(ln[0],value=ln[1])]
        tech_list.append(nl)
        
    if b_b:
        if b != "":
            nl2= [b,st.checkbox(b,value=True)]
            tech_list.append(nl2)

def check_checkbox(ret_json,sl,tl):
    for i in sl:
        if i[1] == True:
            ret_json["softskills"].append(i[0])
    for i in tl:
        if i[1] == True:
            ret_json["technologies"].append(i[0])

        
page = PageCreator(
    "Cv Skill",
    "Genere les skills correspondant entre l'utilisateur et l'url'"
)

processing = Processing()
url = st.text_input("Entrez l'url de la page")

if st.button('Scrap'):
    if "external_data_url" not in st.session_state:
        cleaned_data = processing.process_jobs_infos(Scrapper.get_jobs_infos(url))
        st.session_state["external_data_url"] = url
        st.session_state["external_data"] = cleaned_data
        st.session_state["soft_list"] = []
        st.session_state["tech_list"] = []

        
    elif url != st.session_state["external_data_url"]:
        cleaned_data = processing.process_jobs_infos(Scrapper.get_jobs_infos(url))
        st.session_state["external_data_url"] = url
        st.session_state["external_data"] = cleaned_data
        st.session_state["soft_list"] = []
        st.session_state["tech_list"] = []

uploaded_file_pdf = st.file_uploader("Choose a file", type=('pdf'), key='pdf')

if uploaded_file_pdf is not None:
    reader = PdfReader(uploaded_file_pdf)
    pa = reader.pages[0]
    x= pa.extract_text(extraction_mode="layout")
    
    if "external_data" in st.session_state and uploaded_file_pdf is not None:
        c1, c2 = st.columns(2, vertical_alignment="bottom")
        a = c1.text_input("Add soft list")
        a_b = c1.button('Add soft')
        b = c2.text_input("Add tech list")
        b_b = c2.button('Add tech')
        soft_list= []
        tech_list= []
        if st.session_state["soft_list"] == [] and st.session_state["tech_list"] ==  []:
            create_checkbox_competence_to_add(st.session_state["external_data"],soft_list,tech_list,x)
        else:
            recreate_checkbox(soft_list ,tech_list,a,a_b,b,b_b)

        
        st.session_state["soft_list"] = soft_list
        st.session_state["tech_list"] = tech_list
        json_data = {"technologies": [],"softskills":[], }
        check_checkbox(json_data, st.session_state["soft_list"], st.session_state["tech_list"])
        st.json(json_data)