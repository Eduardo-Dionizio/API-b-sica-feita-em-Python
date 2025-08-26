import sqlite3
import pandas as pd

def load_to_sqlite(df: pd.DataFrame, db_name ="usuarios.db"):
    con = sqlite3.connect(db_name)
    df.to_sql("usuarios", con, if_exists = "replace", index = False)
    con.close()
    print("Dados carregados com sucesso ao SQLite!!")
    