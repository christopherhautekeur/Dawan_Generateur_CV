import streamlit as st


class PageCreator:

    def __init__(self, pageTitle="", stTitle="", sidebarHeader="", sideBarDescription=""):
        self.pageTitle = pageTitle
        self.stTitle = stTitle
        self.sidebarHeader = sidebarHeader
        self.sideBarDescription = sideBarDescription

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

        # Titre
        st.title(self.stTitle)

        # Sidebar
        st.sidebar.header(self.sidebarHeader)
        st.sidebar.write(self.sideBarDescription)
