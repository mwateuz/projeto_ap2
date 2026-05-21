# import pandas as pd
# import seaborn as sn
# import matplotlib.pyplot as plt


# df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
# df.columns
# plt.figure(figsize=(10,6))
# sn.countplot(data=df, x="setor", order=df["setor"].value_counts().index)

# plt.title("Grafico de Barras por setor")
# plt.xlabel("Numero de empresas")
# plt.ylabel("Setor")
# plt.xticks(rotation=45)
# plt.show()

# # Grafico de Pizza
# setor = df["setor"].value_counts()
# plt.figure(figsize=(10,6))
# plt.pie(setor, labels=setor.index)

# # Histograma
# filtro = df["setor"] == "seguro"
# df_setor = df[filtro]
# sn.histplot(df["roe"], bins=20, kde=True, color="blue")




# GIT e Github
import pandas as pd
import streamlit as st
import seaborn as sn
import matplotlib.pyplot as plt

# gravando o excel em uma variaveldf
df = pd.read_excel("planilhao.xlsx", sheet_name="Sheet1")
# titulo do dashboard
st.header("Meu dashboard 2.0")
menu = st.tabs(["tabela", "barra", "pizza", "Histograma"])
# expondo o df no dashboard
with menu[0]:
    st.dataframe(df)
with menu[1]:
    fig = plt.figure(figsize=(10,6))
    sn.countplot(data=df, x="setor", order=df["setor"].value_counts().index)
    plt.title("Grafico de Barras por setor")
    plt.xlabel("Numero de empresas")
    plt.ylabel("Setor")
    plt.xticks(rotation=45)
    plt.show()
    st.pyplot(fig)

with menu[2]:
    setor = df["setor"].value_counts()
    fig = plt.figure(figsize=(10,6))
    plt.pie(setor, labels=setor.index)
    st.pyplot(fig)

with menu[3]:
    filtro = df["setor"] == "seguro"
    df_setor = df[filtro]
    fig = plt.figure(figsize=(10,6))
    sn.histplot(df["roe"], bins=20, kde=True, color="blue")
    st.pyplot(fig)










#importar a biblioteca 
# import pandas as pd
# selecionar o as colunas que tem o valor EBIT
# df = pd.read_excel("ap2.xlsx", sheet_name="Planilha1")
# df["conta"]
# filtro = df["conta"]=="EBIT"
# df.columns

# # selecionando as colunas 
# colunas = ['Conta', 'Variação Trimestral', 'Variação Anual', '20254T', '20252T',
#        '20251T', '20244T', '20243T', '20242T', '20241T', '20234T', '20233T',
#        '20232T', '20231T', '20224T', '20223T', '20222T', '20221T', '20214T',
#        '20213T', '20212T', '20211T', '20204T', '20203T', '20202T', '20201T',
#        '20194T', '20193T', '20192T', '20191T', '20184T', '20183T', '20182T',
#        '20181T', '20174T', '20173T', '20172T', '20171T', '20164T', '20163T',
#        '20162T', '20161T', '20154T']
# colunas = sorted(colunas)


# ebit = df[filtro][colunas].iloc[0]

# import seaborn as sn
# sn.lineplot(ebit)
# sn.histplot(ebit)
# sn.boxplot(ebit)











# import pandas as pd
# df = pd.read_csv("study_performance.csv")
# df["gender"] 
# df.iloc[567]
# df.iloc[567]["gender"]
# df["math_score"]. mean()
# df["math_score"]. median()
# df["math_score"]. mode()
# df["math_score"]. var()
# df["math_score"]. std()
# df["math_score"]. describe()
# df["math_score"]. plot()



# import pandas as pd 
# pd.read_csv("study_performance.csv")

# import statistics as st
# peso = [3,5,7,9,11,11]
# frequencia = [9,12,6,2,1,12]
# # estatistica descritiva
# st.mean(peso)
# st.median(peso)
# st.mode(peso)
# st.stdev(peso)
# st.variance(peso)
# # correlacão
# preco = [33,25,24,18,12,10,8]
# demanda = [300,400,500,600,70,800,900]
# st.correlation(preco, demanda)

# # regressão
# slope, intercept = st.linear_regression(preco, demanda)


