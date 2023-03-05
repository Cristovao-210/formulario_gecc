from funcoes.functions import *
import streamlit as st


 # 2 - Dados Bancários  
def dados_bancarios():
    dados_gecc = {}
    with st.expander("2 - Dados Bancários do(a) Servidor(a)", expanded=True):
        with st.form(key="Campo_2", clear_on_submit=True):
            col_1_cp_2, col_2_cp_2, col_3_cp_2 = st.columns(3)
            with col_1_cp_2:
                dados_gecc['banco_cp_2'] = st.number_input("Banco", step=1, format="%d")
            with col_2_cp_2:
                dados_gecc['agencia_cp_2'] = st.number_input("Agência", step=1, format="%d")
            with col_3_cp_2:
                dados_gecc['conta_cp_2'] = st.number_input("Conta", step=1, format="%d")
            # botão para salvar preenchimento e limpar campos
            btn_submit_cp_2 = st.form_submit_button("SALVAR DADOS BANCÁRIOS")
            if btn_submit_cp_2:
                try:
                    gravar_dados_gecc(dados_gecc, "campo_dados_bancarios")
                    st.success("As informações foram salvas com sucesso!\n Acesse a opção: 'Órgão Servidor'")
                except:
                    st.error("Não foi possível completar a operação. Aguarde alguns instantes e repita a operação.")
                     