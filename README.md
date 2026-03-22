# 📊 Análise de Dados - Netflix

**Autor:** José Airton

---

## 🎯 Objetivo

Analisar os dados da Netflix para identificar quais gêneros possuem maior quantidade de títulos no catálogo, com foco em programas de TV e filmes.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Pandas
* Plotly Express
* VS Code
* Streamlit (dashboard interativo)

---

## 📁 Base de Dados

Dataset utilizado:
https://www.kaggle.com/datasets/imtkaggleteam/netflix

---

## ▶️ Como Executar

1. Baixe o dataset no link acima
2. Clone este repositório ou baixe os arquivos
3. Abra o projeto no VS Code
4. Ative o ambiente virtual (opcional)
5. Instale as dependências:

   ```bash
   pip install pandas plotly streamlit
   ```
6. Execute o dashboard:

   ```bash
   streamlit run app.py
   ```

---

## 🔍 Etapas da Análise

1. Limpeza dos dados (remoção de valores nulos)
2. Separação dos gêneros (`genres`)
3. Transformação dos dados com `explode()`
4. Contagem dos gêneros mais frequentes
5. Criação de visualizações interativas

---

## 📊 Resultados

Os gêneros mais frequentes encontrados foram:

1. Filmes Internacionais *(pode variar conforme o filtro)*
2. Dramas
3. Comédia
4. Ação e Aventura
5. Filmes Independentes
6. Filmes Românticos
7. Documentários
8. Terror
9. Infantil e Família
10. Outros

---

## 📈 Insights

* A Netflix possui forte predominância de conteúdos narrativos
* Gêneros como **Drama** e **Comédia** dominam o catálogo
* Há grande diversidade de conteúdos internacionais

---

## 🧠 Conclusão

A análise mostra que a Netflix concentra grande parte do seu catálogo em conteúdos populares e amplamente consumidos, com destaque para drama e comédia, indicando foco em engajamento do público.

---

## 📌 Possíveis Melhorias

* Separar análise entre filmes e séries (`type`)
* Analisar evolução ao longo dos anos
* Criar dashboard interativo com filtros
* Analisar distribuição por país
* Avaliar duração média dos títulos

---

## 🚀 Projeto em Desenvolvimento

Este projeto foi evoluído para um dashboard interativo utilizando Streamlit, permitindo análise dinâmica dos dados com filtros por ano e tipo de conteúdo.

