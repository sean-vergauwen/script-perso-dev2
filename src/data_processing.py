import pandas as pd

def consolidate_data(data_frames):
    """
    Consolide plusieurs DataFrames prise en entrée en une seule, supprime les doublons et sauvegarde le résultat dans un fichier CSV.
    """
    if not data_frames:
        print("Aucune donnée à consolider.")
        return
    consolidated_data = pd.concat(data_frames, ignore_index=True)
    consolidated_data.drop_duplicates(inplace=True)
    consolidated_data.to_csv('../outputs/consolidated_inventory.csv', index=False)
    print("Données consolidées et sauvegardées dans 'outputs/consolidated_inventory.csv'.")
