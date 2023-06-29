import streamlit as st
from PIL import Image

def titulo_pag():

     # Título da aba do navegador
     st.set_page_config(page_title="Solicitação de GECC", initial_sidebar_state="auto")


     # configurações de estilo
     with open("arquivos/css.css") as f:
          st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
          
     # configurações logo e título
     with st.container():
          col_1, col_2 = st.columns([1,5])
          with col_1:
               #logo unb
               #image = Image.open('img/logo_unb_2.png')
               #st.image(image, caption="Universidade de Brasília")
               #pass
               st.subheader('SOLICITAÇÃO DE PAGAMENTO DE GECC')
          with col_2:
               #Título da página
               st.write("(Art. 76-A da Lei nº 8.112/1990, Decreto nº 11.069/2022-ME)")
