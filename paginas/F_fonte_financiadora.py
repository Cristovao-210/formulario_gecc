from funcoes.functions import *
import streamlit as st
from paginas import *
#from funcoes.functions import dados_gecc


def fonte_financiadora():
    dados_gecc = {}
    with st.expander("5 - Identificação da Fonte Financiadora", expanded=True):
        with st.form(key="Campo_4", clear_on_submit=True):
            dados_gecc["nota_empenho_cp_5"] = st.number_input("Nº da Nota de Empenho - NE  (anexar cópia ao processo SEI):", step=1, format="%d")
            st.info('''* A Nota de empenho (NE) se aplica à solicitação cuja liquidação e pagamento 
                        serão processados na UnB com recursos próprios, 
                        Matriz, PDI ou descentralização  orçamentária encaminhada à FUB. ''')
            dados_gecc["nota_dotacao_cp_5"] = st.number_input("Nº da Nota de Dotação - ND (anexar cópia ao processo SEI):", step=1, format="%d")
            st.info('''* A Nota de dotação (ND) se aplica somente à solicitação de destaque orçamentário (transferência)
            para processamento do pagamento no órgão de origem do servidor que desenvolveu as atividades com recursos próprios, Matriz ou PDI.''')
            btn_submit_cp_3 = st.form_submit_button("SALVAR INFORMAÇÕES DA FONTE FINANCIADORA")
            if btn_submit_cp_3:
                try:
                    gravar_dados_gecc(dados_gecc,"campo_fonte_financiadora")
                    st.success("As informações foram salvas com sucesso!\n Acesse a opção: 'Atividades Executadas'")
                except:
                    st.error("Não foi possível completar a operação. Aguarde alguns instantes e repita a operação.")