import pandas as pd
import plotly.express as px
import streamlit as st 

df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'Casos por 100 mil habitantes'})

state = st.selectbox('Qual estado?', estados)
estados = list(df['state'].unique())


colunas = ['Novos óbitos','Novos casos','Óbitos por 100 mil habitantes','Casos por 100 mil habitantes']
column = st.selectbox('Qual tipo de informação?', colunas)

df = df[df['state'] == state]

fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID - BRASIL')
st.write('Pode escolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral, por favor.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
st.caption('Um aplicativo feito na Digital Innovation One por https://github.com/marianeneiva - Agosto 2022')

