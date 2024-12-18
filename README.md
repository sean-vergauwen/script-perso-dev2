# Script perso dev2

## Structure du projet
```
script-perso-dev2/
    ├── src/
    │   ├── data_import.py
    │   ├── data_processing.py
    │   ├── data_query.py
    │   ├── main.py
    │   ├── report_generation.py
    ├── tests/
    │   ├── test_data_import.py
    │   ├── test_data_processing.py
    │   ├── test_data_query.py
    │   ├── test_report_generation.py
    ├── outputs/
    ├── data/
    ├── .gitattributes
    ├── .gitignore
    ├── README.md
```

## Installation du projet

Tout d'abord, rendez-vous dans le dossier dans lequel vous voulez installer le projet avec une invite de commande

Une fois que vous êtes dans le dossier qui vous plaît, entrez cette commande :

```
git clone https://github.com/sean-vergauwen/script-perso-dev2.git
```

Attendez que tout s'installe et ensuite rendez vous dans le dossier script-perso-dev2 et créez deux dossiers dans celui-ci comme indiqué dans la structure du projet en haut de la page:
- data
- outputs

Une fois que cela est fait, rendez vous dans le dossier src.

## Exécution de l'application

Cette application possède deux mode distincts, le mode shell interactif et le mode ligne de commande.

Pour lancer le shell interactif il suffit de faire la commande une fois que vous êtes bien dans le dossier src 
```
python main.py --shell
```

A partir de ce moment là tout est guidé.

---

Si vous préférez l'utiliser en ligne de commande alors voici toutes les possibilités

En premier lieu il faut importer les fichiers à consolider, par simplicité je vous conseille de les mettre dans le dossier data
```
python main.py --import CHEMINS_DES_FICHIERS...
```
Exemple :
```
python main.py --import ../data/foo.csv ../data/bar.csv
```

Les données consolidées se trouveront dans le fichier "consolidated_invetory.csv" dans le dossier outputs

---

Ensuite si vous voulez faire des recherches dans le fichier consolidé il suffit de faire cette commande

```
python main.py --query COLONNE condition_de_comparaison VALEUR --sort-by COLONNE --order asc OU desc
```
Exemple d'utilisation:
```
python main.py --query "category == 'Sports'"
python main.py --query "unit_price >= 9.99"
python main.py --query "quantity <= 5"
python main.py --query "unit_price <= 9.99" "category == 'Sports'" --sort-by quantity --order desc
```

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


Le résultat de la recherche sera stocké dans le dossier outputs sous le nom de "momentdelarequête_output.csv"


---

Pour générer un rapport des données consolidées il suffit de faire la commande :
```
python main.py --generate-report
```
Celui-ci se trouvera dans le dossier outputs sous le nom de "report.csv"

---

Si vous voulez simplement afficher toutes les données il suffit de faire la commande :
```
python main.py --show-data
```

---

Et finalement si vous voulez exécuter les tests unitaires ils suffit de faire la commande :
```
python main.py --tests
```
