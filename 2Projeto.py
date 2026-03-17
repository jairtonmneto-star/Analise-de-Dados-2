import pandas as pd
import plotly.express as px
Grafico=pd.read_csv("NetFlix.csv")
display(Grafico.info())
Grafico=Grafico.dropna()
display(Grafico.info())
#Separar Generos 
df_generos=Grafico["genres"].str.split(", ")
#Tranformar em Linhas
df_generos=df_generos.explode()
#Contar 
top_generos = df_generos.value_counts().head(10)
#Criar Grafico
grafico= px.bar(x=top_generos.index,y=top_generos.values,text=top_generos.values,title="Top 10 Generos da Netflix")
display(grafico)
