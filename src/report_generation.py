import pandas as pd

def generate_report(file_path):
    """
    Génére un rapport récapitulatif à partir des données consolidées.
    """
    try:
        df = pd.read_csv(file_path)
        report = df.groupby('category').agg(
            total_quantity=('quantity', 'sum'),
            total_value=('unit_price', lambda x: (x * df.loc[x.index, 'quantity']).sum())
        ).reset_index()
        report.to_csv('../outputs/report.csv', index=False)
        print("Rapport généré et sauvegardé dans 'outputs/report.csv'.")
        return report
    except FileNotFoundError:
        print(f"Erreur : le fichier {file_path} est introuvable.")
    except Exception as e:
        print(f"Erreur lors de la génération du rapport : {e}")
