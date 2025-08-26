from extract import extract_users
from transform import transform_users
from load import load_to_sqlite

def main():
    #Extract  Extrair
    df = extract_users()
    print("Dados extraidos")
    print(df.head())

    #Transform  Transformar
    df = transform_users(df)
    print("\nDados Transformados")
    print(df.head())
    
    #Load  Carregar
    load_to_sqlite(df)

if __name__ == "__main__":
    main()