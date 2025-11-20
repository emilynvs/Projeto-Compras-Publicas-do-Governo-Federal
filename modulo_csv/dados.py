from leitor_csv import ler_csv_df
import pandas as pd

# ler o csv e transforma o mesmo em um dataframe 
df = ler_csv_df()
print(df)

# isso aqui eu estava testando apenas as colunas que vamos utilizar para solucionar o problema o qual nós escolhemos 
# caso queira ver apenas essas colunas descomente 
"""colunas_desejadas = [
    "UF_COMPLEXO",
    "MUNICIPIO_COMPLEXO",
    "ASSENTOS_CADEIRANTES",
    "ASSENTOS_MOBILIDADE_REDUZIDA",
    "ASSENTOS_OBESIDADE",
    "ACESSO_ASSENTOS_COM_RAMPA",
    "ACESSO_SALA_COM_RAMPA",
    "BANHEIROS_ACESSIVEIS",
    "DATA_SITUACAO_COMPLEXO"
]

# código padrão para remover duplicados e nulos transformando os mesmos em 0, ou seja, quando você rodar o código normal vbai aparecer
# NaN, com esse df aparecerá 0.00
df = df.drop_duplicates()
df = df.fillna(0)

# esse aqui é o dataframe diltrado para a soloução especifica do nosso problema
df_filtrado = df[colunas_desejadas]

print(df_filtrado)"""

# caso queira exportar em excel o filtrado tá aqui 
#df_filtrado.to_excel("salas_filtrado.xlsx", index=False)

#caso queira exportar o geral filtrado tá aqui 
#df.to_excel("salas_df.xlsx", index=False)
