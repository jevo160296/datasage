import streamlit as st


def trim_line_jumps(text: str):
    return '\n'.join(text.split('\n')[1:-1])


class Articulo:
    def __init__(self, titulo: str, markdown):
        self.titulo = titulo
        self.markdown = markdown

    def render(self):
        st.title(self.titulo)

        st.markdown(self.markdown)
