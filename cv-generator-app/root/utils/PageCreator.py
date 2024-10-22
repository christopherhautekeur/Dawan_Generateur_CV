import streamlit as st


class PageCreator:

    def __init__(self, pageTitle="", stTitle="", sidebarHeader="", sideBarDescription=""):
        self.pageTitle = pageTitle
        self.stTitle = stTitle
        self.sidebarHeader = sidebarHeader
        self.sideBarDescription = sideBarDescription

        if 'step' not in st.session_state:
            st.session_state.step = 0

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
        # Titre
        st.subheader(f"{self.stTitle} - Tutoriel")

        # Barre de progression
        progress = st.progress(0)
        st.write(len(fields))

        with st.container():
            # Première étape
            if st.session_state.step == 0:
                    col1, col2, col3, col4, col5, col6 = st.columns(6)
                    with col1:
                        if st.button("Passer le tutoriel", id("skip_tutorial")):
                            st.session_state.step = len(fields) + 1
                    with col6:
                        if st.button("Commencer le tutoriel"):
                            next_step()
                            progress.progress((st.session_state.step) / (len(fields)))  # Met à jour la jauge
                            st.sidebar.write(st.session_state.step)

        with st.container():
            # Les autres étapes
            if len(fields) > st.session_state.step > 0:
                    display_texts(fields)
                    col1, col2, col3, col4, col5, col6 = st.columns(6)
                    with col1:
                        if st.button("Étape précédente", id("previous_step")):
                            previous_step()
                            display_step(progress, fields)
                            st.sidebar.write(st.session_state.step)

                    with col6:
                        if st.session_state.step == len(fields):
                            if st.button("Fin du tutoriel", id("end_step")):
                                with st.container():
                                    st.subheader("")

                        else:
                            if st.button("Étape suivante", id("next_step")):
                                next_step()
                                display_step(progress, fields)
                                st.sidebar.write(st.session_state.step)
        # with st.container():
        #     # Dernière étape
        #     if st.session_state.step == len(fields) + 1:
        #         st.write("Tutoriel terminé !")
        #
        #         col1, col2, col3, col4, col5 = st.columns(5)
        #         with col1:
        #             # Réinitialisation du tutoriel
        #             if st.button("Recommencer le tutoriel", id("reset_tutorial")):
        #                 reset_tutorial()
        #                 display_step(progress, fields)
        #
        #         with col5:
        #             # Bouton pour quitter le tutoriel
        #             if st.button("Quitter le tutoriel", id("exit_tutorial")):
        #                 with st.container():
        #                     st.empty()


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


def display_texts(fields):
    st.header(list(fields.keys())[st.session_state.step])
    st.write(list(fields.values())[st.session_state.step])
