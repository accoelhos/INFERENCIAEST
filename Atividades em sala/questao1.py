import pandas as pd
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import pairwise_tukeyhsd


df_metodo = pd.read_csv('https://raw.githubusercontent.com/AILAB-CEFET-RJ/gcc1625/refs/heads/main/data/anova/MetodoEstudo.csv', sep=',')
grupo1 = df_metodo['Nota'][df_metodo.Metodo == 'Individual']
grupo2 = df_metodo['Nota'][df_metodo.Metodo == 'Grupo']
grupo3 = df_metodo['Nota'][df_metodo.Metodo == 'Revisao']

#aplicando ANOVA oneway

f_stat, p_value = f_oneway(grupo1, grupo2, grupo3)
print("Resultado da ANOVA:")
print(f"F = {f_stat:.4f}")
print(f"valor-p = {p_value:.4f}")
if p_value > 0.05:
    print("Não há diferença significativa")
else:
    print("Há diferença significativa. Devemos aplicar o teste de Turkey.")

# Teste de Tukey
tukey = pairwise_tukeyhsd(endog=df_metodo["Nota"], groups=df_metodo["Metodo"], alpha=0.05)

dataframe=pd.DataFrame(data=tukey.summary().data[1:], columns=tukey.summary().data[0])

print("Resumo do Teste de Tukey:")
print(dataframe)
dataframe.head()
