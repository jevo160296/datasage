import streamlit as st
from pagina_principal import main


def trim_line_jumps(text: str):
    return '\n'.join(text.split('\n')[1:-1])


def redirect_button(url: str, text: str = None, color="#FD504D"):
    st.markdown(
        f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            margin: 1em 0em 1em 0em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
        unsafe_allow_html=True
    )


class Articulo:
    def __init__(self, titulo: str, markdown):
        self.titulo = titulo
        self.markdown = markdown

    def render(self):
        main_page_link = 'Conoce_nuestros_servicios'

        st.title(self.titulo)

        redirect_button(main_page_link, "Conoce nuestros servicios")

        st.markdown(self.markdown)

        redirect_button(main_page_link, "Conoce nuestros servicios")
