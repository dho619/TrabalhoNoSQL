import pandas as pd
import matplotlib.pyplot as plt

#testeExcel = pd.read_excel('./teste.xlsx')
data = pd.read_csv('./athlete_events.csv')

#dicionario
alunos = {
            'Nome'    : ['Ricardo', 'Pedro', 'Roberto', 'Carlos'],
            'Nota'    : [    4    ,    7   ,    5.5   ,     9   ],
            'Aprovado': [  'Não'  ,  'Sim' ,   'Não'  ,   'Sim' ]
         }

#dicionario para DataFrame
df = pd.DataFrame(alunos)

#Cria um vetor com indices unidimencionais, ele possui indices
obj = pd.Series([0,6,9,8,3],['a','b','c','d','e'])

#print(df.shape)#numero de linhas e de colunas
#print(df.describe())#informacoes gerais de colunas numericas
#print(df['Nome'])#uma coluna específica
#print(df.loc[[0,2]])#pegar linhas que estao no vetor
#print(df.loc[0:2])#pegar linhas que estao entre os valores
#print(df.loc[df['Nome'] == 'Pedro'])#filtrar uma linha

#renomear colunas
newsData = data.rename(columns={'Name':'Nome', 'Sex': 'Sexo'})

#imprimir tds colunas
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(newsData.head())

#pegar os valores únicos e quantos tem
#print(data['City'].value_counts())

newsData.drop('ID', axis=1, inplace=True)#apaga a coluna
#axis=1 selecionar coluna, inplace=True manter a alteracao nesse dataSet

data.hist(column='Age', bins=100)
plt.show()
