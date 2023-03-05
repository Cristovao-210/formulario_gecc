from funcoes.functions import *
import streamlit as st
from paginas import *



def orgao_do_servidor():
       dados_gecc = {}
    # 3 - Identificação do Órgão
       with st.expander("3 - Identificação do Órgão / Entidade Federal de Exercício do(a) Servidor(a)", expanded=True):
            escolha_orgao_servidor = st.radio("Informe o Órgão / Entidade", ('UnB', 'Outro Órgão/Entidade Federal'), label_visibility="hidden") # pular para o Item 4 
            if escolha_orgao_servidor == 'UnB':
                dados_gecc['orgao_unb_cp_3'] = st.text_input("Órgão / Entidade Federal Responsável.", value='UnB', disabled=True)
                btn_avancar_3 = st.button("SALVAR INFORMAÇÕES DO ÓRGÃO DE EXERCÍCIO DO SERVIDOR")
                if btn_avancar_3:
                    try:
                        gravar_dados_gecc(dados_gecc,"campo_orgao_servidor")
                        st.success("As informações foram salvas com sucesso!\n Acesse a aba 'Órgão Responsável'")
                    except:
                         st.error("Não foi possível completar a operação. Aguarde alguns instantes e repita a operação.")
            elif escolha_orgao_servidor == 'Outro Órgão/Entidade Federal':
                st.write("Preencha os demais campos deste item")
                with st.form(key="Campo_3", clear_on_submit=True):
                    col_1_cp_3, col_2_cp_3 = st.columns(2)
                    with col_1_cp_3:
                        dados_gecc['orgao_unb_cp_3'] = st.text_input("Nome do Órgão")
                        dados_gecc["gestao_5_digitos_cp_3"] = st.number_input("Gestão (5 dígitos)", step=1, format="%d",max_value=99999)
                        dados_gecc["endereco_cp_3"] = st.text_input("Endereço")
                    with col_2_cp_3:
                        dados_gecc['cnpj_cp_3'] = st.text_input("CNPJ", max_chars=14)    
                        dados_gecc["ug_6_digitos_cp_3"] = st.number_input("UG (6 dígitos)", step=1, format="%d",max_value=999999)
                        dados_gecc["cep"] = st.number_input("CEP", step=1, format="%d",max_value=99999999)
                    dados_gecc["nome_dir_max_cp_3"] = st.text_input("Nome do Dirigente Máximo")
                    # botão para salvar preenchimento e limpar campos
                    btn_submit_cp_3 = st.form_submit_button("SALVAR INFORMAÇÕES DO ÓRGÃO DE EXERCÍCIO DO SERVIDOR")
                    if btn_submit_cp_3:
                        try:
                            gravar_dados_gecc(dados_gecc,"campo_orgao_servidor")
                            st.success("As informações foram salvas com sucesso!\n Acesse a aba 'Órgão Responsável'")
                        except:
                            st.error("Não foi possível completar a operação. Aguarde alguns instantes e repita a operação.")


