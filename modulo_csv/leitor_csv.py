import csv
import os
import pandas as pd

def ler_csv_df():
    """Lê o CSV da ANCINE corretamente, ignorando linhas quebradas."""
    
    base_dir = os.path.dirname(__file__)
    caminho_arquivo = os.path.join(
        base_dir,
        "salas-de-exibicao-e-complexos.csv"
    )

    df = pd.read_csv(
        caminho_arquivo,
        sep=";",                # separador correto
        encoding="latin1",      # encoding correto
        on_bad_lines="skip"     # ignora linhas corrompidas
    )
    return df
