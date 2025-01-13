import pandas as pd
import streamlit as st
import plotly_express as px

# Lendo os dados
car_data = pd.read_csv(r'C:\Users\Thiago\Desktop\ProjetoGit\tripleten\project_sprint5\vehicles.csv')

# Título da página
st.title('Análise de Dados de Veículos')

# Botões para gráficos
hist_checkbox = st.checkbox('Exibir histograma')  # Caixa de seleção para histograma
scatter_checkbox = st.checkbox('Exibir gráfico de dispersão')  # Caixa de seleção para gráfico de dispersão

# Se o histograma for selecionado
if hist_checkbox:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig_hist = px.histogram(car_data, x="odometer", title="Histograma do Odometer")
    st.plotly_chart(fig_hist, use_container_width=True)  # Exibir histograma

# Se o gráfico de dispersão for selecionado
if scatter_checkbox:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Gráfico de Dispersão: Odometer vs Price")
    st.plotly_chart(fig_scatter, use_container_width=True)  # Exibir gráfico de dispersão

