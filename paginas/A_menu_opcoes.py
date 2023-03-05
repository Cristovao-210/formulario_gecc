import streamlit as st
from streamlit_option_menu import option_menu
from paginas.resolucao_cad import *



def menu_lateral():
    with st.sidebar:

        opcao_menu_navegacao = option_menu(

            menu_title="Formulário para solicitação de GECC",
            options=["Instruções para o preenchimento","Dados do Servidor", "Dados Bancários", "Órgão do Servidor", "Órgão Responsável", "Fonte Financiadora", "Atividades Executadas", "Gerar Formulário"],
            icons=["info-square","person","credit-card","house","bank","cash","calendar3","download"],
            menu_icon="card-text",
            default_index=0,
            orientation="vertical",
            styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "blue", "font-size": "20px"}, 
            "menu_icon": {"color": "blue", "font-size": "20px"},
            "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "rgb(77, 146, 77)"},}       
        )

        #st.write("Para verificar os valores máximos da GECC por hora trabalhada acesse o normativo abaixo.")
        with st.expander("Anexo I da Resolução do CAD 004/2012"):
            st.markdown(resolucao_do_cad, unsafe_allow_html=True)


        return opcao_menu_navegacao
