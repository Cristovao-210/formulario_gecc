from funcoes.functions import *
import streamlit as st



# variável de controle
grupo_recebido = ""
# formulário para preencimento das informações pertinentes às atividades
def formulario_atividades(grupo_atvd, lista_atvd):

    global grupo_recebido
    percen_hora_trabalhada = None
    # para gravar dados inseridos
    dados_atividades = {}

    # Verificando o grupo de atividade para colocar a descrição correta
    if grupo_atvd == "A":
        descricao_gp_atividades = descricao_dos_grupos[0]
    elif grupo_atvd == "B":
        descricao_gp_atividades = descricao_dos_grupos[1]
    elif grupo_atvd == "C":
        descricao_gp_atividades = descricao_dos_grupos[2]
    elif grupo_atvd == "D":
        descricao_gp_atividades = descricao_dos_grupos[3]

    with st.expander(f"{descricao_gp_atividades}", expanded=True): #Grupo {grupo_atvd} - 
        
       
        dados_atividades['nome_atividade_cp_6'] = st.selectbox(f"Selecione a Atividade", lista_atvd)
        #a depender da atividade o percentual de hora trabalhada muda FAZER UM IF
        chave_dict = dados_atividades['nome_atividade_cp_6'][0:3].strip()
        cod_atv = chave_dict
        percen_hora_trabalhada = percentuais_hora_trabalhada.get(cod_atv)

        # captura da data
        try:
            inicial_data, final_data = st.columns(2)
            with inicial_data:
                dados_atividades['data_inicial_cp_6'] = st.date_input("Data Inicial", key=f'{grupo_atvd}-inicial')
                limite_data_final = dados_atividades['data_inicial_cp_6']
                #st.write(data_convertida_br(str(dados_atividades["data_inicial_cp_6"])))
            with final_data:
                dados_atividades['data_final_cp_6'] = st.date_input("Data Final", value=limite_data_final, min_value=limite_data_final, key=f'{grupo_atvd}-final')
                #st.write(data_convertida_br(str(dados_atividades["data_final_cp_6"])))
        except:
            st.error(f"A data inicial não pode ser maior que a data final - Altere a data inicial para continuar.")

        with st.form(key=grupo_atvd, clear_on_submit=True):
            
            
            
            col_3, col_4 = st.columns(2)

            with col_3:
                dados_atividades['percentual_hora_cp_6'] = st.number_input("Percentual por hora trabalhada",
                                                                                step=0.0001, format="%.4f", max_value=percen_hora_trabalhada)
                # a base para o cálculo da hora trabalhada é resolução cad 04/2012 -  R$27.303,62 
                ref_cad_04_2012 = 27303.62
                valor_hora_trab = (dados_atividades["percentual_hora_cp_6"] * ref_cad_04_2012) / 100
                dados_atividades['valor_hora_trab_cp_6'] = f'{valor_hora_trab:,.2f}'
                dados_atividades['valor_total'] = 0.0

            with col_4:
        
                dados_atividades['hora_total'] = st.number_input("Total de horas",step=0.01, format="%.2f")
                # o valor total é a hora_total * valor_hora_trabalhada         
                valor_total = float(dados_atividades["valor_hora_trab_cp_6"]) * float(dados_atividades["hora_total"])
                dados_atividades['valor_total'] = f'{valor_total:.2f}'
            

            gravar_dados = st.form_submit_button("SALVAR INFORMAÇÕES DA ATIVIDADE")
            if gravar_dados:
               
                valor_total_atvd = f'{valor_total:_.2f}'
                st.write(f'Valor total pago pela atividade do Grupo {grupo_atvd}: R$ {valor_total_atvd.replace(".",",").replace("_",".")}')
                
                if grupo_atvd == "A":
                    grupo_recebido = "A"
                elif grupo_atvd == "B":
                    grupo_recebido = "B"
                elif grupo_atvd == "C":
                    grupo_recebido = "C"
                elif grupo_atvd == "D":
                    grupo_recebido = "D"

                st.success("INFORMAÇÕES DA ATIVIDADE SALVAS COM SUCESSO!")#a depender da atividade o percentual de hora trabalhada muda FAZER UM IF


    return dados_atividades
                    




