from funcoes.functions import *
import streamlit as st



def orgao_responsavel():
    dados_gecc = {}
    with st.expander("4 - Identificação do Órgão / Entidade Federal Responsável pela Execução das Atividades e Solicitação de Pagamento", expanded=True):
            
            valor_selecionado = st.radio("Informe o Órgão / Entidade Responsável", ('UnB', 'Outro Órgão/Entidade Federal'))
            if valor_selecionado == 'UnB':
                dados_gecc['unb_responsavel'] = 'UnB'
                dados_gecc['unb_responsavel_cp_4'] = st.text_input("Unidade Responsável", value='', disabled=False, placeholder="UnB - Digite aqui o nome da Unidade Responsável")
            else:
                dados_gecc['unb_responsavel_cp_4'] = st.text_input("Órgão / Entidade Federal Responsável",placeholder="Digite aqui o nome do Órgão / Entidade Federal Responsável")
            btn_avancar_4 = st.button("SALVAR INFORMAÇÕES DO ÓRGÃO / ENTIDADE RESPONSÁVEL",)
            if btn_avancar_4:
                try:
                    gravar_dados_gecc(dados_gecc,"campo_orgao_responsavel")
                    st.success("As informações foram salvas com sucesso!\n Acesse a opção: 'Fonte Financiadora'")
                except:
                    st.error("Não foi possível completar a operação. Aguarde alguns instantes e repita a operação.")