import streamlit as st
import pandas as pd
import plotly.express as px
#Titulo e Descricao
st.title("📊 Dashboard  Netflix")
st.write("""
Este dashboard interativo permite analisar os dados da Netflix,
explorando os gêneros mais frequentes e a evolução de filmes e séries ao longo dos anos.
""")
#Carregar Dados/pode usar df no lugar caso voce queira
Grafico=pd.read_csv("NetFlix.csv")
#Limpar Dados
Grafico=Grafico.dropna()
#Filtro Interativos
tipo= st.sidebar.multiselect("Escolha o Tipo:",
                    options=Grafico["type"].unique(),
                    default=Grafico["type"].unique())
Grafico=Grafico[Grafico["type"].isin(tipo)]
anos=st.sidebar.multiselect("Escolha o Ano de Lancamento:",
                    options=Grafico["release_year"].unique(),
                    default=Grafico["release_year"].unique()
)
#Aplicar Filtro 
Grafico=Grafico[Grafico["release_year"].isin(anos)]
if Grafico.empty:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")
else:
    
    #Separar Generos
    df_generos=Grafico["genres"].str.split(", ")
    df_generos=df_generos.explode()
    #Evolucao
    evolucao_tipo = Grafico.groupby(["release_year","type"]).size().reset_index(name="Quantidade")
    #Contar os Top 10
    top_generos=df_generos.value_counts().head(10)
    #Criar Grafico
    df_top = top_generos.reset_index()
    df_top.columns=["Genero", "Quantidade"]
    st.subheader("📊 Resumo")

    col1, col2 = st.columns(2)

    col1.metric("Total de Títulos", len(Grafico))
    col2.metric("Gêneros Únicos", df_generos.nunique())
    fig1=px.bar(df_top,x="Genero",y="Quantidade",text="Quantidade",title="Top 10 generos da Netflix")
    fig1.update_traces(textposition="outside")
    fig1.update_layout(xaxis_tickangle=-45)
    #Mostrar grafico 1
    st.subheader("🎬 Top 10 Gêneros")

    st.write("Este gráfico mostra os gêneros mais frequentes no catálogo da Netflix com base nos filtros selecionados.")
    st.plotly_chart(fig1)
    #Grafico 2
    st.subheader("📈 Evolução ao Longo dos Anos")

    st.write("Este gráfico mostra a evolução da quantidade de filmes e séries ao longo dos anos.")
    fig2 = px.line(evolucao_tipo,x="release_year",y="Quantidade",color="type",title="Evolução dos Filmes e Series ao Longo dos Anos",markers=True)
    fig2.update_layout(
    legend_title="Tipo",
)
    st.plotly_chart(fig2)
