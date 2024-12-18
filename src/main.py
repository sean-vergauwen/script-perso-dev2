import argparse, sys, unittest
from logging import exception
from pathlib import Path
import pandas as pd
from src.data_import import import_csv_files
from src.data_processing import consolidate_data
from src.data_query import query_data
from src.report_generation import generate_report

def import_files(files):
    data = import_csv_files(files)
    if data:
        consolidate_data(data)
    else:
        print("Aucune donnée importée.")

def query(user_query, sort_by, order):
    result = query_data('../outputs/consolidated_inventory.csv', user_query)
    try:
        if sort_by:
            if order == "asc":
                order = True
            else:
                order = False
            result = result.sort_values(by=sort_by, ascending=order)
    except Exception as e:
        print(f"Erreur : {e})")

    print(result)

def run_tests():
    # Get the project root directory
    project_root = Path(__file__).parent.parent

    # Add the project root to Python path to ensure imports work correctly
    sys.path.insert(0, str(project_root))

    # Discover and run tests
    loader = unittest.TestLoader()
    test_dir = project_root / 'tests'
    suite = loader.discover(str(test_dir))

    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    return result.wasSuccessful()

def mode_shell():
    while True:
        print("")
        print("Système de gestion d’inventaire")
        print("")
        print("(1) Importer des fichiers CSV à consolider en un seul fichier CSV")
        print("(2) Faire des recherches sur les données consolidées")
        print("(3) Afficher les données consolidées")
        print("(4) Générer un rapport par catégorie sur les données consolidées")
        print("(5) Fermer le programme")
        choix = input("Faites votre choix (1..5) : ")
        print("")

        match choix:
            case "1":
                print("Importez des fichiers CSV en écrivant le chemin vers ceux-ci de cette manière (avec un espace entre chaque chemin de fichier) : ../data/sports.csv ../data/tools.csv ...")
                str_chemins_fichiers = input("Chemin des fichiers : ")

                liste_chemins_fichiers  = str_chemins_fichiers.split()
                import_files(liste_chemins_fichiers)
            case "2":
                print("Faites des recherches sur les données consolidées de cette manière (avec un # entre chaque requête : unit_price < 9.99 # category == 'Sports'")
                str_query = input("Chemin des fichiers : ")
                liste_query = str_query.split(' # ')
                print(liste_query)

                print("Si vous voulez trier les données sur une colonne en particulier, entrez le nom de la catégorie ou laissez vide si non")
                str_colonne = input("Nom de la colonne : ")

                asc_ou_desc = "asc"

                if str_colonne:
                    print("Voulez vous que le tri soit fait de manière croissante ou décroissante ?")
                    print("(1) Croissante")
                    print("(2) Décroissante")
                    choix_asc_ou_desc = input("Faites votre choix (1..2) : ")
                    match choix_asc_ou_desc:
                        case "2":
                            asc_ou_desc = "desc"
                        case _:
                            print("Valeur invalide -> passage sur la valeur par défaut : Croissant")

                print("")
                query(liste_query, str_colonne, asc_ou_desc)
            case "4":
                generate_report('../outputs/consolidated_inventory.csv')
            case "3":
                try:
                    print(pd.read_csv('../outputs/consolidated_inventory.csv'))
                except FileNotFoundError:
                    print("Aucune données consolidées à afficher")
            case "5":
                print("Au revoir !")
                break
            case _:
                print("Mauvais choix ! Veuillez écrire un chiffre entre 1 et 5 inclus.")

def main():
    parser = argparse.ArgumentParser(description="Système de gestion d'inventaire.")
    parser.add_argument('--shell', action='store_true', help="Tourne le programme en mode shell")
    parser.add_argument('--import-files', nargs='+', help="Importer des fichiers CSV.")
    parser.add_argument('--query',help=
    """
    Interroge les données consolidées en fonction d'une ou plusieurs condition(s).

    Exemples d'utilisation :
        py main.py --query "category == 'Sports'" |
        py main.py --query "unit_price >= 9.99" |
        py main.py --query "quantity <= 5" |
        py main.py --query "unit_price < 9.99" "category == 'Sports'" --sort-by quantity --order desc
    """, nargs='*')
    parser.add_argument('--generate-report', action='store_true', help="Générer un rapport.")
    parser.add_argument('--show-data', action='store_true', help="Affiche les données consolidées")
    parser.add_argument('--tests', action='store_true', help='Run les tests')
    parser.add_argument("--sort-by", type=str, help="Colomne par laquelle les résultats sont triés")
    parser.add_argument("--order", type=str, choices=["asc", "desc"], default="asc", help="Ordre du tri: 'asc' (default) or 'desc'")

    args = parser.parse_args()

    if args.shell:
        mode_shell()

    elif args.import_files:
        import_files(args.import_files)

    elif args.query:
        query(args.query, args.sort_by, args.order)

    elif args.generate_report:
        generate_report('../outputs/consolidated_inventory.csv')

    elif args.show_data:
        try:
            print(pd.read_csv('../outputs/consolidated_inventory.csv'))
        except FileNotFoundError:
            print("Aucune données consolidées à afficher")

    elif args.tests:
        print("Running tests...")
        tests_passed = run_tests()
        if args.tests:
            sys.exit(0 if tests_passed else 1)

        if not tests_passed:
            print("Tests failed! Please fix the issues before running the application.")
            sys.exit(1)

if __name__ == "__main__":
    main()
