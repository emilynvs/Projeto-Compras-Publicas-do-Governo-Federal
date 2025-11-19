from api import consultar_grupo_material
import pandas as pd

dados = consultar_grupo_material(1)
df = pd.DataFrame(dados["resultado"])

# Remove linhas totalmente vazias
df = df.dropna(how="all")

# Preenchimentos seguros
if "nomeGrupo" in df.columns:
    df["nomeGrupo"] = df["nomeGrupo"].fillna("DESCONHECIDO")

if "statusGrupo" in df.columns:
    df["statusGrupo"] = df["statusGrupo"].fillna(False)

# Para datas, usar pd.NaT
if "dataHoraAtualizacao" in df.columns:
    df["dataHoraAtualizacao"] = pd.to_datetime(df["dataHoraAtualizacao"], errors="coerce")
    df["dataHoraAtualizacao"] = df["dataHoraAtualizacao"].fillna(pd.NaT)

# Normalização strings
if "nomeGrupo" in df.columns:
    df["nomeGrupo"] = df["nomeGrupo"].astype(str).str.strip().str.upper()

# Remover duplicatas
df = df.drop_duplicates()

# Reset de índice
df.reset_index(drop=True, inplace=True)

print(df)
print("\nCOLUNAS:", df.columns)
