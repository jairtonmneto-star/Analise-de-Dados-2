import streamlit as st
import pandas as pd
import plotly.express as px
#Titulo
st.title("Dashboar de Vendas")
#Carregar Dados
Grafico=pd.read_csv("NetFlix.csv")
#Limpar Dados
Grafico=Grafico.dropna()
#Filtro Interativos
anos=st.multiselect("Escolha o Ano de Lancamento:",
                    options=Grafico["release_year"].unique(),
                    default=Grafico["release_year"].unique()
)
#Aplicar Filtro 
Grafico=Grafico[Grafico["release_year"].isin(anos)]
#Separar Generos
df_generos=Grafico["genres"].str.split(", ")
df_generos=df_generos.explode()
#Contar os Top 10
top_generos=df_generos.value_counts().head(10)
#Criar Grafico
fig= px.bar(x=top_generos.index,y=top_generos.values,text=top_generos.values,title="Top 10 Generos da Netflix")
#Mostrar grafico
st.plotly_chart(fig)
