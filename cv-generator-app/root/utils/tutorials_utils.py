import streamlit as st


def create_tutorial(fields):
    """
    Crée un tutoriel interactif en fonction des champs spécifiés.

    Paramètres :
    - fields (dict) : Un dictionnaire contenant les champs du tutoriel.
    """
    # Barre de progression
    progress = st.progress(0)

    # Première étape
    if st.session_state.step == 0:
        with st.empty():
            if st.button("Commencer le tutoriel"):
                next_step()
                progress.progress((st.session_state.step) / (len(fields)))  # Met à jour la jauge
                st.session_state.button_pressed = True
                st.write("")

    # Les autres étapes
    if 0 < st.session_state.step:
        if st.session_state.step > len(fields) - 1:
            pass
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            if st.button("Étape précédente", id("previous_step")):
                previous_step()
                st.session_state.button_pressed = True

        with col6:
            if st.session_state.step == len(fields) - 1:
                next_step()
                st.session_state.button_pressed = True
                if st.button("Fin du tutoriel", id("end_tutorial")):
                    reset_tutorial()
            else:
                if st.button("Étape suivante", id("next_step")):
                    next_step()
                    st.session_state.button_pressed = True

            display_step(progress, fields)

        if st.session_state.button_pressed is True:
            if st.session_state.step != 0:
                display_texts(fields, add_step=-1)
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
