import pandas as pd

def query_data(file_path, condition):
    """
    Interroge les données consolidées en fonction d'une ou plusieurs condition(s).

    Opérateur supportés:
        - '==' : Egal
        - '!=' : Pas égal
        - '<'  : Plus petit que
        - '<=' : Plus petit ou égal à
        - '>'  : Plus grand que
        - '>=' : Plus grand ou égal à

    Options de tri:
        - asc (par défaut)
        - desc

    Exemples d'utilisation :
        py main.py --query "category == 'Sports'"
        py main.py --query "unit_price >= 9.99"
        py main.py --query "quantity <= 5"
        py main.py --query "unit_price < 9.99" "category == 'Sports'" --sort-by quantity --order desc
    """

    try:
        df = pd.read_csv(file_path)
        for cond in condition:
            df = df.query(cond)
        return df
    except FileNotFoundError:
        print(f"Erreur : le fichier {file_path} est introuvable.")
    except Exception as e:
        print(f"Erreur lors de la requête : {e}")
