import streamlit as st


class PageCreator:
    def __init__(self, pageTitle="", stTitle="", sidebarHeader="", sideBarDescription=""):
        self.pageTitle = pageTitle
        self.stTitle = stTitle
        self.sidebarHeader = sidebarHeader
        self.sideBarDescription = sideBarDescription

        if 'step' not in st.session_state:
            st.session_state.step = 0

        if 'button_pressed' not in st.session_state:
            st.session_state.button_pressed = False

        self.create_page()

    def create_page(self):
        """
            Cette fonction configure la page avec le titre, l'icône et la disposition spécifiés.

            Paramètres :
            - self.pageTitle (str) : Le titre de la page.
            - self.stTitle (str) : Le titre affiché sur la page.
            - self.sidebarHeader (str) : L'en-tête affiché dans la barre latérale.
            - self.sideBarDescription (str) : La description affichée dans la barre latérale.
        """
        st.set_page_config(
            page_title=self.pageTitle,
            page_icon=" ",
            layout="centered",
            initial_sidebar_state="auto",
        )
        with st.container():
            # Titre
            st.title(self.stTitle)

        # Sidebar
        st.sidebar.header(self.sidebarHeader)
        st.sidebar.write(self.sideBarDescription)

    def create_tutorial(self, fields):
        """
        Crée un tutoriel interactif en fonction des champs spécifiés.

        Paramètres :
        - fields (dict) : Un dictionnaire contenant les champs du tutoriel.
        """
        # Barre de progression
        progress = st.progress(0)

        # Première étape
        if st.session_state.step == 0:
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            with col1:
                if st.button("Passer le tutoriel", id("skip_tutorial")):
                    st.page_link("http://www.google.com", label="Google", icon="🌎")

            with col6:
                if st.button("Commencer le tutoriel", id("start_tutorial")):
                    next_step()
                    progress.progress((st.session_state.step) / (len(fields)))  # Met à jour la jauge
                    st.sidebar.write(st.session_state.step)
                    st.session_state.button_pressed = True

        # Les autres étapes
        if 0 < st.session_state.step:
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            with col1:
                if st.button("Étape précédente", id("previous_step")):
                    previous_step()
                    st.session_state.button_pressed = True

            with col6:
                if st.session_state.step != len(fields):
                    if st.button("Étape suivante", id("next_step")):
                        next_step()
                        st.session_state.button_pressed = True

                else:
                    st.session_state.button_pressed = True
                    if st.button("Fin du tutoriel", id("end_tutorial")):
                        return
                display_step(progress, fields)

            if st.session_state.button_pressed is True:
                if st.session_state.step != 0:
                    display_texts(fields, add_step=-1)
                    st.sidebar.write(st.session_state.step)
                    st.session_state.button_pressed = False


def next_step():
    """
    Augmente le compteur d'étapes de 1.
    """
    st.session_state.step += 1


def previous_step():
    """
    Réduit le compteur d'étapes de 1.
    """
    st.session_state.step -= 1


def reset_tutorial():
    """
    Réinitialise le tutoriel en remettant le compteur d'étapes à 0.
    """
    st.session_state.step = 0


def display_step(progress, fields, add_step=0):
    progress.progress((st.session_state.step + add_step) / (len(fields)))  # Met à jour la jauge
    st.write(f"Étape {st.session_state.step + add_step} sur {len(fields)}")  # Affiche les étapes


def display_texts(fields, add_step=0):
    st.header(list(fields.keys())[st.session_state.step + add_step])
    for line in list(fields.values())[st.session_state.step + add_step]:
        if line.startswith("img¤"):
            st.image(line[4:])
        if line.startswith("code¤"):
            st.code(line[5:])
        else:
            st.write(line)
