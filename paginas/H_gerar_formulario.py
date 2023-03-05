from funcoes.functions import *
import streamlit as st



def gerar_formulario_html(arq_serv, arq_dados_bancarios, arq_orgao_servidor, arq_orgao_responsavel, arq_fonte_financiadora, arq_atividades):
    nome_do_arquivo = f"Formulario_GECC.html" # {arq_serv[1]}
    with open(nome_do_arquivo, "w", encoding="utf-8") as form_html:
        form_html.write(f'''<!--Autor: Márcio Cristóvão Silva da Rosa-->
        <table style="font-family: arial, sans-serif; border-collapse: collapse; width: 100%; margin: auto; border: 2px solid lightgray;">
        <tr>
            <th colspan="4" height="50px" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">

                <h3 style="text-align: center; font-size: 25px;">
                    SOLICITAÇÃO DE PAGAMENTO DA GECC
                </h3>
                <h6 style="text-align: center;">
                    (Art. 76-A da Lei nº 8.112/1990, Decreto nº 11.069/2022-ME)
                </h6>
                <br>
            </th>

        </tr>

        <tr style="background-color: #dddddd;">
            <td colspan="4" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <strong>
                    1 - Identificação ao(a) Servidor(a) Público Federal Ativo
                </strong>
            </td>

        </tr>

        <!--Identificação servidor-->

        <tr>
            <td width="50%" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">

                Nome Completo: <span>{arq_serv[0]}</span>
            </td>
            <td colspan="2" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                CPF: <span>{arq_serv[1][0:3]}.{arq_serv[1][3:6]}.{arq_serv[1][6:9]}-{arq_serv[1][9:]}</span>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                E-mail: <span>{arq_serv[3]}</span>
            </td>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Telefone: <span>{f'({arq_serv[4][0:2]}) {arq_serv[4][2:3]} {arq_serv[4][3:7]}-{arq_serv[4][7:]}'}</span>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Matrícula SIAPE: <span>{arq_serv[2]}</span>
            </td>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Mat. Órgão/Entidade Federal: <span>{arq_serv[5]}</span>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Lotação: <span>{arq_serv[6]}</span>
            </td>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Cargo: <span>{arq_serv[7]}</span>
            </td>
        </tr>

        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Função: <span>{arq_serv[8]}</span>
            </td>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Titulação: <span>{arq_serv[9]}</span>
            </td>
        </tr>

        <!--Dados Bancários-->

        <tr style="background-color: #dddddd;">
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <strong>
                    2 - Dados Bancários do(a) Servidor(a)
                </strong>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Banco: <span>{arq_dados_bancarios[0]}</span>
            </td>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Agência: <span>{arq_dados_bancarios[1]}</span>
            </td>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Conta Corrente: <span>{arq_dados_bancarios[2]}</span>
            </td>
        </tr>

        <!--Órgão do Servidor-->

        <tr style="background-color: #dddddd;">
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <strong>
                    3 - Identificação do Órgão / Entidade Federal de Exercício do(a) Servidor(a)
                </strong>
            </td>
        </tr>''')
        if arq_orgao_servidor[0] == "UnB":
            form_html.write(f'''
        
            <tr>
                <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                    <ul style="list-style-type: disc;">
                        <li>
                            UnB (Passe para o item 4)
                        </li>
                    </ul>
                    <ul style="list-style-type: circle;">
                        <li>
                            Outro Órgão/Entidade Federal (Preencha os demais campos deste item)
                        </li>
                    </ul>
                </td>
            </tr>''')
        else:
            form_html.write(f'''
            <tr>
                <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                    <ul style="list-style-type: circle; ">
                        <li>
                            UnB (Passe para o item 4)
                        </li>
                    </ul>
                    <ul style="list-style-type: disc;">
                        <li>
                            Outro Órgão/Entidade Federal (Preencha os demais campos deste item)
                        </li>
                    </ul>
                </td>
            </tr>
        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Nome: <span>{arq_orgao_servidor[0]}</span>
            </td>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                
                CNPJ: <span>{f'{arq_orgao_servidor[3][0:2]}.{arq_orgao_servidor[3][2:5]}.{arq_orgao_servidor[3][5:8]}/{arq_orgao_servidor[3][8:12]}-{arq_orgao_servidor[3][12:]}'}</span>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                UG (6 dígitos): <span>{arq_orgao_servidor[4]}</span>
            </td>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Gestão (5 dígitos): <span>{arq_orgao_servidor[1]}</span>
            </td>
        </tr>
        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Endereço: <span>{arq_orgao_servidor[2]}</span>
            </td>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                CEP: <span>{f'{arq_orgao_servidor[5][0:2]}.{arq_orgao_servidor[5][2:5]}-{arq_orgao_servidor[5][5:]}'}</span>
            </td>
        </tr>
        <tr>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Nome do Dirigente Máximo: <span>{arq_orgao_servidor[6]}</span>
            </td>
        </tr>
        
        

        ''')
        form_html.write(f'''

        <!--Órgão Responsável-->

        <tr style="background-color: #dddddd;">
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <strong>
                    4 - Identificação do Órgão / Entidade Federal Responsável pela Execução das Atividades e Solicitação
                    de Pagamento
                </strong>
            </td>
        </tr>
        ''')
        if len(arq_orgao_responsavel) > 1:
            form_html.write(f'''      
            <tr>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <ul style="list-style-type: disc;">
                    <li>
                        UnB - Unidade Resposável: <span>{arq_orgao_responsavel[1]}</span>
                    </li>
                </ul>
                <ul style="list-style-type: circle; ">
                    <li>
                        Outro Órgão/Entidade Federal - Nome: <span> </span>
                    </li>
                </ul>
            </td>
        </tr>''')
        else:
            form_html.write(f'''
            <tr>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <ul style="list-style-type: circle;">
                    <li>
                        UnB - Unidade Resposável: <span></span>
                    </li>
                </ul>
                <ul style="list-style-type: disc;">
                    <li>
                        Outro Órgão/Entidade Federal - Nome: <span>{arq_orgao_responsavel[0]}</span>
                    </li>
                </ul>
            </td>
        </tr>''')

        # Formatando saída da coluna valor total    
        valor_total_A = float(arq_atividades[0][6]) if float(arq_atividades[0][6]) > 0 else ""  
        valor_total_A_f = "" if valor_total_A == "" else f'{valor_total_A:_.2f}'

        valor_total_B = float(arq_atividades[1][6]) if float(arq_atividades[1][6]) > 0 else ""
        valor_total_B_f = "" if valor_total_B == "" else f'{valor_total_B:_.2f}'

        valor_total_C = float(arq_atividades[2][6]) if float(arq_atividades[2][6]) > 0 else ""
        valor_total_C_f = "" if valor_total_C == "" else f'{valor_total_C:_.2f}'

        valor_total_D = float(arq_atividades[3][6]) if float(arq_atividades[3][6]) > 0 else ""  
        valor_total_D_f = "" if valor_total_D == "" else f'{valor_total_D:_.2f}'

        form_html.write(f''' 
         
           <!--Fonte Financiadora-->
        
        <tr style="background-color: #dddddd;">
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <strong>
                    5 - Identificação da Fonte Financiadora
                </strong>
            </td>
        </tr>

        <tr>
            <td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Nº da Nota de Empenho - NE (Anexar cópia ao SEI): <span>{arq_fonte_financiadora[0]}</span>
            </td>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                Nº da Nota de Dotação - ND (Anexar cópia ao SEI): <span>{arq_fonte_financiadora[1]}</span>
            </td>
        </tr>

        <!--Atividades Executadas-->

        <tr style="background-color: #dddddd;">
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <strong>
                    6 - Atividades Executadas (Inserir as atividades realizadas somente no mês de referência)
                </strong>
            </td>
        </tr>
        <tr>
            <td colspan="3" style="border: 1px solid #dddddd; text-align: left; padding: 8px;">
                <table style="border-collapse: collapse; 
        width: 100%;">
                    <tr>
                        <th colspan="2" style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            Nome da Atividade <br>
                            <span style="font-size: 11px;">(conforme Decreto nº 11.069/2022-ME)</span>
                        </th>
                        <th style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span style="font-size: 14px;">Percentual <br> por Hora <br> Trabalhada</span>
                        </th>
                        <th style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span style="font-size: 14px;">Valor <br> por Hora <br> Trabalhada (R$)</span>
                        </th>
                        <th style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span style="font-size: 14px;">Período de <br> Realização</span>
                        </th>
                        <th style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span style="font-size: 14px;"> Total de <br> Horas</span>
                        </th>
                        <th style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span style="font-size: 14px;">Valor <br> Total (R$)</span>
                        </th>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: left;">
                            <strong>
                                Atividade A:
                            </strong>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                             <span>{arq_atividades[0][0]}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[0][1] if float(arq_atividades[0][1]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[0][2] if float(arq_atividades[0][2]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{arq_atividades[0][3]}</span> {"a"  if arq_atividades[0][3] != "" else "" } <span>{arq_atividades[0][4]}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[0][5] if float(arq_atividades[0][5]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{valor_total_A_f.replace(".",",").replace("_",".")}</span>
                        </td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: left;">
                            <strong>
                                Atividade B:
                            </strong>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{arq_atividades[1][0]}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                             <span>{f'{arq_atividades[1][1] if float(arq_atividades[1][1]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[1][2] if float(arq_atividades[1][2]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{arq_atividades[1][3]}</span> {"a"  if arq_atividades[1][3] != "" else "" } <span>{arq_atividades[1][4]}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[1][5] if float(arq_atividades[1][5]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{valor_total_B_f.replace(".",",").replace("_",".")}</span>
                        </td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: left;">
                            <strong>
                                Atividade C:
                            </strong>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{arq_atividades[2][0]}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[2][1] if float(arq_atividades[2][1]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[2][2] if float(arq_atividades[2][2]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{arq_atividades[2][3]}</span> {"a"  if arq_atividades[2][3] != "" else "" } <span>{arq_atividades[2][4]}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[2][5] if float(arq_atividades[2][5]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{valor_total_C_f.replace(".",",").replace("_",".")}</span>
                        </td>
                    </tr>
                    <tr>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: left;">
                            <strong>
                                Atividade D:
                            </strong>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{arq_atividades[3][0]}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[3][1] if float(arq_atividades[3][1]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[3][2] if float(arq_atividades[3][2]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{arq_atividades[3][3]}</span> {"a"  if arq_atividades[3][3] != "" else "" } <span>{arq_atividades[3][4]}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            <span>{f'{arq_atividades[3][5] if float(arq_atividades[3][5]) > 0 else ""}'.replace(".",",")}</span>
                        </td>
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            
                            <span>{valor_total_D_f.replace(".",",").replace("_",".")}</span>
                        </td>

                    </tr>
                    <tr>
                        <td colspan="6" style="text-align: right; border: 1px solid #dddddd; padding: 8px;">
                            <b>
                                Total Geral:
                            </b>
                        </td>''')
        soma = (float(arq_atividades[0][6]) + float(arq_atividades[1][6]) + float(arq_atividades[2][6]) + float(arq_atividades[3][6]))
        soma_f = f'{soma:_.2f}'
        form_html.write(f''' 
                        <td style="border: 1px solid #dddddd; padding: 8px; text-align: center;">
                            R$ <span>{soma_f.replace(".", ",").replace("_", ".")}</span>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>''') 
           
    return [form_html, nome_do_arquivo]
