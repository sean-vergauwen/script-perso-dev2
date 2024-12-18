import pandas as pd

def import_csv_files(file_paths):
    """
    Importe plusieurs fichiers CSV et retourne une liste de DataFrames.

    Prend en entrée une liste de chemins de fichier CSV et retourne une liste de DataFrames.
    """
    data_frames = []
    for path in file_paths:
        try:
            df = pd.read_csv(path)
            data_frames.append(df)
        except FileNotFoundError:
            print(f"Erreur : le fichier {path} est introuvable.")
        except Exception as e:
            print(f"Erreur lors de l'importation de {path} : {e}")
    return data_frames
