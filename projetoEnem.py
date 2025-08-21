import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# lendo o DF com Pandas
df_enem = pd.read_csv(r'C:\Users\allys\Downloads\microdados_enem_2023\DADOS/MICRODADOS_ENEM_2023.csv', encoding='latin-1', sep=';')

# agrupando notas de acordo com a renda familiar
df_renda = df_enem.groupby('Q006')['NU_NOTA_MT'].mean().reset_index()

# organizando a renda para facilitar a leitura dos dados
q006ToSm = {
    'A':'Nunhuma Renda',
    'B':'Até 1 SM',
    'C':'1-2 SM',
    'D':'2-3 SM',
    'E':'>3 SM',
}

# setando a organização anterior no DF
df_enem['renda_sm'] = df_enem['Q006'].map(q006ToSm)

# agrupando novamente com a coluna nova e organizando de forma ascendente
df_renda = df_enem.groupby('renda_sm')['NU_NOTA_MT'].mean().reset_index()
mediaNota = df_renda.sort_values(by='NU_NOTA_MT', ascending=True)

plt.figure(figsize=(10, 6))
plt.bar(mediaNota['renda_sm'] ,mediaNota['NU_NOTA_MT'], color='skyblue')
plt.xticks(rotation=45)
plt.xlabel('Renda - Salário mínimo')
plt.ylabel('Média de notas')
plt.title('Média de notas por renda')
plt.tight_layout()

plt.show()


# q006_ordinal = {
#     'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
#     'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16
# }

# df_enem['q006_ordinal'] = df_enem['Q006'].map(q006_ordinal)

# print(df_enem[['NU_NOTA_MT', 'q006_ordinal']].head())



