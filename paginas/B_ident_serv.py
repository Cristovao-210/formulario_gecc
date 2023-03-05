from funcoes.functions import *
import streamlit as st
from funcoes.functions import titulacao_item_1
#import pandas as pd


def identificacao_servidor():
    dados_gecc = {}
    limpar = True
    with st.expander("1 - Identificação do(a) Servidor(a) Público Federal Ativo", expanded=True):
        with st.form(key="Campo_1", clear_on_submit=limpar):
            col_1_cp_1, col_2_cp_1 = st.columns(2)
            with col_1_cp_1:
                dados_gecc['nome_completo_cp_1'] = st.text_input("Nome Completo")
                dados_gecc['cpf_cp_1'] = st.text_input("CPF (Sem caractéres especiais)", max_chars=11)  #, step=1, format="%d"
                dados_gecc['matricula_SIAPE'] = st.number_input("Matrícula SIAPE", step=1, format="%d")
                dados_gecc['email_cp_1'] = st.text_input("E-mail")
                dados_gecc['telefone_cp_1'] =  st.text_input("Telefone (Com DDD e Sem caractéres especiais)",max_chars=11)#st.number_input("Telefone", step=1, format="%d")
            with col_2_cp_1:
                dados_gecc['matricula_orgao_cp_1'] = st.number_input("Matrícula Órgão do Servidor", step=1, format="%d")
                dados_gecc['lotacao_cp_1'] = st.text_input("Lotação")
                dados_gecc['cargo_cp_1'] = st.text_input("Cargo") 
                dados_gecc['funcao_cp_1'] = st.text_input("Função")
                dados_gecc['titulacao_cp_1'] = st.selectbox("Titulação",titulacao_item_1)
            # botão para salvar preenchimento e limpar campos
            btn_submit_cp_1 = st.form_submit_button("SALVAR DADOS DO SERVIDOR")
            if btn_submit_cp_1:
                if dados_gecc['nome_completo_cp_1'] == "":
                    st.error("Campo obrigatório não preenchido: 'Nome Completo'")
                else:
                    try:
                        gravar_dados_gecc(dados_gecc,"campo_servidor")
                        st.success("As informações foram salvas com sucesso!\n Acesse a opção: 'Dados Bancários'")
                    except:
                        st.error("Não foi possível completar a operação. Aguarde alguns instantes e repita a operação.")
                    

            

        # tabela_servidor = {"Servidor": [dados_gecc['nome_completo_cp_1'],
        #                                 dados_gecc['matricula_orgao_cp_1'],
        #                                 dados_gecc['matricula_SIAPE'],
        #                                 dados_gecc['cpf_cp_1'],
        #                                 dados_gecc['lotacao_cp_1'],
        #                                 dados_gecc['email_cp_1'],
        #                                 dados_gecc['cargo_cp_1'],
        #                                 dados_gecc['telefone_cp_1'],
        #                                 dados_gecc['funcao_cp_1'],
        #                                 dados_gecc['titulacao_cp_1']] }
        # df_cp_1 = pd.DataFrame(tabela_servidor, index=["Nome", "Matrícula Órgão do Servidor", "Matrícula SIAPE", "CPF", "Lotação", "E-mail", "Cargo", "Telefone", "Funçao", "Titulação"])
        # st.sidebar.table(data=df_cp_1)
        
