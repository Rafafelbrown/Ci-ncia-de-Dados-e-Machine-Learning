#fazer linha 2 e 3 antes para funcinoa no terminal
#pip install pandas 
#pip install numpy      
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

("(╬▔皿▔)╯")# fique atento ao oque vc esta importando 
data_atual = datetime.now().strftime('%Y-%m-%d-%H-%M')
url = input("Qual a URL do arquivo CSV?\n")
dados = pd.read_csv(url)
print(dados)
coluna = input("Qual a coluna que você quer analisar?\n")
print("Média:\n", np.mean(dados[coluna]))
print("Variância:\n", np.var(dados[coluna]))
print("Desvio padrão:\n", np.std(dados[coluna]))
print("Primeiro quartil:\n", np.quantile(dados[coluna], 0.25))
print("Segundo quartil:\n", np.nanquantile(dados[coluna], 0.5))
print("Terceiro quartil:\n", np.nanquantile(dados[coluna], 0.75))
("(┬┬﹏┬┬)")# escrita no arquivo 

filename = f"analise_dados-{coluna}{data_atual}.csv"
dados_analise = pd.DataFrame({
    "coluna": [coluna],
    "media": [np.mean(dados[coluna])],
    "variancia": [np.var(dados[coluna])],
    "desvio_padrao": [np.std(dados[coluna])],
    "primeiro_quartil": [np.quantile(dados[coluna], 0.25)],
    "segundo_quartil": [np.nanquantile(dados[coluna], 0.5)],
    "terceiro_quartil": [np.nanquantile(dados[coluna], 0.75)]
})
dados_analise.to_csv(filename, index=False)
print("As informações foram salvas em", filename)
print("ಥ_ಥ    parabéns funcionou")# deu trabalho
#gerando o garafico
plt.hist(dados[coluna], bins=20, density=False)
plt.title(f"Histograma da coluna {coluna}")
plt.xlabel(coluna)
plt.ylabel("Frequência")
plt.show()

print("filnalmete funcionou, quase 3 semanas so para o grafico.")









 #feito pele rafael andrade













 #feito pele rafael andrade