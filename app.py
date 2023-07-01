import streamlit as st
from paginas.titulo import *
from paginas.A_menu_opcoes import menu_lateral
from paginas.B_ident_serv import *
from paginas.C_dados_bancarios import *
from paginas.D_orgao_servidor import *
from paginas.E_orgao_responsavel import *
from paginas.F_fonte_financiadora import *
from paginas.G_atividades import *
from paginas.H_gerar_formulario import *
import os


# fixando o título na pagina
titulo_pag()

# criando barra lateral
opcao = menu_lateral()

# Verificando qual campo do foi selecionado e Criando o formulário equivalente
if opcao == "Instruções para o preenchimento":
    # st.markdown('<iframe src="https://scribehow.com/embed/Passo_a_passo_para_gerar_o_formulario_de_GECC__3iFPRlojQB67zK9rdJm9kw" width="640" height="640" allowfullscreen frameborder="0"></iframe>', unsafe_allow_html=True)

    st.markdown("<br><br><p style='text-align: center;'>Instruções para o preenchimento e inserção do formulário gerado no SEI</p><br>", unsafe_allow_html=True)
    try:
        video_file = open('img/inseri_form_gecc_sei.mp4', 'rb')
        video = video_file.read()
        st.video(video, start_time=1)
    except:
        st.error("Falha no carregamento do vídeo, aguarde alguns instantes e tente novamente.")
    pass
elif opcao == "Dados do Servidor":
    identificacao_servidor()
elif opcao == "Dados Bancários":
    if os.path.exists("campo_servidor.txt"):
        dados_bancarios()
    else:
        msg_error_acessar_pag_anterior('Dados do Servidor')
elif opcao == "Órgão do Servidor":
    if os.path.exists("campo_dados_bancarios.txt"):
        orgao_do_servidor()
    else:
        msg_error_acessar_pag_anterior('Dados Bancários')
elif opcao == "Órgão Responsável":
    if os.path.exists("campo_orgao_servidor.txt"):
        orgao_responsavel()
    else:
        msg_error_acessar_pag_anterior('Órgão do Servidor')
elif opcao == "Fonte Financiadora":
    if os.path.exists("campo_orgao_responsavel.txt"):
        fonte_financiadora()
    else:
        msg_error_acessar_pag_anterior('Órgão Responsável')
elif opcao == "Atividades Executadas":
    if os.path.exists("campo_fonte_financiadora.txt"):
        atividades_executadas()
    else:
        msg_error_acessar_pag_anterior('Fonte Financiadora')
elif opcao == "Gerar Formulário":

    try:
        info_servidor = ler_arq_dados("campo_servidor")
        info_dados_bancarios = ler_arq_dados("campo_dados_bancarios")
        info_orgao_servidor = ler_arq_dados("campo_orgao_servidor")
        info_orgao_responsavel = ler_arq_dados("campo_orgao_responsavel")
        info_fonte_financiadora = ler_arq_dados("campo_fonte_financiadora")

        # Configurando arquivos das atividades executadas
        info_atividades_executadas = []

        # Atividade Grupo A
        if os.path.exists("campo_atividades_A.txt"):
            info_atividades_executadas.append(ler_arq_dados_atividades("campo_atividades_A"))
        else:
            gravar_dados_gecc_atividades(arquivos_atividades_nao_criados, "campo_atividades_A")
            info_atividades_executadas.append(ler_arq_dados_atividades("campo_atividades_A"))

        # Atividade Grupo B
        if os.path.exists("campo_atividades_B.txt"):
            info_atividades_executadas.append(ler_arq_dados_atividades("campo_atividades_B"))
        else:
            gravar_dados_gecc_atividades(arquivos_atividades_nao_criados, "campo_atividades_B")
            info_atividades_executadas.append(ler_arq_dados_atividades("campo_atividades_B"))

        # Atividade Grupo C
        if os.path.exists("campo_atividades_C.txt"):
            info_atividades_executadas.append(ler_arq_dados_atividades("campo_atividades_C"))
        else:
            gravar_dados_gecc_atividades(arquivos_atividades_nao_criados, "campo_atividades_C")
            info_atividades_executadas.append(ler_arq_dados_atividades("campo_atividades_C"))

        # Atividade Grupo D
        if os.path.exists("campo_atividades_D.txt"):
            info_atividades_executadas.append(ler_arq_dados_atividades("campo_atividades_D"))
        else:
            gravar_dados_gecc_atividades(arquivos_atividades_nao_criados, "campo_atividades_D")
            info_atividades_executadas.append(ler_arq_dados_atividades("campo_atividades_D"))


        form_gerado = gerar_formulario_html(info_servidor,
                                            info_dados_bancarios, 
                                            info_orgao_servidor, 
                                            info_orgao_responsavel, 
                                            info_fonte_financiadora,
                                            info_atividades_executadas)

        baixar_formulario(form_gerado)


    except: #FileNotFoundError as error:
        st.warning(f"Ainda existem campos não preenchidos. Preencha todos para poder baixar o formulário")# -- {error}")
                
                



