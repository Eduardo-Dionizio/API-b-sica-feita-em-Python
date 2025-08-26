import pandas as pd

def transform_users(df : pd.DataFrame) -> pd.DataFrame:
    #Selecionar as colunas relevantes
    df = df[["id", "name", "username", "email"]]

    #Normalizar o texto
    df["name"] = df["name"].str.lower()

    #Criar coluna extra
    df["tamanho_nome"]= df["name"].apply(len)

    return df