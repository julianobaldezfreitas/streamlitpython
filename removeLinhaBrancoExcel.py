import pandas as pd
import streamlit as st

def download_arquivo(arquivo_excel):
    arquivo_excel.to_excel('exemplo.xlsx', index=False)  # Salvar o DataFrame em um arquivo CSV
    with open('exemplo.xlsx', 'rb') as file:
        st.download_button(
            label='Clique para fazer o download',
            data=file,
            key='download_button',
            file_name='saida.xlsx'
        )

def remover_linhas_em_branco(arquivo_excel):
    df = pd.read_excel(arquivo_excel)

    # remover linhas em branco
    df.dropna(axis=0, how="all", subset=None, inplace=True)

    # remover colunas em branco (deve remover colunas B e C)
    df.dropna(axis=1, how="all", subset=None, inplace=True)

    novo_dataframe = pd.DataFrame(columns=df.columns)

    # Iterar pelas linhas do arquivo Excel
    for indice, linha in df.iterrows():
        print(linha.iloc[0])
        # Verificar se o texto da primeira coluna é diferente de "Data"
        if linha.iloc[0] != "Data":
            novo_dataframe = novo_dataframe.append(linha)

    return novo_dataframe

# Configuração do aplicativo Streamlit
st.title("Remover Linhas em Branco de Arquivo Excel")

uploaded_file = st.file_uploader("Faça o upload do arquivo Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    # Remover linhas em branco
    df_sem_linhas_em_branco = remover_linhas_em_branco(uploaded_file)

    # Mostrar o DataFrame resultante
    st.dataframe(df_sem_linhas_em_branco)

    # Opção para salvar o novo arquivo
    if st.button("Salvar Arquivo Sem Linhas em Branco"):
        st.write("Salvando o arquivo...")
        #df_sem_linhas_em_branco.to_excel("arquivo_sem_linhas_em_branco.xlsx", index=False)
        download_arquivo(df_sem_linhas_em_branco)
        st.write("Arquivo salvo com sucesso!")

