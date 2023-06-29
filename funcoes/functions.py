import streamlit as st
import pandas as pd
import os



# variáveis globais
lista_nome_arq_gerados = ["campo_atividades_A.txt", 
                            "campo_atividades_B.txt", 
                            "campo_atividades_C.txt", 
                            "campo_atividades_D.txt", 
                            "campo_servidor.txt", 
                            "campo_dados_bancarios.txt", 
                            "campo_orgao_servidor.txt", 
                            "campo_orgao_responsavel.txt", 
                            "campo_fonte_financiadora.txt",]

arquivos_atividades_nao_criados = ["", 0.0, 0.0, "", "", 0.0, 0.0]

#dados_gecc = {}
titulacao_item_1 = ["",  "Ensino Médio",
                         "Graduação",
                         "Especialização",
                         "Mestrado",
                         "Doutorado"
                         ] #"Pós-doutorado" "Experiência Comprovada", "Educação Profissional ou Tecnológica",

# Valores para cálculo do percentual
percentuais_hora_trabalhada = {
    "A1": 1.47,
    "A2": 1.47,
    "A3": 0.97,
    "A4": 0.97,
    "A5": 1.47,
    "A6": 1.47,
    "A7": 1.47,
    "A8": 0.50,
    "A9": 0.97,
    "A10": 0.97,
    "A11": 1.47,
    "A12": 1.47,
  
    "B1": 1.37,
    "B2": 0.8,
    "B3": 1.47,
    "B4": 1.47,
    "B5": 1.47,
    "B6": 1.17,
    "B7": 1.47,
    "B8": 1.47,
  
    "C1": 0.8,
    "C2": 0.8,
    "C3": 0.6,
    "C4": 0.5,
  
    "D1": 0.3,
    "D2": 0.6,
    "D3": 0.8
}

# Atividades grupo A
lista_de_atividades_A = [
    "",
    "A1 - Instrutoria em curso de formação de carreiras",
    "A2 - Instrutoria em curso de desenvolvimento e aperfeiçoamento",
    "A3 - Instrutoria em curso de treinamento",
    "A4 - Tutoria em curso a distância",
    "A5 - Instrutoria em curso gerencial",
    "A6 - Instrutoria em curso de pós-graduação",
    "A7 - Orientação de monografia",
    "A8 - Instrutoria em curso de educação de jovens e adultos",
    "A9 - Coordenação técnica e pedagógica",
    "A10 - Elaboração de material didático",
    "A11 - Elaboração de material multimídia para curso a distância",
    "A12 - Atividade de conferencista e de palestrante em evento de capacitação"

]

# Atividades grupo B
lista_de_atividades_B = [

    "",
    "B1 - Exame oral",
    "B2 - Análise curricular",
    "B3 - Correção de prova discursiva",
    "B4 - Elaboração de questão de prova",
    "B5 - Julgamento de recurso",
    "B6 - Prova prática",
    "B7 - Análise crítica de questão de prova",
    "B8 - Julgamento de concurso de monografia"
]

# Atividades grupo 
lista_de_atividades_C = [

    "",
    "C1 - Planejamento",
    "C2 - Coordenação",
    "C3 - Supervisão",
    "C4 - Execução"
]

# Atividades grupo 
lista_de_atividades_D = [

    "",
    "D1 - Aplicação",
    "D2 - Fiscalização",
    "D3 - Supervisão"
]

# Nome dos grupos
descricao_dos_grupos = [

    "Instrutoria em curso de formação, ou instrutoria em cursos de desenvolvimento ou de treinamento para servidores, regularmente instituído no âmbito da administração pública federal.",
    "Banca examinadora ou de comissão para exames orais, análise curricular, correção de provas discursivas, elaboração de questões de provas ou para jugamento de recursos intentados por candidatos.",
    "Logística de preparação e de realização de curso, concurso público ou exame vestibular - planejamento, coordenação, supervisão e execução.",
    "Aplicação, fiscalização ou supervisão de provas de exame vestibular ou de concurso público."

]


# função para deixar data recebida no formato necessário
def data_convertida_br(dt): # recebe uma String
  dia = dt[8:]
  mes = dt[5:7]
  ano = dt[0:4]
  if dia == "":
    return ""
  else:
    return f'{dia}/{mes}/{ano}' # retorna uma String

# persistindo informações geradas pelos formulários
def gravar_dados_gecc(dados, nome_arquivo):
    lista_dados = []
    for chave in dados:
        lista_dados.append(dados[chave])
    with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as db:
       db.write(str(lista_dados))

# ler e MOSTRAR informações salvas
def ler_arquivo_dados(nome_arq, texto_botao):
    dados_gravacao = []
    mostrar = st.button(f"{texto_botao}")
    if mostrar:
        with open(f"{nome_arq}.txt", "r", encoding="utf-8") as f:
            dados_arquivo = f.readline()
            for posicao in dados_arquivo.split(","):
                dados_gravacao.append(posicao.replace("[","").replace("]","").replace("'","").strip())
            st.write(dados_gravacao)
    return dados_gravacao

# LER informações salvas
def ler_arq_dados(nome_arq):
    dados_gravacao = []
    with open(f"{nome_arq}.txt", "r", encoding="utf-8") as f:
        dados_arquivo = f.readline()
        for posicao in dados_arquivo.split(","):
            dados_gravacao.append(posicao.replace("[","").replace("]","").replace("'","").strip())
        #st.write(dados_gravacao) DEBUG
    return dados_gravacao

# Criando tabela de visualização
def tabela_visualizacao_dados(infos, lista_colunas, lista_indices):
   with st.expander("Detalhamento", expanded=True):
        df_txt = pd.DataFrame(infos, columns=lista_colunas, index=lista_indices)
        st.table(data=df_txt)

# Baixar Arquivo
def baixar_formulario(form_gerado):
    coluna_1, coluna_2, coluna_3 = st.columns([2, 3, 1])
    with coluna_1:
        pass
    with coluna_2:
        with open(form_gerado[1], "rb") as file:
            # Como baixar documento gerado
            btn_baixar = st.download_button(
                        label="Baixar Formulário",
                        data=file,
                        file_name=form_gerado[1],
                        mime="text/html")
            
            if btn_baixar:
                for arquivo in lista_nome_arq_gerados:
                    os.remove(arquivo)
    with coluna_3:
        os.remove("Formulario_GECC.html")

# gravar atividades executadas
def gravar_dados_gecc_atividades(dados, nome_arquivo):
    lista_dados = []
    for dado in dados:
        lista_dados.append(f'{dado}')
    with open(f"{nome_arquivo}.txt", "w", encoding="utf-8") as db:
       db.write(str(lista_dados))
       

# ler atividades executadas
def ler_arq_dados_atividades(nome_arq):
    dados_gravacao = []
    with open(f"{nome_arq}.txt", "r", encoding="utf-8") as f:
        dados_arquivo = f.readline()
        for posicao in dados_arquivo.split(","):
            dados_gravacao.append(posicao.replace("[","").replace("]","").replace("'","").strip())
        #st.write(dados_gravacao) DEBUG
    return dados_gravacao

def msg_error_acessar_pag_anterior(nome_secao):
    st.error(f"Para acessar esta página é necessário que a opção '{nome_secao}' tenha sido preenchida (vide 'Instruções para o preenchimento').")