def atividades_executadas():

   
    Grupo_A, Grupo_B, Grupo_C, Grupo_D = st.tabs(["Grupo A", "Grupo B", "Grupo C", "Grupo D"])

    with Grupo_A:
        # Grupo A
        lista_A = formulario_atividades("A", lista_de_atividades_A)
        # Salvando informações em variáveis para que sejam sobrescritas sempre que mudar de opção
        nome_atv_A = lista_A['nome_atividade_cp_6'] 
        percent_A = lista_A['percentual_hora_cp_6'] 
        valor_hora_A = lista_A['valor_hora_trab_cp_6'] 
        dt_ini_A = lista_A['data_inicial_cp_6'] 
        dt_fim_A = lista_A['data_final_cp_6']
        h_total_A = lista_A['hora_total']
        v_final_A = lista_A['valor_total']
        # Garantindo que não seja gravado sem o nome da atividade
        if nome_atv_A == "":
            percent_A = 0.0
            valor_hora_A = 0.0
            dt_ini_A = ""
            dt_fim_A = ""
            h_total_A = 0.0
            v_final_A = 0.0

    with Grupo_B:
        # Grupo B
        lista_B = formulario_atividades("B", lista_de_atividades_B)
        # Salvando informações em variáveis para que sejam sobrescritas sempre que mudar de opção
        nome_atv_B = lista_B['nome_atividade_cp_6'] 
        percent_B = lista_B['percentual_hora_cp_6'] 
        valor_hora_B = lista_B['valor_hora_trab_cp_6'] 
        dt_ini_B = lista_B['data_inicial_cp_6'] 
        dt_fim_B = lista_B['data_final_cp_6']
        h_total_B = lista_B['hora_total']
        v_final_B = lista_B['valor_total']
        # Garantindo que não seja gravado sem o nome da atividade
        if nome_atv_B == "":
            percent_B = 0.0
            valor_hora_B = 0.0
            dt_ini_B = ""
            dt_fim_B = ""
            h_total_B = 0.0
            v_final_B = 0.0

    with Grupo_C:
        # Grupo C
        lista_C = formulario_atividades("C", lista_de_atividades_C)
        # Salvando informações em variáveis para que sejam sobrescritas sempre que mudar de opção
        nome_atv_C = lista_C['nome_atividade_cp_6'] 
        percent_C = lista_C['percentual_hora_cp_6'] 
        valor_hora_C = lista_C['valor_hora_trab_cp_6'] 
        dt_ini_C = lista_C['data_inicial_cp_6'] 
        dt_fim_C = lista_C['data_final_cp_6']
        h_total_C = lista_C['hora_total']
        v_final_C = lista_C['valor_total']
        # Garantindo que não seja gravado sem o nome da atividade
        if nome_atv_C == "":
            percent_C = 0.0
            valor_hora_C = 0.0
            dt_ini_C = ""
            dt_fim_C = ""
            h_total_C = 0.0
            v_final_C = 0.0
    
    with Grupo_D:
        # Grupo D
        lista_D = formulario_atividades("D", lista_de_atividades_D)
       # Salvando informações em variáveis para que sejam sobrescritas sempre que mudar de opção
        nome_atv_D = lista_D['nome_atividade_cp_6'] 
        percent_D = lista_D['percentual_hora_cp_6'] 
        valor_hora_D = lista_D['valor_hora_trab_cp_6'] 
        dt_ini_D = lista_D['data_inicial_cp_6'] 
        dt_fim_D = lista_D['data_final_cp_6']
        h_total_D = lista_D['hora_total']
        v_final_D = lista_D['valor_total']
        # Garantindo que não seja gravado sem o nome da atividade
        if nome_atv_D == "":
            percent_D = 0.0
            valor_hora_D = 0.0
            dt_ini_D = ""
            dt_fim_D = ""
            h_total_D = 0.0
            v_final_D = 0.0

    # Gerando estrutura de dados para guardar informações
    tabela_atividades = {"Grupo A":[nome_atv_A, 
                                    str(percent_A), 
                                    str(valor_hora_A), 
                                    data_convertida_br(str(dt_ini_A)), 
                                    data_convertida_br(str(dt_fim_A)), 
                                    str(h_total_A), 
                                    str(v_final_A)],
                         "Grupo B":[nome_atv_B, 
                                    str(percent_B), 
                                    str(valor_hora_B),
                                    data_convertida_br(str(dt_ini_B)), 
                                    data_convertida_br(str(dt_fim_B)), 
                                    str(h_total_B),
                                    str(v_final_B)],
                         "Grupo C":[nome_atv_C, 
                                    str(percent_C), 
                                    str(valor_hora_C), 
                                    data_convertida_br(str(dt_ini_C)), 
                                    data_convertida_br(str(dt_fim_C)), 
                                    str(h_total_C), 
                                    str(v_final_C)],
                         "Grupo D":[nome_atv_D, 
                                    str(percent_D), 
                                    str(valor_hora_D), 
                                    data_convertida_br(str(dt_ini_D)), 
                                    data_convertida_br(str(dt_fim_D)), 
                                    str(h_total_D), 
                                    str(v_final_D)]}
    
    global grupo_recebido
    # verificar qual aquivo será gravado
    if grupo_recebido == "A":#len(tabela_atividades["Grupo A"][0]) > 0:
        gravar_dados_gecc_atividades(tabela_atividades["Grupo A"], f"campo_atividades_A")
        grupo_recebido = ""
    if grupo_recebido == "B":#len(tabela_atividades["Grupo B"][0]) > 0:
        gravar_dados_gecc_atividades(tabela_atividades["Grupo B"], f"campo_atividades_B")
        grupo_recebido = ""
    if grupo_recebido == "C":#len(tabela_atividades["Grupo C"][0]) > 0:
        gravar_dados_gecc_atividades(tabela_atividades["Grupo C"], f"campo_atividades_C")
        grupo_recebido = ""
    if grupo_recebido == "D":#len(tabela_atividades["Grupo D"][0]) > 0:
        gravar_dados_gecc_atividades(tabela_atividades["Grupo D"], f"campo_atividades_D")
        grupo_recebido = ""
    


    # st.write(len(tabela_atividades["Grupo A"]))
    # df = pd.DataFrame(tabela_atividades, index=["Atividade", "% Hora Trab.", "R$ Hora Trab.", "Data Inicial", "Data Final", "Total Horas", "Valor Total"])
    # st.sidebar.table(data=df)
        
    
